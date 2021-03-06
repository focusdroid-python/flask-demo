# coding:utf-8

from . import api
from ihome.utils.captcha.captcha import captcha
from ihome import redis_store
from ihome import constants
from flask import current_app, jsonify, make_response, request
from ihome.utils.response_code import RET
# from ihome.libs.yuntongxun.sms import CCP # 引入这个提示没有这个包
from ihome.modules import User
import random
# from ihome.tasks.task_sms import send_sms
from ihome.tasks.sms.tasks import send_sms  # 封装置后的celery

# GET 127.0.0.1/api/v1.0/image_code/<image_code_id>

@api.route("/image_code/<image_code_id>")
def get_image_code(image_code_id):
    """
    获取图片验证码
    :params image_code_id: 验证码图片
    """
    # 获取参数
    # 检验参数
    # 业务处理
    # 生成验证码图片
    name, text, image_data = captcha.generate_captcha()
    # 将验证码真实值与编号保存到redis中, 设置有效期
    #　redis: 字符串，　列表，　哈希　set
    #　"key"：xx
    # "image_data": {"":"","":""} 哈希　hset("image_codes", "id1", "abc")
    # redis_store.set("image_code_%s" % image_code_id, text)
    # redis_store.expire("image_code_%s" % image_code_id, constants.IMAGE_CODE_REDIS_EXPIRES)
    #                     记录名字                          有效期                           记录值
    try:
        redis_store.setex("image_code_%s" % image_code_id, constants.IMAGE_CODE_REDIS_EXPIRES, text)
    except Exception as e:
        # 记录日志
        current_app.logger.error(e)
        # return jsonify(errno=RET.DBERR, errmsg="save image code id failed")
        return jsonify(errno=RET.DBERR, errmsg="保存图片验证码失败")

    # 返回数据
    resp = make_response(image_data)
    resp.headers["Content-Type"] = "image/jpg"
    return resp


# get /api/v1.0/sms_codes/<mobile>?image_code=xxx&image_code_id=xxx
# @api.route("/sms_codes/<re(r'1[34578]\d{9}'):mobile>")
# def get_sms_code(mobile):
#     """获取短信验证码"""
#     # 获取参数
#     image_code = request.args.get("image_code")
#     image_code_id = request.args.get("image_code_id")
#     # 校验参数
#     if not all([image_code_id, image_code]):
#         # 表示参数不完整
#         return jsonify(error=RET.PARAMERR, errmsg="参数不完整")
#     # 业务逻辑返回
#     # 从redis后端验证码取出来，先验证图片验证码
#     try:
#         real_image_code = redis_store.get("image_code_%s"%image_code_id)
#     except Exception as e:
#         current_app.logger.error(e)
#         return jsonify(error=RET.DBERR, errmsg="redis数据库异常")
#
#     # 判断图片验证码是否过期
#     if real_image_code is None:
#         # 图片中验证码过期
#         return jsonify(error=RET.NODATA, errmsg="图片验证码时效")
#
#     # 删除redis手机验证码图片,防止用户使用同一个验证码验证多次
#     try:
#         redis_store.delete("image_code_%s" % image_code_id)
#     except Exception as e:
#         current_app.logger.error(e)
#
#
#     # 与用户填写的值进行比对
#     if real_image_code.lower() != image_code.lower():
#         # 表示用户填写错误
#         return jsonify(error=RET.DATAERR, errmsg="图片验证码错误")
#
#     # p判断对于这个手机号的操作，在６０秒没有没有记录，如果有，则认为用户操作频繁，就不做处理
#     try:
#         send_flag = redis_store.get("send_sms_code_%s" % mobile)
#     except Exception as e:
#         current_app.logger.error(e)
#     else:
#         if send_flag is not None:
#             # 表示在６０之内发送过请求
#             return jsonify(error=RET.REQERR, errmsg="请求过于频繁，请于60秒以后再试")
#
#     # 判断这个手机号的操作，在60秒之内有没有之前的记录，如果有则认为用户操作频繁，不接受处理
#     try:
#         send_flag = redis_store.get("send_sms_code_%s" % mobile)
#     except Exception as e:
#         current_app.loger.error(e)
#     else:
#         if send_flag is not None:
#             # 表示在60秒内有过发送的记录
#             return jsonify(error=RET.REQERR, errmsg="请求过于频繁，请60秒之后再试")
#
#     # 判断手机号是否存在
#     try:
#         user = User.query.filter_by(mobile=mobile).first()
#     except Exception as e:
#         current_app.logger.error(e)
#
#     if user is not None:
#         return jsonify(error=RET.DATAEXIST, errmsg="用户手机号已存在")
#
#
#     # 生成验证码
#     sms_code = "%06d" % random.randint(0, 999999)
#
#     # 如果手机号存在，则生成短信验证码
#     try:
#         redis_store.setex("sms_code_%s" % mobile, constants.SMS_CODE_REDIS_EXPIRES, sms_code)
#         # 保存这个手机号的记录，防止用户在６０s内再次发送短信验证码
#         redis_store.setex("send_sms_code_%s" % mobile, constants.SEND_SMS_CODE_INTERVAL, 1)
#     except Exception as e:
#         current_app.logger.error(e)
#         return jsonify(error=RET.DBERR, errmsg="保存短信验证码异常")
#
#     # 发送短信
#     try:
#         ccp = CCP()
#         result = ccp.send_template_sms(mobile, [sms_code, int(constants.SMS_CODE_REDIS_EXPIRES / 60)], 1)
#     except Exception as e:
#         current_app.logger.error(e)
#         return jsonify(error=RET.THIRDERR, errmsg="短信服务器发送失败")
#
#     # 返回值
#     if result == 0:
#         return jsonify(error=RET.OK, errmsg="发送成功")
#     else:
#         return jsonify(error=RET.THIRDERR, errmsg="发送失败")

