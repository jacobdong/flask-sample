# -*- coding:utf-8 -*-
from app import create_app

__author__ = 'jacobdong'

if __name__ == '__main__':
    app = create_app('default')
    app.debug = True
    app.run()
