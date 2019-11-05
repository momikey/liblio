### User settings, such as profile and display options

from datetime import datetime

from flask import Blueprint, jsonify, make_response, current_app, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from webargs import fields, validate
from webargs.flaskparser import use_args
from flask_uploads import UploadNotAllowed

from liblio import db, jwt, liblio_uploads
from liblio.error import APIError
from liblio.models import User, Tag, Avatar
from liblio.helpers import flake_id, printable_id
from . import API_PATH

BLUEPRINT_PATH="{api}/settings".format(api=API_PATH)

blueprint = Blueprint('settings', __name__, url_prefix=BLUEPRINT_PATH)

### Request schemas

request_schemas = {
    'edit_profile': {
        'name': fields.Str(),
        'bio': fields.Str(),
        'tags': fields.List(fields.Str()),
        'private': fields.Boolean(missing=False),
        'settings': fields.Dict()
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

    return make_response(jsonify(profile=profile.to_profile_dict()), 200)

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
    new_tags = args['tags']

    if new_name is not None:
        profile.display_name = new_name
    
    if new_bio is not None:
        profile.bio = new_bio
    
    if new_tags is not None:
        profile.tags = Tag.query.filter(Tag.name.in_(new_tags)).all()
    # TODO: do the same thing for roles and tags, once they're implemented

    # This is an API action, so update the activity timestamp
    profile.login.last_action = datetime.now()

    db.session.add(profile)
    db.session.commit()

    return make_response(jsonify(profile=profile.to_profile_dict()), 200)

@blueprint.route("/me", methods=('GET',))
@jwt_required
def get_my_info():
    """Get the likes, shares, and following/followed lists for the logged-in user."""

    username = get_jwt_identity()
    origin = current_app.config['SERVER_ORIGIN']

    profile = User.query.filter_by(username=username, origin=origin).first()
    if profile is None:
        # This shouldn't happen.
        raise APIError(400, "User {username} does not exist on this server".format(username=username))

    # Update last activity time
    profile.login.last_action = datetime.now()

    return jsonify(
        likes=[l.id for l in profile.likes],
        shares=[s.id for s in profile.sharing],
        followers=[f.id for f in profile.followers],
        following=[f.id for f in profile.following]
    ), 200

@blueprint.route("/edit-avatar", methods=('POST',))
@jwt_required
def edit_avatar():
    """Change the avatar of the logged-in user."""

    username = get_jwt_identity()
    origin = current_app.config['SERVER_ORIGIN']

    profile = User.query.filter_by(username=username, origin=origin).first()
    if profile is None:
        # This shouldn't happen, but an attacker could feasibly try to edit
        # a nonexistent profile.
        raise APIError(400, "User {username} does not exist on this server".format(username=username))

    # Get the new avatar from the request and put it in the DB
    if 'avatar' in request.files:
        for f in request.files.getlist('avatar'):
            try:
                fid = flake_id()
                name_with_id = printable_id(fid) + f.name
                filename = liblio_uploads.save(f)
                avatar = Avatar(flake=fid, filename=filename, user=profile)
                profile.current_avatar = avatar

                db.session.add(avatar, profile)
                db.session.commit()

                return jsonify(msg="Avatar changed for user {0}".format(profile.username)), \
                    200, \
                    { 'Location': avatar.uri }
            except UploadNotAllowed as error:
                print("Upload failed: {0}", str(error))
                raise APIError(415, "Can't upload files of this type")
