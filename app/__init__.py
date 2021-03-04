from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap

from confing import app_config

db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    
    db.init_app(app)
    Bootstrap(app)
    migrate = Migrate(app, db)


    from app import models

    from .crud_app import crud_app as crud_app_blueprint
    app.register_blueprint(crud_app_blueprint, url_prefix='/crud_app')

    return app