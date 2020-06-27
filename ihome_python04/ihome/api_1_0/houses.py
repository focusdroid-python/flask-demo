# coding:utf-8

from . import api
from ihome.utils.common import login_required
from flask import g, current_app, jsonify, request
from ihome.utils.response_code import RET

from ihome.utils.image_storage import storage
from ihome.modules import Area
from ihome import db, constants, redis_store
import json

area_li = None

@api.route("/areas")
def get_area_info():
    """
        获取城区信息
    """
    # 尝试从redis后直接读取数据
    try:
        print("进入redis数据库获取数据")
        resp_json = redis_store.get("area_info")
    except Exception as e:
        current_app.logger.error(e)
    else:
        if resp_json is not None:
            print("redis数据库不为空，可以获取到数据,并返回")
            # redis有缓存数据
            return resp_json, 200, {"Content-Type": "application/json"}


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


    # 将数据转换为json字符串
    resp_dict = dict(error=RET.OK, errmsg="ok", data=area_dict_li)
    resp_json = json.dumps(resp_dict)

    try:
        # 给数据设置redis缓存数据
        redis_store.setex("area_info", constants.AREA_INFO_REDIS_CHCHE_EXPIRES,resp_json)
    except Exception as e:
        current_app.logger.error(e)


    return resp_json, 200, {"Content-Type": "application/json"}