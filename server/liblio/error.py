# Simple extension to Flask's error-handling
# (Mostly derived from the Flask docs)

from http import HTTPStatus

from flask import jsonify

class APIError(Exception):
    "Helper class to generate meaningful API exceptions with proper HTTP status"

    def __init__(self, status_code=400, message=None, payload=None):
        Exception.__init__(self)

        self.status_code = HTTPStatus(status_code)
        self.message = message or self.status_code.description
        self.payload = payload
    
    def to_dict(self):
        resp = dict(self.payload or ())
        resp['status'] = self.status_code
        resp['message'] = self.message
        return resp