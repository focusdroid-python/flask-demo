# coding:utf-8
from . import api
# from ihome import db, models
# import logging
from flask import current_app, make_response
from flask_wtf import csrf


@api.route('/index')
def index():
    current_app.logger.error('error msg')
    current_app.logger.warn('warn msg')
    current_app.logger.info('info msg')
    current_app.logger.debug('debug msg')
    return 'index page'

@api.route("/indexs")
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