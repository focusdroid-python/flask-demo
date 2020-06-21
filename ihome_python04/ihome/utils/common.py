# coding:utf-8

from werkzeug.routing import BaseConverter
from flask import session, jsonify, g
from ihome.utils.response_code import RET
import functools

# 定义一个正则转换器
class ReConverter(BaseConverter):
    """"""
    def __init__(self, url_map, regex):
        '''调用父类方法'''
        super(ReConverter, self).__init__(url_map)
        # 保存正则表达式
        self.regex = regex

# 登录装饰器
def login_required(view_func):

    @functools.wraps(view_func) # python自定义的装饰器，接受外层函数的参数,不改变参数指向
    def wrapper(*args, **kwargs):
        # 判断用户的登录状态
        user_id = session.get("user_id")
        # 如果用户是登陆的，执行视图函数，
        if session is not None:
            # 讲user_id保存在g对象中，在试图函数中可以通过g对象获取保存数据
            g.user_id = user_id
            return view_func(*args, **kwargs)
        else:
            # 如果未登录，返回未登陆的信息
            return jsonify(error=RET.SESSIONERR, errmsg="用户未登陆")
        
    return wrapper


@login_required
def set_user_avatar():
    user_id = g.user_id
    pass