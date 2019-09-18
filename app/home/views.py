# -*- coding:utf-8 -*-
from . import home
from flask import render_template

@home.route('/')
@home.route('/index')
def index():
    return render_template('home/index.html')

@home.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404