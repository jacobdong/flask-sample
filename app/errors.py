# -*- coding:utf-8 -*-
from flask import render_template
from . import main

__author__ = 'jacobdong'


@main.app_errorhandler(404)
def page_not_fount(e):
    return render_template('404.html'), 404


@main.app_errorhandler(500)
def s(e):
    return render_template('500.html'), 500
