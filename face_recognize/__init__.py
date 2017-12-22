from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import config

db = SQLAlchemy()

from .controller import controller

config_name = 'development'
app = Flask(__name__)
app.config.from_object(config[config_name])
config[config_name].init_app(app)
print(config_name + ' mode on.')
db.init_app(app)
app.register_blueprint(controller)

app_config = app.config
