# -*- coding:utf-8 -*-
from config import config
from flask import Flask

__author__ = 'jacobdong'


def create_app(config_name):
    print u"创建APP-{0}".format(__name__)
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    from .main import main as main_blueprint
    # app.register_blueprint(main_blueprint)
    app.register_blueprint(main_blueprint)
    # etc
    return app
