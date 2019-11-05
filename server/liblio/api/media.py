# API endpoints for uploaded media, including avatars

from flask import Blueprint, current_app, jsonify, request, send_from_directory, send_file
from flask_jwt_extended import get_jwt_identity, jwt_required

from liblio import db, jwt, liblio_uploads
from liblio.error import APIError
from liblio.models import Upload, Avatar
from liblio.helpers import decode_printable_id

from . import API_PATH

# BLUEPRINT_PATH="{api}/".format(api=API_PATH)
# Media access is top-level
BLUEPRINT_PATH="/"

blueprint = Blueprint('media', __name__, url_prefix=BLUEPRINT_PATH)

### Routes

@blueprint.route('media/<media_fid>')
def get_media(media_fid):
    """Get uploaded media by its Flake ID."""

    media = Upload.query.filter_by(flake=decode_printable_id(media_fid)).first()

    if media is not None:
        path = liblio_uploads.path(media.filename)
        return send_file(path)
    else:
        raise APIError(404, "Media not found")

@blueprint.route('avatars/<media_fid>')
def get_avatar(media_fid):
    """Get uploaded avatar by its Flake ID."""

    avatar = Avatar.query.filter_by(flake=decode_printable_id(media_fid)).first()

    if avatar is not None:
        path = liblio_uploads.path(avatar.filename)
        return send_file(path)
    else:
        raise APIError(404, "Media not found")
