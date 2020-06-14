# coding:utf-8

from . import api

@api.route("/users", methods=["POST"])
def register():
    """注册
        请求参数：　手机号、短信验证码、密码
        参数格式：
    """
    pass