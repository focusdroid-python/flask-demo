# -*- coding: utf-8 -*-

from . import api
from ihome.utils.common import login_required
from flask import g, current_app, jsonify, request
from ihome.utils.response_code import RET


@api.route("/users/avatar", methods=["POST"])
@login_required
def set_user_avatar():
    """
    设置用户图像
    参数：　图片（多媒体表单格式）　　用户id (g.user_id)
    """
    # 获取参数, 装饰器的代码已经将user_id保存在g对象中，所以视图中可以可以直接读取
    user_id = g.user_id

    # 获取图片
    image_file = request.files.get("avatar")

    if image_file is None:
        return jsonify(error=RET.PARAMERR, errmsg="未上传图片")

    image_data = image_file.read()

    # 调用七牛上传文件
    storage(image_data)
    #

