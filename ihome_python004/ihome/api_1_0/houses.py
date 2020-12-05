# -*- coding:utf-8 -*-

from . import api
from ihome.utils.commons import login_required
from flask import g, current_app, jsonify, request, Response
from ihome.utils.response_code import RET
from ihome.utils.image_storage import storage
from ihome.modules import User, Area
from ihome import db, constants


@api.route("/areas")
def get_area_info():
    """获取城区"""
    # 查询数据库,读取城区信息
    try:
        area_li = Area.query.all()
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmsg="数据库异常")

    area_dict_li = []
    #
    for area in area_li:
        area_dict_li.append(area.to_dict())


    return jsonify(errno=RET.OK, errmsg="OK", data=area_dict_li)