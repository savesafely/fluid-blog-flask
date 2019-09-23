# coding:utf8
from flask import Flask
from app.home import home as home_blueprint
from app.admin import admin as admin_blueprint
from . import config

app = Flask(__name__)
app.config.from_object(config)
app.register_blueprint(home_blueprint)
app.register_blueprint(admin_blueprint, url_prefix="/admin")