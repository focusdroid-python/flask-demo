# coding:utf-8

from flask import Blueprint, current_app

# 提供静态文件的蓝图
html = Blueprint("web_html", __name__)

# @html.route("/<re(r'.*'):html_file_name>")
@html.route("/filename")
def get_html():
    """提供html文件"""

    # falsk定义的返回静态文件的方法
    # return current_app.send_static_file(html_file_name)
    return '另外一个视图'