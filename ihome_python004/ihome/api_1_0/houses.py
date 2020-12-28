# -*- coding:utf-8 -*-

from . import api
from ihome.utils.commons import login_required
from flask import g, current_app, jsonify, request, Response
from ihome.utils.response_code import RET
from ihome.utils.image_storage import storage
from ihome.modules import User, Area
from ihome import db, constants, redis_store
import json

@api.route("/areas")
def get_area_info():
    """获取城区"""
    # 尝试从redisduqushuju
    try:
        resp_json = redis_store.get("area_info")
    except Exception as e:
        current_app.logger.error(e)
    else:
        if resp_json is not None:
            current_app.logger.info("读取缓存的城市列表信息")
            print("读取缓存的城市列表信息-print")
            return resp_json,200,{"Content-Type":"application/json"}


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

    # 将数据
    resp_dict = dict(errno=RET.OK, errmsg="OK", data=area_dict_li)
    resp_json = json.dumps(resp_dict)

    # 将数据保存到redis
    try:
        redis_store.setex("area_info", constants.AREA_INFO_REDIS_CHCHE_EXPIRES, resp_json);
    except Exception as e:
        current_app.logger.erro(e)



    return resp_json,200,{"Content-Type":"application/json"}


@api.route("/houses/info", methods=["POST"])
@login_required
def save_house_info():
    """保存房屋的基本信息
    {
        title:"",  房屋名称标题
        price:"",  房屋单价
        area_id:"", 房屋所属城区编号
        address:"", 房屋地址
        room_count:"", 房屋包含的房间数目
        acreage:"",  房屋面积
        unit:"",  房屋布局（几室几厅）
        capacity:"", 房屋容纳人数
        beds:"", 房屋卧床数目
        deposit:"", 押金
        min_days:"", 最小入住天数
        max_days:"", 最大入住天数
        facility:[7,8],
    }

    """
    # 获取数据
    house_dict = request.get_jdon()

    title = house_dict.get("title")
    price = house_dict.get("price")
    area_id = house_dict.get("area_id")
    address = house_dict.get("address")
    room_count = house_dict.get("room_count")
    acreage = house_dict.get("acreage")
    unit = house_dict.get("unit")
    capacity = house_dict.get("capacity")
    beds = house_dict.get("beds")
    deposit = house_dict.get("deposit")
    min_days = house_dict.get("min_days")
    max_days = house_dict.get("max_days")

    user_id = g.user_id

    if not all([title, price, area_id, address, room_count, acreage, unit, capacity, beds, deposit, min_days, max_days]):
        return jsonify(errno=RET.PARAMERR , errmsg="请将数据填写完整")

    # 校验金额是否正确，
    try:
        price = int(float(price) * 100)
        deposit = int(float(deposit) * 100)
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.PARAMERR , errmsg="参数错误")

    # 校验城区id是否存在


