# -*- coding:utf-8 -*-
from sqlalchemy import or_

from . import home
from flask import render_template,request,redirect, url_for,flash,jsonify
from app.models import Content
from flask_paginate import get_page_parameter, Pagination



@home.route('/ajax')
def ajax():
    page = request.args.get('page', 1, type=int)
    pagination = Content.query.paginate(page, per_page=10)
    news_list = pagination.items
    for anews in news_list:
        print(anews)
    return render_template('home/ajax_add.html', datas=news_list)




@home.route('/')
@home.route('/index')
def index():

    # 翻页
    PER_PAGE = 10
    page = request.args.get(get_page_parameter(),type=int,default=1)
    start = (page - 1) * PER_PAGE
    end = start + PER_PAGE
    total = Content.query.count()
    print("数据总量:",total)
    pagination = Pagination(page=page,start=start,end=end,total=total)
    datas = Content.query.all()
    context = {
     'datas' : datas[start:end],
     'pagination' : pagination
    }
    return render_template('home/index.html',**context)



@home.route('/archives')
def archives():
    return render_template('home/archives.html')
    
@home.route('/tags')
def tags():
    return render_template('home/tags.html')   
    
@home.route('/about')
def about():
    return render_template('home/about.html')


@home.route('/search')
def search():
    search_key = request.args.get("search", "")
    if search_key != "":
        print("搜索关键字:", search_key, type(search_key))
        res = Content.query.filter(or_(Content.title.contains(search_key),Content.content.contains(search_key))).all()
        if res:
            print("搜索数据结果:",res)
            return render_template('home/search.html',datas=res,search_key=search_key)
        else:
            return '没有搜索结果'
    else:
        print("没有关键字")
        flash("注册成功！", "ok")

    return '还请输入关键字查找啊'


@home.route('/Index<id>')
def index_id(id):
    return render_template('home/Index{}.html'.format(id))

@home.errorhandler(404)
def page_not_found(error):
    return render_template('home/404.html'), 404

