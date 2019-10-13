#encoding: utf-8
from playhouse.db_url import connect
from flask_mail import Mail
from config import DATABASE
from flask_caching import Cache

db = connect(DATABASE)
mail = Mail()
cache = Cache()

