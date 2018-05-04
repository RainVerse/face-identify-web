from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import config
from .service.deep_id_validator import deep_id_validator

db = SQLAlchemy()

from .controller import controller

# config_name = 'development'
config_name = 'production'
app = Flask(__name__)
app.config.from_object(config[config_name])
config[config_name].init_app(app)
print(config_name + ' mode on.')
db.init_app(app)
app.register_blueprint(controller)

app_config = app.config
deep_id_validator = deep_id_validator(app_config['FILE_BASE_PATH'] + '/model/deep_id')
