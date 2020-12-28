# -*- coding:utf-8 -*-

from . import api
from ihome.utils.commons import login_required
from flask import g, current_app, jsonify, request, Response, session
from ihome.utils.response_code import RET
from ihome.utils.image_storage import storage
from ihome.modules import User, constants
from ihome import db

import json


@api.route("/users/avatar", methods=["POST"])
@login_required
def set_user_avatar():
    """
    设置用户图像
    参数: 用户 用户id
    :return:
    """
    # 装饰器的代码中已经将_id,bao 保存到对象,所以
    user_id = g.user_id

    # 获取图片
    # flask获取参数的方式,
    # 直接传文件 request.files["参数名"] request.files.get("参数名")
    # 表单传文件 request.form["参数名"] request.form.get("参数名")
    # get请求 request.args["参数名"] request.args.get("参数名")
    # post request.get_json()
    image_file = request.files["avatar"]
    # image_file1 = request.files.get("avatar")
    print(image_file)
    # print(image_file1)
    if image_file is None:
        return jsonify(errno=RET.PARAMERR, errmsg="未上传图片")

    # image_data = image_file.read()
    image_data = image_file

    # 调用七牛上传图片, 返回文件名
    try:
        file_name = storage(image_data)
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.THIRDERR, errmsg="上传图片失败")

    # 保存文件名到数据库中
    img_url = constants.QUNIU_URL_DOMAIN+file_name
    try:
        User.query.filter_by(id=user_id).update({"avatar_url": img_url})
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmsg="保存图片信息失败")

    # 保存成功返回
    data = {"status": 200,"avatar_url": img_url}
    # data = json.dumps(data, ensure_ascii=False)
    return jsonify(errno=RET.OK, errmsg="保存成功!", data=data)
    # return (data, 200, {"Content-Type":"text/json"})


@api.route("/users/name", methods=["POST"])
@login_required
def change_user_name():
    """
        修改用户名
        params: name
    """
    # 使用login_required装饰器后，可以从g对象中获取user_id
    user_id = g.user_id

    # 获取用户想设置的用户名
    req_data = request.get_json()
    if not req_data:
        return jsonify(errno=RET.PARAMERR, errmsg="参数不完整")

    name = req_data.get("name")
    print("修改用户名start"*20)
    print(name)
    print("修改用户名end"*20)
    if not name:
        return jsonify(errno=RET.PARAMERR, errmsg="名字不能为空")

    # 保存用户昵称name，并同时判断name是否重复（利用数据库唯一索引）
    try:
        User.query.filter_by(id=user_id).update({"name":name})
        db.session.commit()
    except Exception as e:
        current_app.logger.error(e)
        db.session.rollback()
        return jsonify(errno=RET.DBERR, errmsg="设置用户错误")

    # 修改session数据中的name字段
    session["name"] = name
    return jsonify(errno=RET.OK, errmsg="ok", data={"name":name})


@api.route("/user", methods=["GET"])
@login_required
def get_user_profile():
    """
        获取个人信息
    """
    user_id = g.user_id

    # 查询数据库获取个人信息
    try:
        user = User.query.get(user_id)
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmsg="获取用户信息失败")

    if user is None:
        return jsonify(errno=RET.NODATA, errmsg="无效操作")

    return jsonify(errno=RET.OK, errmsg="ok", data=user.to_dict())



@api.route("/user/auth", methods=["GET"])
@login_required
def get_user_auth():
    """
        获取用户的实名认证信息
    """

    user_id = g.user_id

    # 在数据库中查询信息
    try:
        user = User.query.get(user_id)
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmsg="获取用户信息失败")

    if user is None:
        return jsonify(errno=RET.NODATA, errmsg="无效操作")

    return jsonify(errno=RET.OK, errmsg="ok", data=user.auth_to_dict())


@api.route("/users/author", methods=["POST"])
@login_required
def get_users_author():
    """保存实名认证信息"""
    user_id = g.user_id
    # 获取参数
    req_data = request.get_json()
    if not req_data:
        return jsonify(errno=RET.PARAMERR, errmsg="参数错误")

    real_name = req_data.get("real_name")
    id_card = req_data.get("id_card")
    # 检验参数
    if not all([real_name, id_card]):
        return jsonify(errno=RET.PARAMERR, errmsg="参数错误")
    # 保存用户信息
    try:
        User.query.filter_by(id=user_id, real_name=None, id_card=None).update({"real_name": real_name, "id_card":id_card})
        db.session.commit()
    except Exception as e:
        current_app.logger.error(e)
        db.session.rollback()
        return jsonify(error=RET.DBERR, errmsg="保存用户实名信息失败")
    # 返回信息
    return jsonify(errno=RET.OK,errmsg="OK")



