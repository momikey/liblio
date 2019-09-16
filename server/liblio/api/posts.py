### CRUD operations for posts, except probably not the U part

from flask import Blueprint, current_app, jsonify, make_response
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
        'parent_id': fields.Int(require=False)
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

    return jsonify({ 'likes': [p.id for p in login.user.likes] }), 200

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