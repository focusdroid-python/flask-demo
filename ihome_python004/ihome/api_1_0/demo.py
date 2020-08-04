#coding:utf-8

from . import api
from ihome import db, modules
import logging
from flask import current_app

@api.route("/index")
def index():
    """"""
    # logging.error('log error') # 错误级别
    # logging.warn('log error') # 警告级别
    # logging.info('log error') # 消息提示级别
    # logging.debug('log error') # 调试级别
    current_app.logger.error('flask curent_app error')
    current_app.logger.warn('flask curent_app warn')
    current_app.logger.info('flask curent_app info')
    current_app.logger.debug('flask curent_app debug')
    return "index page"