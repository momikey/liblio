### User settings, such as profile and display options

from datetime import datetime

from flask import Blueprint, jsonify, make_response, current_app
from flask_jwt_extended import jwt_required, get_jwt_identity
from webargs import fields, validate
from webargs.flaskparser import use_args

from liblio import db, jwt
from liblio.error import APIError
from liblio.models import User
from . import API_PATH

BLUEPRINT_PATH="{api}/settings".format(api=API_PATH)

blueprint = Blueprint('settings', __name__, url_prefix=BLUEPRINT_PATH)

### Request schemas

request_schemas = {
    'edit_profile': {
        'name': fields.Str(),
        'bio': fields.Str(),
        'role': fields.Int(missing=0),
        'tags': fields.List(fields.Int())
    }
}

### Routes

@blueprint.route('/my-profile', methods=('GET',))
@jwt_required
def get_my_profile():
    """Get the profile for the logged-in user. (This may have sensitive/private info.)"""

    username = get_jwt_identity()
    origin = current_app.config['SERVER_ORIGIN']

    profile = User.query.filter_by(username=username, origin=origin).first()
    if profile is None:
        # This shouldn't happen.
        raise APIError(400, "User {username} does not exist on this server".format(username=username))

    # Update last activity time
    profile.login.last_action = datetime.now()

    return make_response(jsonify(profile=profile.to_dict()), 200)

@blueprint.route('/edit-profile', methods=('POST',))
@jwt_required
@use_args(request_schemas['edit_profile'])
def edit_profile(args):
    """Edit a user's profile."""

    username = get_jwt_identity()
    origin = current_app.config['SERVER_ORIGIN']

    profile = User.query.filter_by(username=username, origin=origin).first()
    if profile is None:
        # This shouldn't happen, but an attacker could feasibly try to edit
        # a nonexistent profile.
        raise APIError(400, "User {username} does not exist on this server".format(username=username))

    new_name = args['name']
    new_bio = args['bio']

    if new_name is not None:
        profile.display_name = new_name
    
    if new_bio is not None:
        profile.bio = new_bio
    
    # TODO: do the same thing for roles and tags, once they're implemented

    # This is an API action, so update the activity timestamp
    profile.login.last_action = datetime.now()

    db.session.add(profile)
    db.session.commit()

    return make_response(jsonify(msg="Profile updated"), 200)


### Helper functions