# Admin-only actions, including raw post data, account editing, etc.

from flask import Blueprint, current_app, jsonify, request
from flask_jwt_extended import get_jwt_identity, jwt_required
from webargs import fields, validate
from webargs.flaskparser import use_args
from datetime import datetime

from liblio import db, jwt
from liblio.error import APIError
from liblio.models import Post, User, Login, Tag, Role
from liblio.helpers import decode_printable_id
from . import API_PATH

BLUEPRINT_PATH="{api}/admin".format(api=API_PATH)

blueprint = Blueprint('admin', __name__, url_prefix=BLUEPRINT_PATH)

### Helpers

def login_to_dict(login):
    """Creates a Python dict for a Login database entity.

    This is not a method of the Login model because it is not normally needed
    by the Liblio server. It's admin-only, so it can be considered private to
    this controller.

    Note: This does expose user email addresses, so use with care. Passwords
    are not returned, but they're stored as hashes anyway.
    """
    return dict(
        id=login.id,
        username=login.username,
        email=login.email,
        last_login=login.last_login,
        last_action=login.last_action,
        role=login.role.name,
        userdata=login.user.to_dict()
    )

def error_on_unauthorized():
    """Raises appropriate API errors on bad usernames and for users
    who are not administrators. This is a common authentication check
    for essentially every admin route.
    """

    username = get_jwt_identity()
    user = Login.query.filter_by(username=username).first()

    if user is None:
        raise APIError(400, "User {username} does not exist on this server".format(username=username))
    elif user.role is not Role.admin:
        raise APIError(401, "Only administrators have access to this page")


### Routes

@blueprint.route('/accounts', methods=('GET',))
@jwt_required
def get_accounts():
    """Retrieve accounts on this server. Can use the following query parameters:

    * max: The maximum number of records to return
    * page: The "page" of records
    """

    error_on_unauthorized()

    accounts = Login.query.order_by(Login.id)
    total_num = accounts.count()

    try:
        count = int(request.args.get('max', total_num))
        page = int(request.args.get('page', 1))

        if count <= 0 or page <= 0:
            raise APIError(422, "Query parameters out of range")

        begin = (page - 1) * count
        end = min(begin + count, total_num)
        
        return jsonify([login_to_dict(l) for l in accounts.all()[begin:end]]), 200
    except ValueError:
        raise APIError(422, "Invalid query parameter")

@blueprint.route('/users', methods=('GET',))
@jwt_required
def get_users():
    """Retrieve users known to this server, whether local or foreign. Can use the
    following query parameters:

    * max: The maximum number of records to return
    * page: The "page" of records
    * origin: If specified, only those users with this origin will be returned
    """

    error_on_unauthorized()

    users = User.query.order_by(User.id)
    total_num = users.count()

    try:
        count = int(request.args.get('max', total_num))
        page = int(request.args.get('page', 1))
        origin = request.args.get('origin', None)

        if count <= 0 or page <= 0:
            raise APIError(422, "Query parameters out of range")

        if origin is not None:
            users = users.filter_by(origin=origin)

        begin = (page - 1) * count
        end = min(begin + count, total_num)
        
        return jsonify([u.to_dict() for u in users.all()[begin:end]]), 200
    except ValueError:
        raise APIError(422, "Invalid query parameter")

@blueprint.route('/posts', methods=('GET',))
@jwt_required
def get_posts():
    """Retrieve posts known to this server. This can be filtered by origin, and
    takes the following query parameters:


    * max: The maximum number of records to return
    * page: The "page" of records
    * origin: If specified, only those users with this origin will be returned
    """

    error_on_unauthorized()
    
    posts = Post.query.order_by(Post.id)
    total_num = posts.count()

    try:
        count = int(request.args.get('max', total_num))
        page = int(request.args.get('page', 1))
        origin = request.args.get('origin', None)

        if count <= 0 or page <= 0:
            raise APIError(422, "Query parameters out of range")

        if origin is not None:
            posts = posts.filter(User.origin == origin)

        begin = (page - 1) * count
        end = min(begin + count, total_num)
        
        return jsonify(total=total_num, posts=[p.to_dict() for p in posts.all()[begin:end]]), 200
    except ValueError:
        raise APIError(422, "Invalid query parameter")

@blueprint.route('/tags', methods=('GET',))
@jwt_required
def get_tags():
    """Retrieves all tags known to this server. Can use the following query
    parameters:

    * max: The maximum number of records to return
    * page: The "page" of records
    """

    error_on_unauthorized()

    tags = Tag.query.order_by(Tag.id)
    total_num = tags.count()

    try:
        count = int(request.args.get('max', total_num))
        page = int(request.args.get('page', 1))

        if count <= 0 or page <= 0:
            raise APIError(422, "Query parameters out of range")

        begin = (page - 1) * count
        end = min(begin + count, total_num)
        
        return jsonify([t.to_dict() for t in tags.all()[begin:end]]), 200
    except ValueError:
        raise APIError(422, "Invalid query parameter")