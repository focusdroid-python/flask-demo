# -*- coding:utf-8 -*-
from . import api
from ihome.utils.captcha.captcha import captcha
from ihome.utils.response_code import RET
from ihome import redis_store, constants, db
from flask import current_app, jsonify, make_response, request
from ihome.modules import User
from ihome.yuntongxun.sms import CCP
from flask_wtf import csrf
import random


@api.route("/get_image_code")
def get_image_code():
    """
    获取图片验证码
    :param image_code_id: 图片验证码编号
    :return:　正常：验证码图片　　异常：返回json
    """

    #　创建一个csrf值
    csrf_token = csrf.generate_csrf()

    # 获取参数
    # 检验参数
    # 业务逻辑处理，生成验证码操作
    # 名字　真实文本　图片数据

    image_code_id = request.args.get("image_code_id")
    name, text, image_data = captcha.generate_captcha()
    # 将验证码真实值与编号存到redis中
    # 单条维护记录，选用字符串
    # image_codes_编号１: "真实值"
    # image_codes_编号２: "真实值"
    # redis_store.set("image_code_%s" % image_code_id, text)
    # redis_store.expire("image_code_%s" % image_code_id, constants.IMAGE_CODE_REDIS_EXPIRES)
    try:
        redis_store.setex("image_code_%s" % image_code_id, constants.IMAGE_CODE_REDIS_EXPIRES, text)
    except Exception as e:
        # 记录日志
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmsg="保存图片验证码信息失败")

    # 返回图片
    resp = make_response(image_data)

    resp.headers["Content-Type"] = "image/jpg"

    # 使用 make_response　设置 ｃｏｏｋｉｅ值
    resp.set_cookie("csrf_token", csrf_token)
    return resp


# get /api/v1.0/sms_codes/<mobile>?image_code=xx&image_code_id=xx
# @api.route("/sms_codes/<re(r'1[345789]\d{9}'):mobile>")
@api.route("/sms_codes")
def get_sms_code():
    """获取短信验证码"""
    # 1. 获取参数
    image_code = request.args.get("image_code")
    image_code_id = request.args.get("image_code_id")
    mobile = request.args.get("mobile")

    # 1. 校验参数
    if not all([image_code, image_code_id]):
        # 表示参数不完整
        return jsonify(errno=RET.PARAMERR, errmsg="参数不完整")

    # 1. 业务逻辑处理
    # 从redis中取出真实的验证码
    try:
        real_image_code = redis_store.get("image_code_%s" % image_code_id)
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmsg="redis数据库异常")

    # 判断图片验证码是否过期
    if real_image_code is None:
        # 表示验证码已经过期了
        return jsonify(errno=RET.NODATA, errmsg="图片验证码失效")

    # 删除redis中图片验证码，防止用户使用同一个图片验证码验证多次
    try:
        redis_store.delete("image_code_%s" % image_code_id)
    except Exception as e:
        current_app.logger.error(e)

    # 与用户填写的值进行对比
    if real_image_code.lower() != image_code.lower():
        # 表示用户填写错误
        return jsonify(errno=RET.DATAERR, errmsg="图片验证码错误")




    # 判断对于手机号的操作，在60秒内有没有记录，如果有则认为用户操作频繁，不接受处理
    try:
        send_flag = redis_store.get("send_sms_code_%s" % mobile)
    except Exception as e:
        current_app.logger.error(e)
    else:
        if send_flag is not None:
            # 表示在60内有发送记录
            return jsonify(errno=RET.REQERR, errmsg="请求过于频繁，请６０秒以后再试")

    # 判断手机号时都存在
    # db.session(User)
    try:
        user = User.query.filter_by(mobile=mobile).first()
    except Exception as e:
        current_app.logger.error(e)
    else:
        if user is not None:
            # 表示手机号已经存在
            return jsonify(errno=RET.DATAEXIST, errmsg="手机号已存在")

    # 如果手机号不存在，则生成短信验证码
    sms_code = "%06d" % random.randint(0, 999999)

    # 保存真实的短信验证码
    try:
        redis_store.setex("sms_code_%s" % mobile, constants.SMS_CODE_REDIS_EXPIRES, sms_code)
        # 保存发送给这个手机号的记录，防止用户在６０ｓ内重复发送短信的操作
        redis_store.setex("send_sms_code_%s" % mobile, constants.SEND_SMS_CODE_INTERVAL, 1)
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmsg="保存短信验证码异常")
    # 发送短信
    try:
        ccp = CCP()
        result = ccp.send_template_sms(mobile, [sms_code, int(constants.SMS_CODE_REDIS_EXPIRES/60)], 1)
    except Exception as e:
        current_app.logger.error(e)

    # 1. 返回值
    print('*' * 50)
    print(result)
    if result == 0:
        return jsonify(errno=RET.OK, errmsg="发送短信成功")
    else:
        return jsonify(errno=RET.THIRDERR, errmsg="发送短信失败")
