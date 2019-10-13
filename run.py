# coding:utf8
from flask import Flask,render_template
from apps.admin import admin as admin_bp
from apps.home import home as home_bp
import config
from exts import db,mail,cache
from playhouse.flask_utils import FlaskDB

import logging
import sys


def create_app():
    app = Flask(__name__.split(".")[0])
    app.config.from_object(config)
    register_blueprints(app)
    register_extensions(app)
    register_errorhandlers(app)
    configure_logger(app)
    return app

def register_blueprints(app):
    app.register_blueprint(admin_bp)
    app.register_blueprint(home_bp)

def register_extensions(app):
    FlaskDB(app,db)
    mail.init_app(app)
    cache.init_app(app)

def register_errorhandlers(app):
    def render_error(error):
        """Render error template."""
        # If a HTTPException, pull the `code` attribute; default to 500
        error_code = getattr(error, "code", 500)
        return render_template("{0}.html".format(error_code)), error_code

    for errcode in [401, 404, 500]:
        app.errorhandler(errcode)(render_error)

def configure_logger(app):
    """Configure loggers."""
    handler = logging.StreamHandler(sys.stdout)
    if not app.logger.handlers:
        app.logger.addHandler(handler)

app = create_app()
if __name__ == '__main__':  
    app.run(host='0.0.0.0')