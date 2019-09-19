### Anything tag-based, including fetching users/posts by tag

from flask import Blueprint, current_app, jsonify, make_response
from flask_jwt_extended import jwt_required, get_jwt_identity
from webargs import fields, validate
from webargs.flaskparser import use_args
from datetime import datetime

from liblio import db, jwt
from liblio.error import APIError
from liblio.models import User, Post, Tag
from . import API_PATH

BLUEPRINT_PATH="{api}/tag".format(api=API_PATH)

blueprint = Blueprint('tags', __name__, url_prefix=BLUEPRINT_PATH)

### Request schemas

request_schemas = {
    'new_tag': {
        'name': fields.Str(required=True),
        'description': fields.Str(required=False)
    }
}

### Routes

@blueprint.route('/', methods=('GET',))
def get_all_tags():
    """Get a list of all tag names known to this server."""
    tags = Tag.query.all()

    return jsonify([t.to_dict() for t in tags]), 200

@blueprint.route('', methods=('POST',))
# @jwt_required
@use_args(request_schemas['new_tag'])
def create_tag(args):
    """Add a new tag to this server."""

    # TODO: Check that the token is from an admin, or have some setting
    # that determines whether users are allowed to make new descriptive tags.

    tag = Tag(
        name=Tag.normalize_name(args['name']),
        description=args.get('description')
    )

    # TODO: Should this affect last activity?

    db.session.add(tag)
    db.session.commit()

    return jsonify(tag.to_dict()), 201, { 'Location': tag.uri() }

@blueprint.route('/<tagname>')
def get_tag(tagname):
    """Get the tag with a given name."""
    tag = Tag.query.filter_by(name=tagname).first()

    if tag is not None:
        return jsonify(tag.to_dict()), 200
    else:
        raise APIError(404, "No tag {tagname} on this server".format(tagname=tagname))
