import os

DEBUG = True

#数据库连接
SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False


#分页设置
PER_PAGE = 10

#SERVER_NAME = ''

DEFAULT_THEME = 'default'



APP_ROOT = os.path.dirname(os.path.abspath(__file__))   
STATIC = os.path.join(APP_ROOT, 'static')
TEMPLATE = os.path.join(APP_ROOT, 'templates')
PUBLIC = os.path.join(APP_ROOT, 'public')
