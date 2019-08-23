### Authentication, including login, account creation, etc.

from flask import Blueprint, request, jsonify, abort
from webargs import fields, validate
from webargs.flaskparser import use_args
from werkzeug.security import check_password_hash, generate_password_hash

from liblio import db
from liblio.error import APIError
from . import API_PATH

BLUEPRINT_PATH="{api}/auth".format(api=API_PATH)

blueprint = Blueprint('auth', __name__, url_prefix=BLUEPRINT_PATH)

### Request schemas

request_schemas = {
    'create_account': {
        'username': fields.Str(required=True),
        'password': fields.Str(validate=validate.Length(min=6))
    }
}

### Routes

@blueprint.route('/create-account', methods=('POST',))
@use_args(request_schemas['create_account'])
def create_account(args):
    "Create a new account on this server."
    if request.method == 'POST':
        username = args['username']
        password = args['password']

        return jsonify({'username': username, 'hash': generate_password_hash(password)}), 201

@blueprint.route('/create-account', methods=('GET',))
def create_account_get():
    "This endpoint does not support GET, so send a formatted response."
    raise APIError(405, "POST to this endpoint to create an account")