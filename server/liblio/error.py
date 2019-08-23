# Simple extension to Flask's error-handling
# (Mostly derived from the Flask docs)

from flask import jsonify

class APIError(Exception):
    "Helper class to generate meaningful API exceptions with proper HTTP status"

    def __init__(self, message, status_code=400, payload=None):
        Exception.__init__(self)

        self.message = message
        self.status_code = status_code
        self.payload = payload
    
    def to_dict(self):
        resp = dict(self.payload or ())
        resp['message'] = self.message
        return resp