@api.route("/sms_codes/<re(r'1[34578]\d{9}'):mobile>")
def get_sms_code(mobile):
    """获取短信验证码"""
    # 获取参数
    image_code = request.args.get("image_code")
    image_code_id = request.args.get("image_code_id")
    # 校验参数
    if not all([image_code_id, image_code]):
        # 表示参数不完整
        return jsonify(error=RET.PARAMERR, errmsg="参数不完整")
    # 业务逻辑返回
    # 从redis后端验证码取出来，先验证图片验证码
    try:
        real_image_code = redis_store.get("image_code_%s"%image_code_id)
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(error=RET.DBERR, errmsg="redis数据库异常")

    # 判断图片验证码是否过期
    if real_image_code is None:
        # 图片中验证码过期
        return jsonify(error=RET.NODATA, errmsg="图片验证码时效")

    # 删除redis手机验证码图片,防止用户使用同一个验证码验证多次
    try:
        redis_store.delete("image_code_%s" % image_code_id)
    except Exception as e:
        current_app.logger.error(e)


    # 与用户填写的值进行比对
    if real_image_code.lower() != image_code.lower():
        # 表示用户填写错误
        return jsonify(error=RET.DATAERR, errmsg="图片验证码错误")

    # p判断对于这个手机号的操作，在６０秒没有没有记录，如果有，则认为用户操作频繁，就不做处理
    try:
        send_flag = redis_store.get("send_sms_code_%s" % mobile)
    except Exception as e:
        current_app.logger.error(e)
    else:
        if send_flag is not None:
            # 表示在６０之内发送过请求
            return jsonify(error=RET.REQERR, errmsg="请求过于频繁，请于60秒以后再试")

    # 判断这个手机号的操作，在60秒之内有没有之前的记录，如果有则认为用户操作频繁，不接受处理
    try:
        send_flag = redis_store.get("send_sms_code_%s" % mobile)
    except Exception as e:
        current_app.loger.error(e)
    else:
        if send_flag is not None:
            # 表示在60秒内有过发送的记录
            return jsonify(error=RET.REQERR, errmsg="请求过于频繁，请60秒之后再试")

    # 判断手机号是否存在
    try:
        user = User.query.filter_by(mobile=mobile).first()
    except Exception as e:
        current_app.logger.error(e)

    if user is not None:
        return jsonify(error=RET.DATAEXIST, errmsg="用户手机号已存在")


    # 生成验证码
    sms_code = "%06d" % random.randint(0, 999999)

    # 如果手机号存在，则生成短信验证码
    try:
        redis_store.setex("sms_code_%s" % mobile, constants.SMS_CODE_REDIS_EXPIRES, sms_code)
        # 保存这个手机号的记录，防止用户在６０s内再次发送短信验证码
        redis_store.setex("send_sms_code_%s" % mobile, constants.SEND_SMS_CODE_INTERVAL, 1)
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(error=RET.DBERR, errmsg="保存短信验证码异常")

    # 发送短信
    # try:
    #     ccp = CCP()
    #     result = ccp.send_template_sms(mobile, [sms_code, int(constants.SMS_CODE_REDIS_EXPIRES / 60)], 1)
    # except Exception as e:
    #     current_app.logger.error(e)
    #     return jsonify(error=RET.THIRDERR, errmsg="短信服务器发送失败")

    # 使用celery异步发送短信，　delay函数滴啊用后立即返回
    # send_sms.delay(mobile, [sms_code, int(constants.SMS_CODE_REDIS_EXPIRES / 60)], 1)

    # 查看返回值
    result = send_sms.delay(mobile, [sms_code, int(constants.SMS_CODE_REDIS_EXPIRES / 60)], 1)
    print('*'*30)
    print(result)
    print(result.id)
    print('*' * 30)
    # 通过get方法能获取celery异步执行的结果
    # get方法默认阻塞行为,会等到执行结果之后才返回
    #　get方法也接受参数timeout，超时时间，超过超时间拿不到结果，则返回
    print('-' * 10)
    ret = result.get()
    print(ret)
    print('-' * 10)
    # 返回值
    # if result == 0:
    #     return jsonify(error=RET.OK, errmsg="发送成功")
    # else:
    #     return jsonify(error=RET.THIRDERR, errmsg="发送失败")
    return jsonify(error=RET.OK, errmsg="发送成功")