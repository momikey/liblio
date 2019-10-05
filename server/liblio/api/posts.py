### CRUD operations for posts, except probably not the U part

from flask import Blueprint, current_app, jsonify, make_response, request
from flask_jwt_extended import get_jwt_identity, jwt_required
from webargs import fields, validate
from webargs.flaskparser import use_args
from datetime import datetime

from liblio import db, jwt
from liblio.error import APIError
from liblio.models import Post, User, Login
from liblio.helpers import decode_printable_id
from . import API_PATH

BLUEPRINT_PATH="{api}/post".format(api=API_PATH)

blueprint = Blueprint('posts', __name__, url_prefix=BLUEPRINT_PATH)

### Request schemas
request_schemas = {
    'new_post': {
        'subject': fields.Str(required=False),
        'source': fields.Str(required=True),
        'parent_id': fields.Int(required=False)
    }
}

### Routes

@blueprint.route('/by-id/<int:post_id>')
def get_by_id(post_id):
    """Get the post with the given database ID."""
    post = Post.query.get(post_id)

    if post is not None:
        return jsonify(post.to_dict()), 200
    else:
        raise APIError(404, "Post with ID {id} does not exist on this server".format(id=post_id))

@blueprint.route('/by-flake/<flake_id>')
def get_by_flake(flake_id):
    """Get the post with the given Flake ID."""
    post = Post.query.filter_by(flake=decode_printable_id(flake_id)).first()

    if post is not None:
        return jsonify(post.to_dict()), 200
    else:
        raise APIError(404, "Post with Flake ID {id} does not exist on this server".format(id=flake_id))

@blueprint.route('/public')
def get_public_posts():
    """Get the posts in the public timeline."""
    since = datetime.utcfromtimestamp(int(request.args.get('since', 0)))
    count = request.args.get('max', None)

    query = Post.query.filter(Post.timestamp > since).filter(User.private is not True).order_by(Post.timestamp.desc())

    results = query.all() if count is None else query[:int(count)]

    return jsonify([r.to_dict() for r in results]), 200

@blueprint.route('/new', methods=('POST',))
@jwt_required
@use_args(request_schemas['new_post'])
def create_post(args):
    """Create a new post."""
    username = get_jwt_identity()

    login = Login.query.filter_by(username=username).first()

    if login is None:
        raise APIError(400, "User {username} does not exist on this server".format(username=username))

    post = Post(
        user=login.user,
        subject=args.get('subject'),
        source=args['source'],
    )

    # Posts without parents are allowed; they're just "top-level"
    parent_id = args.get('parent_id')
    if parent_id is not None:
        post.parent_id = parent_id

    # This does affect the "last active" time
    login.last_action = datetime.now()

    db.session.add(post, login)    
    db.session.commit()

    return jsonify(post.to_dict()), 201, { 'Location': post.uri }

@blueprint.route('/like/<int:post_id>', methods=('POST', 'PUT'))
@jwt_required
def like_post(post_id):
    """Like the post with a given ID."""
    username = get_jwt_identity()

    login = Login.query.filter_by(username=username).first()

    if login is None:
        raise APIError(400, "User {username} does not exist on this server".format(username=username))

    if post_id not in [p.id for p in login.user.likes]:
        post = Post.query.get(post_id)
        login.user.likes.append(post)

        login.last_action = datetime.now()
        db.session.add(post, login)
        db.session.commit()

    return jsonify({ 'likes': [p.id for p in login.user.likes] }), 201

@blueprint.route('/like/<int:post_id>', methods=('DELETE',))
@jwt_required
def remove_like(post_id):
    """Remove a like from a given post."""
    username = get_jwt_identity()

    login = Login.query.filter_by(username=username).first()

    if login is None:
        raise APIError(400, "User {username} does not exist on this server".format(username=username))

    likes_ids = [p.id for p in login.user.likes]
    if post_id in likes_ids:
        post = login.user.likes[likes_ids.index(post_id)]
        del login.user.likes[likes_ids.index(post_id)]

        login.last_action = datetime.now()
        db.session.add(post, login)
        db.session.commit()

        return jsonify({ 'likes': [p.id for p in login.user.likes] }), 200
    else:
        # Trying to remove the like from a post that isn't liked
        raise APIError(404, "User has not liked this post")

@blueprint.route('/share/<int:post_id>', methods=('POST', 'PUT'))
@jwt_required
def share_post(post_id):
    """Share (aka boost/announce) a given post."""
    username = get_jwt_identity()

    login = Login.query.filter_by(username=username).first()

    if login is None:
        raise APIError(400, "User {username} does not exist on this server".format(username=username))

    if post_id not in [p.id for p in login.user.sharing]:
        post = Post.query.get(post_id)
        login.user.sharing.append(post)

        login.last_action = datetime.now()
        db.session.add(post, login)
        db.session.commit()

    return jsonify(sharing=[p.id for p in login.user.sharing]), 201

@blueprint.route('/share/<int:post_id>', methods=('DELETE',))
@jwt_required
def unshare_post(post_id):
    """Remove a share from a given post."""
    username = get_jwt_identity()

    login = Login.query.filter_by(username=username).first()

    if login is None:
        raise APIError(400, "User {username} does not exist on this server".format(username=username))

    share_ids = [p.id for p in login.user.sharing]
    if post_id in share_ids:
        post = login.user.sharing[share_ids.index(post_id)]
        del login.user.sharing[share_ids.index(post_id)]

        login.last_action = datetime.now()
        db.session.add(post, login)
        db.session.commit()

        return jsonify(sharing=[p.id for p in login.user.sharing]), 200
    else:
        # Trying to remove the share from a post that isn't shared
        raise APIError(404, "User has not shared this post")

@blueprint.route('/tree/<int:post_id>')
def get_post_tree(post_id):
    """Get the post and all its descendants."""

    # The given post is the root of a tree of arbitrary depth,
    # so we use a recursive query to get the IDs of all the
    # posts lower in the tree, then use that list to fetch only
    # the needed posts. SQLAlchemy handles setting up the relations.

    root = Post.query.get(post_id)

    included = db.session.query(
        Post.id).filter(Post.parent_id == root.id).cte(name="included", recursive=True)

    included_alias = db.aliased(included, name="parent")
    children_alias = db.aliased(Post, name="child")

    included = included.union_all(
        db.session.query(children_alias.id).filter(children_alias.parent_id == included_alias.c.id)
    )

    # The DB returns the results in tuples, so we extract them here
    post_ids = sorted([root.id] + [t[0] for t in db.session.query(included.c.id).distinct().all()])

    posts = Post.query.filter(Post.id.in_(post_ids)).all()

    return jsonify([p.to_dict() for p in posts]), 200