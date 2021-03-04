from flask import Blueprint

crud_app = Blueprint('crud_app', __name__)

from . import views