from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import sqlite3 as sql

from config import app_config

db = SQLAlchemy()

def create_app(config_name):
	# bare app
    app = Flask(__name__)
    

    # Load configuration
    app.config.from_object(app_config[config_name])
    db.init_app(app)

    # flask migration plugin
    migrate = Migrate(app, db)

    from app import models

    from .maps import maps as maps_blueprint
    app.register_blueprint(maps_blueprint)
    
    return app