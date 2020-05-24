# coding:utf-8

from flask import Blueprint, current_app, make_response, redirect, url_for
from flask_wtf import csrf

# 提供静态文件的蓝图
html = Blueprint("web_html", __name__)


@html.route("/index")
def get_index():
    # 创建一个csrf_token值

    csrf_token = csrf.generate_csrf()

    # falsk提供的返回静态文件的方法
    response = make_response(current_app.send_static_file())

    ## 设置cookie
    response.set_cookie("csrf_token", csrf_token)
    print(csrf_token)

    # return redirect(url_for('192.168.0.103:3000'))
    return 'index pages'

@html.route("/<re(r'.*'):file_name>")
def get_html(html_file_name):
    """提供html文件"""
    if not html_file_name:
        html_file_name = "index.html"

    if html_file_name:
        html_file_name = "html/" + html_file_name

    # 创建一个csrf_token值
    csrf_token = csrf.generate_csrf()





    # falsk提供的返回静态文件的方法
    response = make_response(current_app.send_static_file(html_file_name))

    ## 设置cookie
    response.set_cookie("csrf_token", csrf_token)

    return response