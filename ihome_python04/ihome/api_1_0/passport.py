# coding:utf-8

from . import api
from flask import jsonify, request, current_app, session
from ihome.utils.response_code import RET
from ihome import redis_store, db, constants
from ihome.modules import User
from sqlalchemy.exc import IntegrityError
# from werkzeug.security import generate, password_hash, check_password_hash
import re

@api.route("/users", methods=["POST"])
def register():
    """注册
        请求参数：　手机号、短信验证码、密码
        参数格式：  json

    """
    reg_dict = request.get_json()
    mobile = reg_dict.get("mobile")
    sms_code = reg_dict.get("sms_code")
    password = reg_dict.get("password")
    password2 = reg_dict.get("password2")

    # 校验参数
    if not all([mobile, sms_code, password]):
        return jsonify(error=RET.PARAMERR, errmsg="参数不完整")

    # 判断手机号格式
    if  not re.match(r"1[34578]\d{9}", mobile):
        #　表示格式不对
        return jsonify(error=RET.PARAMERR, errmsg="手机格式错误")

    # 判断两次密码不一致
    if password != password2:
        return jsonify(error=RET.PARAMERR, errmsg="两次密码不一致")

    # 从redis中取出短信验证码
    try:
        real_sms_code = redis_store.get("sms_code_%" % mobile)
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(error=RET.DBERR, errmsg="读取短信验证码异常")
    # 判断短信验证码是否过期
    if real_sms_code is None:
        return jsonify(error=RET.NODATA, errmsg="短信验证码失效")

    # 删除redis中短信验证码，防止重复使用校验
    try:
        redis_store.delete("sms_code_%s" % mobile)
    except Exception as e:
        current_app.logger.error(e)

    # 判断用户填写的短信验证码的正确性
    if real_sms_code != sms_code:
        return jsonify(error=RET.DATAERR, errmsg="短信验证码错误")

    # 判断用户的手机是否注册过
    try:
        user = User.query.filter_by(mobile=mobile).first()
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(error=RET.DBERR, errmsg="数据库异常")

    else:
        if user is not None:
            return jsonify(error=RET.DATAEXIST, errmsg="用户手机号已存在")

    # 保存用户注册的数据到数据库
    user = User(name=mobile, mobile=mobile)
    # 多密码进行处理使用modules勒种的generate_password_hash函数进行处理，并保存在数据库中
    # user.generate_password_hash(password)

    # 设置属性
    user.password = password
    try:
        db.session.add(user)
        db.session.commit()
    except IntegrityError as e:
        # 数据库操作错误的回滚
        db.session.rollback()
        # 手机号出现了重复值，手机号注册过
        current_app.logger.error(e)
        return jsonify(error=RET.DATAEXIST, errmsg="手机号已存在")
    except Exception as e:
        # 数据库操作错误的回滚
        db.session.rollback()
        current_app.logger.error(e)
        return jsonify(error=RET.DBERR, errmdg="查询数据库异常")

    # 保存登录状态到session中
    session["name"] = mobile
    session["mobile"] = mobile
    session["user_id"] = user.id
    # 返回结果
    return jsonify(error=RET.OK, errmsg="注册成功")

@api.route("/login", methods=["POST"])
def login():
    """
    用户登录
    参数：　手机号、密码
    :return:
    """
    # 获取参数
    req_dict = request.get_json()
    mobile = req_dict.get("mobile")
    password = req_dict.get("password")
    # 校验参数
    # 参数完整的校验
    if not all ([mobile, password]):
        return jsonify(error=RET.PARAMERR, errmsg="参数不完整")

    # 手机号的格式
    if not re.match(r"1[3456789]\d{9}", mobile):
        return jsonify(error=RET.PARAMERR, errmsg="手机格式错误")

    # 判断错误次数是否超过限制，如果超过限制，则返回
    # redis记录：　"access_nums_请求的ip": 次数
    user_ip = request.remote_addr # 用户的ip地址
    try:
        access_nums = redis_store.get("access_nums_%s" % user_ip)
    except Exception as e:
        current_app.logger.error(e)
    else:
        if access_nums is not None and int(access_nums) >= constants.LOGIN_ERROR_MAX_TIMES:
            return jsonify(error=RET.REQERR, errmsg="错误次数太多，请稍后再试")



    # 从数据中根据手机号查询用户的数据对象
    try:
        user = User.query.filter_by(mobile=mobile).first()
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(error=RET.DBERR, errmsg="获取用户信息失败")

    if user is None:
        return jsonify(error=RET.DATAERR, errmsg="用户名或密码错误")

    # 用数据库的密码与用户填写的密码进行对比验证
    if user is None or not user.check_password(password):
        # 验证失败，记录错误次数，返回信息
        try:
            redis_store.incr("access_nums_%s"%user_ip)
            redis_store.expire("axxess_num_%s"%user_ip, constants.LOGIN_ERROR_DORBID_TIME)
        except Exception as e:
            current_app.logger.error(e)

        return jsonify(error=RET.DATAERR, errmsg="用户名或密码错误")

    # 如果验证相同成功，保持登录状态，在session中
    session["name"] = user.name
    session["mobile"] = user.mobile
    session["user_id"] = user.id

    return jsonify(error=RET.OK, errmsg="登录成功")
    # 如果验证失败，记录错误次数，返回信息




@api.route("/session", methods=["GET"])
def check_login():
    """检查登录状态"""
    # 尝试从session中获取用户的名字
    name = session.get("name")
    # 如果session中数据name名字存在，则表示用户已登录，否则未登录
    if name is not None:
        return jsonify(error=RET.OK, errmsg="true", data={"name": name})
    else:
        return jsonify(error=RET.SESSIONERR, errmsg="false")

# 退出
@api.route("/loginout", methods=["DELETE"])
def loginput():
    """
    退出操作
    :return:
    """
    # 清楚session操作
    # csrf_token = session.get("csrf_token")
    session.clear()
    return jsonify(error=RET.OK, errmsg="OK")