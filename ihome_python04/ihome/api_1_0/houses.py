# coding:utf-8

from . import api
from ihome.utils.common import login_required
from flask import g, current_app, jsonify, request
from ihome.utils.response_code import RET

from ihome.utils.image_storage import storage
from ihome.modules import Area
from ihome import db, constants


@api.route("/areas")
def get_area_info():
    """
        获取城区信息
    """
    print('进入城区接口')
    # 查询数据库，读取城区信息
    try:
        print("获取城区数据开始")
        area_li = Area.query.all()
        print("获取城区数据ｅｎｄ")
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(error=RET.DBERR, errmsg="数据库异常")

    print('城区接口查询完成')
    area_dict_li = []
    # 将对象转换为字典
    for area in area_li:
        area_dict_li.append(area.to_dict())
    print('城区接口列表装填完毕')


    return jsonify(error=RET.OK, errmsg="ok", data=area_dict_li)