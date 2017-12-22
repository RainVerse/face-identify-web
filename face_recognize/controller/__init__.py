from flask import Blueprint

controller = Blueprint('controller', __name__)
from . import admin_controller, index_controller, deep_id_controller
