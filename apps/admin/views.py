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

admin = Blueprint('admin',__name__,url_prefix='/admin')

def view(html):
    return render_template('admin/' + html)

@admin.route('/')
def index():
    return view('index.html')