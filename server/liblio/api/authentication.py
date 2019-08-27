### Authentication, including login, account creation, etc.

from flask import Blueprint, request, jsonify, make_response
from webargs import fields, validate
from webargs.flaskparser import use_args

from liblio import db
from liblio.error import APIError
from liblio.models import Login
from . import API_PATH

BLUEPRINT_PATH="{api}/auth".format(api=API_PATH)

blueprint = Blueprint('auth', __name__, url_prefix=BLUEPRINT_PATH)

### Request schemas

request_schemas = {
    'create_account': {
        'username': fields.Str(required=True),
        'email': fields.Email(required=True),
        'password': fields.Str(validate=validate.Length(min=6))
    }
}

### Routes

@blueprint.route('/create-account', methods=('POST',))
@use_args(request_schemas['create_account'])
def create_account(args):
    "Create a new account on this server."
    if request.method == 'POST':

        # TODO: Check for a user who is already logged in
        
        username = args['username']
        email = args['email']
        password = args['password']

        user = Login.query.filter_by(username=username).first()
        if user is not None:
            raise APIError(message="Username already exists on this server")

        em = Login.query.filter_by(email=email).first()
        if em is not None:
            raise APIError(message="A user with this email address already exists on this server")

        login = Login(username=username, email=email)
        login.set_password(password)

        # Add to the DB
        db.session.add(login)
        db.session.commit()

        return make_response(jsonify({'username': username}), 201)

@blueprint.route('/create-account', methods=('GET',))
def create_account_get():
    "This endpoint does not support GET, so send a formatted response."
    raise APIError(405, "POST to this endpoint to create an account")