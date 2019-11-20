# coding:utf8
from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
# from app.home import home as home_blueprint
# from app.admin import admin as admin_blueprint
from .config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
db.init_app(app)

# 不要在生成db之前导入注册蓝图。
from app.home import home as home_blueprint
from app.admin import admin as admin_blueprint

app.register_blueprint(home_blueprint)
app.register_blueprint(admin_blueprint, url_prefix="/admin")

@app.errorhandler(404)
def page_not_found(error):
    return render_template("home/404.html"), 404