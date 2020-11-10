# -*- coding:utf-8 -*-
from werkzeug.routing import BaseConverter
from flask import session, jsonify
from ihome.utils.response_code import RET
# 定义正则装换器

class ReConverter(BaseConverter):
    """

    """
    def __init__(self, url_map, regex):
        # 调用父类的初始化方法
        super(ReConverter, self).__init__(url_map)
        # 保存
        self.regex = regex


# 定义登录验证器的装饰器验证器
def loggin_required(view_func):
    def wrapper(*args, **kwargs):
        # 判断用户的登录状态
        user_id = session.get("user_id")
        # 如果用户是登陆的,执行视图函数
        if user_id is not None:
            view_func(*args, **kwargs)
        else:
            # 如果未登录,返回登录信息
            return jsonify(errno=)
        #

    return wrapper


@loggin_required
def set_user_avatar():
    return json ""