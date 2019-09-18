# -*- coding:utf-8 -*-
from . import home
from flask import render_template


def view(html):
    return render_template('home/' + html)

@home.route('/')
def index():
    return view('index.html')
