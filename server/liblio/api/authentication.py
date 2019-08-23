### Authentication, including login, account creation, etc.

from flask import Blueprint, request, jsonify, abort
from werkzeug.security import check_password_hash, generate_password_hash
from werkzeug.exceptions import MethodNotAllowed

from liblio import db
from liblio.error import APIError
from . import API_PATH

BLUEPRINT_PATH="{api}/auth".format(api=API_PATH)

blueprint = Blueprint('auth', __name__, url_prefix=BLUEPRINT_PATH)

@blueprint.route('/create-account', methods=('GET', 'POST'))
def create_account():
    if request.method == 'POST':
        acct = request.get_json()

        username = acct.username
        password = acct.password

        if not username:
            abort(400)
        if not password:
            abort(400)

    else:
        #raise APIError("POST to this endpoint to create an account", 405)
        raise MethodNotAllowed(['POST'])