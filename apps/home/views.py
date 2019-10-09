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
from .models import (
    BlogModel
)
import os
import config
from exts import db, mail
from flask_paginate import Pagination, get_page_parameter
import config

home = Blueprint('home', __name__,template_folder=config.TEMPLATE+'/'+config.DEFAULT_THEME+'/home')

@home.route('/')
@home.route('/index')
def index():
    # filename = os.path.join(home.root_path, '../public','index.html')
    # print(filename)
    # with open(filename,'w') as f:
    #     f.write(str(render_template('home/index.html')))
    #     f.close()
    page = request.args.get(get_page_parameter(),type=int,default=1)
    start = (page - 1) * config.PER_PAGE
    end = start + config.PER_PAGE
    total = BlogModel.query.filter().count()
    # print(total)
    pagination = Pagination(page=page,start=start,end=end,total=total)
    blogs = BlogModel.query.slice(start,end)
    # db.create_all()
    # data = BlogModel('你好','Juukee')
    # db.session.add(data)
    # db.session.commit()
    context = {
     'blogs' : blogs,
     'pagination' : pagination

    }
    return render_template('index.html',**context)


@home.route('/archives')
def archives():
    return render_template('archives.html')


@home.route('/tags')
def tags():
    return render_template('tags.html')


@home.route('/about')
def about():
    return render_template('about.html')


@home.app_errorhandler(404)
def page_not_found(e):
    return render_template('404.html',), 404
