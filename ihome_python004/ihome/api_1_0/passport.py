# -*- coding:utf-8 -*-
from . import api
from flask import request, current_app, jsonify
from ihome.utils.response_code import RET
from ihome import redis_store
from ihome.modules import User
import re


@api.route("/register", methods=["POST"])
def register():
    """
    注册
    参数params： 手机号　验证码　短信验证码　密码
    参数格式
    :return:
    """
    req_dict = request.get_json()
    mobile = req_dict.get("mobile")
    sms_code = req_dict.get("sms_code")
    password = req_dict.get("password")
    confirmPassword = req_dict.get("confirmPassword")

    # 校验参数
    if not all([mobile, sms_code, password]):
        return jsonify(errno=RET.PARAERR, errmsg="参数不完整")

    # 判断手机号格式
    if not re.match(r"1[3456789]\d{9}", mobile):
        return jsonify(errno=RET.PARAERR, errmsg="手机号格式错误")

    # 判断两次密码是否输入一致
    if password != confirmPassword:
        return jsonify(errno=RET.PARAERR, errmsg="两次密码输入不一致")

    # 从redis取出短信验证码
    try:
        real_sms_code = redis_store.get("sms_code_%s" % mobile)
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmsg="读取短信验证码异常")

    # 判断短信验证码是否过期
    if real_sms_code is None:
        return jsonify(errno=RET.NODATA, errmsg="读取短信验证码异常")

    # 删除redis中的短信验证码，防止重复使用校验
    try:
        redis_store.delete("sms_code_%s" % mobile)
    except Exception as e:
        current_app.logger.error(e)

    # 判断用户填写短信验证码的正确性
    if real_sms_code != sms_code:
        return jsonify(errno=RET.DBERR, errmsg="短信验证码错误")

    # 判断用户手机号是否被注册过
    try:
        user = User.query.filter_by(mobile=mobile).first()
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmsg="数据库异常")
    else:
        if user is not None:
            # 表示手机号已经存在
            return jsonify(errno=RET.DATAEXIST, errmsg="手机号已存在")

    # 保护用户的注册数据提交到数据库中

    # 并保存登录状态在session中
















