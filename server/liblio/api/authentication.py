### Authentication, including login, account creation, etc.

from datetime import datetime

from flask import Blueprint, request, jsonify, make_response
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from webargs import fields, validate
from webargs.flaskparser import use_args

from liblio import db, jwt
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
    },

    'login': {
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

@blueprint.route('/login', methods=("POST",))
@use_args(request_schemas['login'])
def login(args):
    "Login to this server, receiving an authentication token in response."

    username = args['username']
    password = args['password']

    login = Login.query.filter_by(username=username).first()
    if login is None or not login.check_password(password):
        # Best security practice is to avoid telling a user whether
        # the username or password is incorrect.
        raise APIError(401, "Invalid username or password")
    
    login.last_login = datetime.now()
    login.last_action = datetime.now()
    db.session.add(login)
    db.session.commit()

    token = create_access_token(username)
    return make_response(jsonify(access_token=token), 200)

@blueprint.route('/logout', methods=('POST',))
@jwt_required
def logout():
    ### TODO: Token revocation, blacklist, or whatever
    username = get_jwt_identity()
    return make_response(jsonify(logout=username), 200)