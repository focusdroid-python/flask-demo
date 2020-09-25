# -*- coding:utf-8 -*-
from . import api
from ihome import modules, db
import logging
from flask import current_app, make_response
from flask_wtf import csrf

@api.route("/index")
def index():
    current_app.logger.error("error manager")
    current_app.logger.warn("warn manager")
    current_app.logger.info("info manager")
    current_app.logger.debug("debug manager")

    # # 创建一个csrf_token值
    # csrf_token = csrf.generate_csrf()
    #
    # # falsk提供的返回静态文件的方法
    # resp = make_response()
    #
    # # 设置cookie
    # resp.set_cookie("csrf_token", csrf_token)

    return 'index pages'