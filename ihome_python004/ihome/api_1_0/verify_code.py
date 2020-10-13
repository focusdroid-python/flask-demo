# -*- coding:utf-8 -*-
from . import api
from ihome.utils.captcha.captcha import captcha
from ihome.utils.response_code import RET
from ihome import redis_store, constants, db
from flask import current_app, jsonify, make_response, request
from ihome.modules import User
from ihome.libs.yuntongxun.sms import CCP
import random


@api.route("/get_image_code/<image_code_id>")
def get_image_code(image_code_id):
    """
    获取图片验证码
    :param image_code_id: 图片验证码编号
    :return:　正常：验证码图片　　异常：返回json
    """
    # 获取参数
    # 检验参数
    # 业务逻辑处理，生成验证码操作
    # 名字　真实文本　图片数据
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
        # return jsonify(errno=RET.DBERR, errmsg='save image code failed')
        return jsonify(errno=RET.DBERR, errmsg="保存图片验证码信息失败")

    # 返回图片
    resp = make_response(image_data)
    resp.headers["Content-Type"] = "image/jpg"
    return resp

    # 生成ｂａｓｅ６４编码需要使用
    #　<img src="data:image/png;base64,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">
    # from io import BytesIO
    # from captcha.image import ImageCaptcha
    # import random
    # import base64
    #
    # captcha_str = ''.join(random.choice('1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ') for i in range(4))
    # image = ImageCaptcha().generate_image(captcha_str)
    # buffer = BytesIO()
    # image.save(buffer, format='PNG')
    # data = buffer.getvalue()
    # return 'data:image/png;base64,' + base64.b64encode(data).decode()


# get /api/v1.0/sms_codes/<mobile>?image_code=xx&image_code_id=xx
@api.route("/sms_codes/<re(r'1[345789]\d{9}'):mobile>")
def get_sms_code(mobile):
    """获取短信验证码"""
    # 1. 获取参数
    image_code = request.args.get("image_code")
    image_code_id = request.args.get("image_code_id")

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

    # 与用户填写的值进行对比
    if real_image_code.lower() != image_code.lower():
        # 表示用户填写错误
        return jsonify(errno=RET.DATAERR, errmsg="图片验证码错误")

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
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmsg="保存短信验证码异常")
    # 发送短信
    result = -1
    try:
        ccp = CCP()
        result = ccp.send_template_sms(mobile, [sms_code, int(constants.SMS_CODE_REDIS_EXPIRES/60)])
    except Exception as e:
        current_app.logger.error(e)

    # 1. 返回值
    if result == 0:
        return jsonify(errno=RET.OK, errmsg="发送短信成功")
    else:
        return jsonify(errno=RET.THIRDERR, errmsg="发送短信失败")
