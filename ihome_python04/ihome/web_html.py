# coding:utf-8

from flask import Blueprint

# 提供静态文件的蓝图
html = Blueprint("web_html", __name__)

@html.route("/<file_name>")
def get_html():
    """提供html文件"""
    pass