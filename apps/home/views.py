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
import os
from exts import db,mail

home = Blueprint('home',__name__)



@home.route('/')
@home.route('/index')
def index():
    # filename = os.path.join(home.root_path, '../public','index.html')
    # print(filename)
    # with open(filename,'w') as f:
    #     f.write(str(render_template('home/index.html')))
    #     f.close()
    return render_template('home/index.html')
      

@home.route('/archives')
def archives():
    return render_template('home/archives.html')
    
@home.route('/tags')
def tags():
    return render_template('home/tags.html')   
    
@home.route('/about')
def about():
    return render_template('home/about.html')   

@home.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404
