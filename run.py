# coding:utf8
from flask import Flask
from apps.admin import admin as admin_bp
from apps.home import home as home_bp
import config
from exts import db,mail

def create_app():
    app = Flask(__name__)
    app.config.from_object(config)
    app.register_blueprint(admin_bp)
    app.register_blueprint(home_bp)

    db.init_app(app)
    mail.init_app(app)
    return app
app = create_app()
if __name__ == '__main__':  
    app.run(host='0.0.0.0')