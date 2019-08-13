# Entry point for the Liblio server

import os

from flask import Flask

def create_app():
    # Create the app
    app = Flask(__name__, instance_relative_config=True)

    # Development data
    app.config.from_mapping(
        SECRET_KEY='dev'
    )

    # Other config stuff goes here
    if app.env == 'production':
        app.config.from_pyfile('config.py', silent=True)

    # Create the instance folder if it doesn't exist
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Routes (we'll factor these out later)
    @app.route("/")
    def home():
        return "Hello, world!"
    
    return app