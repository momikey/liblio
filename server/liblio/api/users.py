### Anything to do with users, mostly retrieving information about them.

from flask import Blueprint, current_app, jsonify, make_response
from flask_jwt_extended import jwt_required, get_jwt_identity
from webargs import fields, validate
from webargs.flaskparser import parser
from datetime import datetime

from liblio import db, jwt
from liblio.error import APIError
from liblio.models import User, Login
from . import API_PATH

BLUEPRINT_PATH="{api}/user".format(api=API_PATH)

blueprint = Blueprint('users', __name__, url_prefix=BLUEPRINT_PATH)

### Request schemas

### Routes

@blueprint.route('/by-id/<int:user_id>')
def get_by_id(user_id):
    """Get the user with the given database ID"""
    user = User.query.get(user_id)

    if user is not None:
        return jsonify(user.to_dict()), 200
    else:
        raise APIError(404, "User with ID {id} does not exist on this server".format(id=user_id))

@blueprint.route('/by-name/<username>')
def get_by_name(username):
    """Find a user by name. This can be done in one of two ways. For local users,
    simply passing the username will find the user with that name. If the query
    parameter contains an @ character, the search will instead be across all known
    servers.

    Examples:
    * "/by-name/foo" searches for a user named "foo" on this server.
    * "/by-name/foo@example.com" searches for a user with the name "foo" from
        the origin server "example.com".
    """

    if '@' in username:
        # Username/origin pair, so search both
        name, origin = username.split('@')
        user = User.query.filter_by(username=name, origin=origin).first()

        if user is not None:
            return jsonify(user.to_dict()), 200
        else:
            raise APIError(404, "No user {username} found.".format(username=username))
    else:
        # Local username search
        user = User.query.filter_by(username=username).first()

        if user is not None:
            return jsonify(user.to_dict()), 200
        else:
            raise APIError(404, "User {name} does not exist on this server".format(name=username))

@blueprint.route('/all')
def get_all_users():
    """Get a list of all users this server knows."""
    users = User.query.all()

    return jsonify([u.to_dict() for u in users]), 200

@blueprint.route('/public')
def get_public_users():
    """Get a list of all users whose profiles are public."""
    users = User.query.filter_by(private=False).all()

    return jsonify([u.to_dict() for u in users]), 200

@blueprint.route('/posts-by-id/<int:user_id>')
def get_posts_by_id(user_id):
    """Get all posts for the user with the given database ID."""
    user = User.query.get(user_id)

    if user is not None:
        return jsonify([p.to_dict() for p in user.posts]), 200
    else:
        raise APIError(404, "User with ID {id} does not exist on this server".format(id=user_id))

@blueprint.route('/followers/<int:user_id>', methods=('GET',))
def get_user_followers(user_id):
    """Get all of a user's followers."""
    user = User.query.get(user_id)

    if user is not None:
        return jsonify([f.to_dict() for f in user.followers]), 200
    else:
        raise APIError(404, "User with ID {id} does not exist on this server".format(id=user_id))

@blueprint.route('/following/<int:user_id>', methods=('GET',))
def get_user_following(user_id):
    """Get all users this user is following."""
    user = User.query.get(user_id)

    if user is not None:
        return jsonify([f.to_dict() for f in user.following]), 200
    else:
        raise APIError(404, "User with ID {id} does not exist on this server".format(id=user_id))

@blueprint.route('/follow/<int:user_id>', methods=('POST', 'PUT'))
@jwt_required
def follow_user(user_id):
    """Follow the user with a given ID."""
    username = get_jwt_identity()

    login = Login.query.filter_by(username=username).first()

    if login is None:
        raise APIError(400, "User {username} does not exist on this server".format(username=username))

    following_user = login.user

    followed_user = User.query.get(user_id)
    if followed_user is None:
        raise APIError(404, "Attempting to follow a user who does not exist")

    if user_id not in [u.id for u in following_user.following]:
        following_user.following.append(followed_user)

        login.last_action = datetime.now()
        db.session.add(following_user, login)
        db.session.commit()

    return jsonify([u.to_dict() for u in following_user.following]), 201

@blueprint.route('/follow/<int:user_id>', methods=('DELETE',))
@jwt_required
def unfollow_user(user_id):
    """Stop following the user with a given ID."""
    username = get_jwt_identity()

    login = Login.query.filter_by(username=username).first()

    if login is None:
        raise APIError(400, "User {username} does not exist on this server".format(username=username))

    following_user = login.user

    followed_user = User.query.get(user_id)
    if followed_user is None:
        raise APIError(404, "Attempting to follow a user who does not exist")

    follow_ids = [f.id for f in following_user.following]
    if user_id in follow_ids:
        del following_user.following[follow_ids.index(user_id)]

        login.last_action = datetime.now()
        db.session.add(following_user, login)
        db.session.commit()

    return jsonify([u.to_dict() for u in following_user.following]), 200