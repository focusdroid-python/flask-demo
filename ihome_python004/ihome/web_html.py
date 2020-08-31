# coding:utf-8

from flask import Blueprint, current_app

# 提供静态文件的蓝图
html = Blueprint("web_html", __name__)

# @html.route("/<re(r'.*'):html_file_name>")
@html.route("/<re(r'.*'):filename>")
def get_html(html_file_name):
    """提供html文件"""

    # falsk定义的返回静态文件的方法
    # return current_app.send_static_file(html_file_name)
    if not html_file_name:
        html_file_name = 'index.html'

    if html_file_name:
        html_file_name = "html/" + html_file_name

    # flask提供的返回静态文件的方法
    return current_app.send_static_file(html_file_name)