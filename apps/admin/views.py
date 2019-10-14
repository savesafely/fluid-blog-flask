# -*- coding:utf-8 -*-
from flask import (
    Blueprint,
    views,
    render_template,
    request,
    session,
    redirect,
    url_for,
    g,
    jsonify
)
from exts import db,mail
import config

admin = Blueprint('admin',__name__,template_folder=config.TEMPLATE+'/admin',url_prefix='/admin')

#@admin.route('/')
@admin.route('/index/')
def index():
    print(config.TEMPLATE+'/admin')
    return render_template('index.html')

@admin.route('/editor/')
def editor():
    return render_template('editor.html')