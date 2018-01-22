from flask import Blueprint

maps = Blueprint('maps_main', __name__)

from . import views