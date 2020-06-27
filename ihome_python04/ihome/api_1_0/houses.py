# coding:utf-8

from . import api
from ihome.utils.common import login_required
from flask import g, current_app, jsonify, request
from ihome.utils.response_code import RET

from ihome.modules import Area, House, Facility
from ihome import db, constants, redis_store
import json


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

@api.route("/houses/info", methods=["POST"])
@login_required
def save_house_info():
    """保存房屋的基本信息－发布新房源"""
    pass
    """
        "title": self.title,
        "price": self.price,
        "address": self.address,
        "room_count": self.room_count,
        "acreage": self.acreage,
        "unit": self.unit,
        "capacity": self.capacity,
        "beds": self.beds,
        "deposit": self.deposit,
        "min_days": self.min_days,
        "max_days": self.max_days,
    """
    # 获取数据
    user_id = g.user_id
    house_data = request.get_json()

    title = house_data.get("title") # 房屋标题
    price = house_data.get("price") # 房屋单价
    area_id = house_data.get("area_id") # 房屋所属城区编号
    address = house_data.get("address") # 房屋地址
    room_count = house_data.get("room_count") # 房屋包含的房间数目
    acreage = house_data.get("acreage") # 房屋面积
    unit = house_data.get("unit") # 房屋布局(几室季婷)
    capacity = house_data.get("capacity") # 房屋容纳人数
    beds = house_data.get("beds") # 房屋卧床数目
    deposit = house_data.get("deposit") # 房屋押金
    min_days = house_data.get("min_days") # 房屋最小入住天数
    max_days = house_data.get("max_days") # 房屋最大入住天数

    # 校验参数
    if not all([title, price, area_id, address, room_count, acreage, unit, capacity, beds, deposit, min_days, max_days]):
        return jsonify(error=RET.PARAMERR, errrmsg="参数不完整")

    # 校验金额是否正确
    try:
        price = int(float(price) * 100)
        deposit = int(float(deposit) * 100)
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(error=RET.PARAMERR, errmsg="参数错误")

    # 城区id是否存在
    try:
        area = Area.query.get(area_id)
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(error=RET.DBERR, errmsg="数据异常")

    if area is None:
        return jsonify(error=RET.NODATA, errmsg="城区信息有误")

    # 保存房屋信息
    house = House(
        user_id = user_id,
        area_id = area_id,
        title=title,
        price = price,
        address = address,
        room_count = room_count,
        acreage = acreage,
        unit = unit,
        capacity = capacity,
        beds = beds,
        deposit = deposit,
        min_days = min_days,
        max_days = max_days
    )

    # 处理房屋的设施信息
    facility_ids = house_data.get("facility")

    # 如果用户勾选了设施信息，在保存数据库
    if facility_ids:
        # ['7', '8']
        # select * from ih_facility_info where id in []
        try:
            facilities = Facility.query.filter(Facility.id.in_(facility_ids)).all()
        except Exception as e:
            current_app.logger.error(e)
            return jsonify(error=RET.DBERR, errmsg="数据库异常")

        if facilities:
            # 表示有合法数据
            # 保存设施数据
            house.facilities = facilities

    try:
        db.session.add(house)
        db.session.commit()
    except Exception as e:
        current_app.logger.error(e)
        db.session.rollback()
        return jsonify(error=RET.DBERR, errmsg="保存数据失败")

    # 保存数据成功
    return jsonify(error=RET.OK, errmsg="ok", data={"house.id": house.id})


@api.route("/houses/image", methods=["POST"])
def save_house_image():
    """保存房屋图片
        参数　　图片　　房屋id
    """
    image_file = request.files.get("house_image")

    house_id = request.form.get("house_id")

    if not all([image_file, house_id]):
        pass

