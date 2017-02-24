from flask import Blueprint

# -*- coding:utf-8 -*-
__author__ = 'jacobdong'

main = Blueprint('main', __name__)
from . import views, errors
