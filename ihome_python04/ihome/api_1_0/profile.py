# -*- coding: utf-8 -*-

from . import api
from ihome.utils.common import login_required
from flask import g, current_app, jsonify, request, session
from ihome.utils.response_code import RET

from ihome.utils.image_storage import storage
from ihome.modules import User
from ihome import db, constants

@api.route("/user/avatar", methods=["POST"])
@login_required
def set_user_avatar():
    """
        设置用户图像
        参数：　图片　　用户id  　　
    """
    # 装饰器的代码中已经将user_id保存到g对象中，所以视图中可以直接读取
    user_id = g.user_id

    # 获取图片
    image_file = request.files.get("avatar")

    if image_file is None:
        return jsonify(error=RET.PARAMERR, errmsg="未上传图片")

    image_data = image_file.read()

    # 调用七牛上传文件, 返回文件名
    try:
        file_name = storage(image_data)
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(error=RET.THIRDERR, errmsg="上传文件失败")

    # 保存文件名到数据库中
    try:
        User.query.filter_by(id=user_id).update({"avatar_url": file_name})
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        current_app.logger.error(e)
        return jsonify(error=RET.DBERR, errmsg="保存图片失败")


    avatar_url = constants.QUNIU_URL_DOMAIN + file_name
    # 保存成功反馈
    return jsonify(error=RET.OK, errmsg="保存成功",data={"avatar_url": avatar_url})


@api.route("/users/name", methods=["PUT"])
@login_required
def change_user_name():
    """修改用户名"""
    # 使用login_requires装饰器后，可以从对象中获取用户的user_id
    user_id = g.user_id

    # 获取用户想要设置的用户名
    req_data = request.get_json()
    if not req_data:
        return jsonify(error=RET.PARAMERR, errmsg="参数不完整")

    name = req_data.get("name") # 用户想要设置的名字
    if not name:
        return jsonify(error=RET.PARAMERR, errmsg="名字不能为空")

    # 保存用户昵称name，　并同时判断name是否重复（利用数据库唯一索引）
    try:
        User.query.filter_by(id=user_id).update({"name": name})
        db.session.commit()
    except Exception as e:
        current_app.logger.error(e)
        db.session.rollback()
        return jsonify(error=RET.DBERR, errmsg="设置用户错误")

    # 修改session数据中的name字段
    session["name"] = name
    return jsonify(error=RET.DBERR, errmsg="ok", data={"name": name})

@api.route("/user", methods=["GET"])
def get_user():
    """获取个人信息"""
    user_id = g.user_id

    # 查询数据库获取个人信息
    try:
        user = User.query.get(user_id)
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(error=RET.DBERR, errmsg="获取用户信息失败")

    if user is None:
        return jsonify(error=RET.NODATA, errmsg="无效操作")

    return jsonify(error=RET.OK, errmsg="ok", data=user.to_dict())