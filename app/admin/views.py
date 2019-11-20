# -*- coding:utf-8 -*-
from . import admin
from flask import render_template
def view(html):
    return render_template('admin/' + html)

@admin.route('/')
def index():
    return view('index.html')