### Anything to do with users, mostly retrieving information about them.

from flask import Blueprint, current_app, jsonify, make_response
from flask_jwt_extended import jwt_required, get_jwt_identity
from webargs import fields, validate
from webargs.flaskparser import parser

from liblio import db, jwt
from liblio.error import APIError
from liblio.models import User
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
        return make_response(jsonify(user.to_dict()), 200)
    else:
        raise APIError(404, "User with ID {id} does not exist on this server".format(id=user_id))

@blueprint.route('/all')
def get_all_users():
    """Get a list of all users this server knows."""
    users = User.query.all()

    return make_response(jsonify([u.to_dict() for u in users]), 200)

@blueprint.route('/public')
def get_public_users():
    """Get a list of all users whose profiles are public."""
    users = User.query.filter_by(private=False).all()

    return make_response(jsonify([u.to_dict() for u in users]), 200)