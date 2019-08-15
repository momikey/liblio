# Entry point for the Liblio server

import os

from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

def create_app():
    # Create the app
    app = Flask(__name__, instance_relative_config=True)

    # CORS (maybe make this per-route or something later on)
    CORS(app)

    # Development data
    app.config.from_mapping(
        SECRET_KEY='dev'
    )

    # Other config stuff goes here
    app.config.from_pyfile('config.py', silent=True)

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
    db = SQLAlchemy(app)
    migrate = Migrate(app, db)

    # Routes (we'll factor these out later)
    @app.route("/")
    def home():
        return "Hello, world!"
    
    return app