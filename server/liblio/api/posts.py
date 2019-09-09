### CRUD operations for posts, except probably not the U part

from flask import Blueprint, current_app, jsonify, make_response
from flask_jwt_extended import get_jwt_identity, jwt_required
from webargs import fields, validate
from webargs.flaskparser import parser

from liblio import db, jwt
from liblio.error import APIError
from liblio.models import Post, User
from liblio.helpers import decode_printable_id
from . import API_PATH

BLUEPRINT_PATH="{api}/post".format(api=API_PATH)

blueprint = Blueprint('posts', __name__, url_prefix=BLUEPRINT_PATH)

### Request schemas

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