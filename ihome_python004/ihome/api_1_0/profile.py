# -*- coding:utf-8 -*-

from . import api
from ihome.utils.commons import login_required
from flask import g, current_app, jsonify, request
from ihome.utils.response_code import RET
from ihome.utils.image_storage import storage
from ihome.modules import User, constants
from ihome import db


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
    image_file = request.files.get("avatar")
    if image_file is None:
        return jsonify(errno=RET.PARAMERR, errmsg="未上传图片")

    image_data = image_file.read()

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
    return jsonify(errno=RET.OK, errmsg="保存成功!", data={"status": 200,"avatar_url": img_url})
