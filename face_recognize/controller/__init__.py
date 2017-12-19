from flask import Blueprint

controller = Blueprint('controller', __name__)
from . import admin_controller, update_controller, index_controller
