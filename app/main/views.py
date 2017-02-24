# -*- coding:utf-8 -*-
from . import main

__author__ = 'jacobdong'


@main.route("/", methods=['GET'])
def index():
    return "hello world"
