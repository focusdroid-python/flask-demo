# -*- coding:utf-8 -*-
from . import api
from flask import request, current_app, jsonify, session, make_response
from ihome.utils.response_code import RET
from ihome import redis_store, db, constants
from ihome.modules import User
from sqlalchemy.exc import IntegrityError
import re
import json
from flask_wtf import csrf

@api.route("/get_csrf_token")
def get_csrf_token():
    """
    获取csrf_token
    :return:
    """
    # 　创建一个csrf值
    csrf_token = csrf.generate_csrf()
    # 使用 make_response　设置 ｃｏｏｋｉｅ值
    resp = make_response(csrf_token)
    resp.set_cookie("csrf_token", csrf_token)
    return resp

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
    password2 = req_dict.get("password2")

    # 校验参数
    if not all([mobile, sms_code, password]):
        return jsonify(errno=RET.PARAERR, errmsg="参数不完整")

    # 判断手机号格式
    if not re.match(r"1[3456789]\d{9}", mobile):
        return jsonify(errno=RET.PARAERR, errmsg="手机号格式错误")

    # 判断两次密码是否输入一致
    if password != password2:
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
    # try:
    #     user = User.query.filter_by(mobile=mobile).first()
    # except Exception as e:
    #     current_app.logger.error(e)
    #     return jsonify(errno=RET.DBERR, errmsg="数据库异常")
    # else:
    #     if user is not None:
    #         # 表示手机号已经存在
    #         return jsonify(errno=RET.DATAEXIST, errmsg="手机号已存在")

    # 保护用户的注册数据提交到数据库中
    user = User(name=mobile, password=password, mobile=mobile)
    # user.generate_password_hash(password)
    # user.password = password

    try:
        db.session.add(user)
        db.session.commit()
    except IntegrityError as e:
        # IntegrityError 捕获具体的
        # 表示手机号出现重复值，即手机号已经被注册过
        # 操作错误的回滚，回滚上一次提交的状态
        db.session.rollback()
        current_app.logger.error(e)
        return jsonify(errno=RET.DATAEXIST, errmsg="手机号已存在")
    except Exception as e:
        # 操作错误的回滚，回滚上一次提交的状态
        db.session.rollback()
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmsg="查询数据库异常")

    # 并保存登录状态在session中
    session["name"] = mobile
    session["mobile"] = mobile
    session["user_id"] = user.id
    # 返回结果
    return jsonify(errno=RET.OK, errmsg="注册成功")


@api.route("/login", methods=["POST"])
def login():
    """
    用户登录
    参数　手机号　　密码
    格式　json
    :return:
    """
    # 获取参数
    req_dict = request.get_json()
    mobile = req_dict.get("mobile")
    password = req_dict.get("password")
    # 检验参数
    # 参数完整性
    if not all ([mobile, password]):
        return jsonify(errno=RET.PARAMERR, errmsg="参数不完整")
    # 手机号格式
    if not re.match(r"1[3456789]\d{9}", mobile):
        return jsonify(errno=RET.PARAMERR, errmsg="手机号码格式错误")

    # 超过一定时间禁止继续登录
    # redis: acess_nums_请求ＩＰ
    user_ip = request.remote_addr # 用户ip
    try:
        print("开始查询access_num")
        access_nums = redis_store.get("access_num_%s" % user_ip)
        print(redis_store.get("access_num_%" % user_ip))
    except Exception as e:
        current_app.logger.error(e)
    else:
        if access_nums is not None and int(access_nums) >= constants.LOGIN_ERROR_MAX_TIMES:
            return jsonify(error=RET.REQERR, errmsg="错误次数太多，请稍后再试")
    # 从数据库中根据手机号查询用户的数据对象
    user = None
    try:
        current_app.logger.info("开始登录查询用户信息")
        print("--------------登录查看用户信息----------")
        user = User.query.filter_by(mobile=mobile).first()
        print("-------------------"+user.name+"----------------------")
    except Exception as e:
        current_app.logger.error(e);
        return jsonify(error=RET.DBERR, errmsg="用户名或密码错误")

    # 用数据库的密码与用户填写的密码进行对比验证
    if user is None or not user.check_password(password):
        # 如果验证失败，记录错误次数，返回信息
        try:
            redis_store.incr("access_num_%" % user_ip)
            redis_store.expire("access_num_%" % user_ip, constants.LOGIN_ERROR_DORBID_TIME)
        except Exception as e:
            current_app.logger.error(e)
            return jsonify(error=RET.DATAERR, errmsg="用户名或密码错误")

    print(user.name)
    # 如果验证相同，成功保存登录状态，在session中
    session["name"] = user.name
    session["mobile"] = user.mobile
    session["user_id"] = user.mobile
    session["user_ip"] = user_ip
    #　如果验证失败，记录错误次数，返回信息
    data = {
        "success":"true",
        "code":"200",
        "user":user.name,
        "mobile":user.mobile,
        "ip": user_ip
    }
    resp = {"errno": RET.OK, "errmsg": "登陆成功", "data": data}
    resp = jsonify(resp)
    resp.headers['Access-Control-Allow-Headers'] = "content-type"
    resp.headers['Access-Control-Allow-Origin'] = '*'


    return resp
    #


@api.route("/session", methods=["GET"])
def check_login():
    """检查用户登录状态"""
    # 案例写明使用name,但我认为必须使用mobile
    name = session.get("name")
    #  如果名字存在session中,则表示用户已经登录,否则就是未登陆
    if name is not None:
        return jsonify(errmno=RET.OK, ERRMSG=True, data={"name":name})
    else:
        return jsonify(errmno=RET.SESSIONERR, ERRMSG=False)


@api.route("/login", methods=["POST"])
def logout():
    """登出"""
    # 清除session操作
    session.clear()
    return jsonify(errno=RET.OK, errmsg="OK")















