# -*- coding:utf-8 -*-
from flask import Blueprint

home = Blueprint("home", __name__)
from app.home import views