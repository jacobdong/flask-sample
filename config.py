# -*- coding:utf-8 -*-
import os

__author__ = 'jacobdong'

basedir = os.path.abspath(os.path.dirname(__name__))


class Config(object):
    APP_NAME = "flask_sample"
    APP_ENV = "default"

    @staticmethod
    def init_app(app):
        app.setting = {

        }


class DevConfig(Config):
    APP_ENV = "dev"


class DockerConfig(Config):
    APP_ENV = "docker"


class LocalConfig(Config):
    APP_ENV = "local"


config = {
    'dev'    : DevConfig,
    'docker' : DevConfig,
    'local'  : LocalConfig,
    'default': LocalConfig
}
