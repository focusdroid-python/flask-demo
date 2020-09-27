# -*- coding:utf-8 -*-
from . import api
from ihome.utils.captcha.captcha import captcha
from ihome.utils.response_code import RET
from ihome import redis_store, constants
from flask import current_app, jsonify, make_response

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