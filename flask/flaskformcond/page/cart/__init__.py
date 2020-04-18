# coding:utf-8

from flask import Blueprint

# 创建蓝图
app_cart = Blueprint('app_cart', __name__, template_folder='template')

# 在__init__.py文件被执行的时候，把视图加载进来，让蓝图与应用程序知道有视图的存在
from .view import get_carts