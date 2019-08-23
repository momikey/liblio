# Entry point for the Liblio server

import os

from flask import Flask, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_executor import Executor

from werkzeug.exceptions import HTTPException

from .error import APIError

# Define extensions here, so we can access them easily
from .models import db
cors = CORS()
migrate = Migrate()
executor = Executor()

def create_app():
    """
    Create the Liblio server object as a Flask application.
    """

    # Create the app
    app = Flask(__name__, instance_relative_config=True)

    # CORS (maybe make this per-route or something later on)
    cors.init_app(app)

    # Development data
    app.config.from_mapping(
        SECRET_KEY='dev'
    )

    # Other config stuff goes here
    app.config.from_pyfile('config.py', silent=True)

    # Different configurations for production and development modes
    if app.env == 'production':
        app.config.from_pyfile('prod.py', silent=True)
    else:
        app.config.from_pyfile('dev.py', silent=True)

    # Create the instance folder if it doesn't exist
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    # Database and migrations
    # from .models import db
    db.init_app(app)
    migrate.init_app(app, db)

    # Executor for futures
    executor.init_app(app)

    # Blueprints for API
    from .api import authentication
    app.register_blueprint(authentication.blueprint)

    # Register our custom error handler
    @app.errorhandler(APIError)
    def handle_api_error(error):
        response = jsonify(error.to_dict())
        return response, error.status_code

    # Convert webargs errors to API
    @app.errorhandler(422)
    @app.errorhandler(400)
    def convert_api_error(error):
        headers = error.data.get('headers', None)
        messages = error.data.get('messages', ["Invalid request"])

        return handle_api_error(APIError(error.code, "Validation failure", payload={"errors": messages}))

    # Routes (we'll factor these out later)
    @app.route("/hello")
    def home():
        return "Hello, world!"

    # Testing route to show all routes
    @app.route("/routes")
    def routes():
        return jsonify(repr(app.url_map))
    
    return app