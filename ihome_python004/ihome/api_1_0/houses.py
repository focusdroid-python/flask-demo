# -*- coding:utf-8 -*-

from . import api
from ihome.utils.commons import login_required
from flask import g, current_app, jsonify, request, Response
from ihome.utils.response_code import RET
from ihome.utils.image_storage import storage
from ihome.modules import User, Area, House, Facility, HouseImage
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
    house_dict = request.get_json()

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
    try:
        area = Area.query.get(area_id)
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmsg="数据异常")

    if area is None:
        return jsonify(errno=RET.NODATA, errmsg="城区信息有误")

    # 保存房屋信息
    house = House(
        user_id=user_id,
        area_id=area_id,
        title=title,
        price=price,
        address=address,
        room_count=room_count,
        acreage=acreage,
        unit=unit,
        capacity=capacity,
        beds=beds,
        deposit=deposit,
        min_days=min_days,
        max_days=max_days,
    )

    db.session.add(house)

    # 保存设施信息
    facility_ids = house_dict.get("facility")

    if facility_ids:
        # select * from ih_facility__info where id in []
        try:
            facilites = Facility.query.filter(Facility.id.in_(facility_ids)).all()
        except Exception as e:
            current_app.logger.error(e)
            return jsonify(erron=RET.DBERR, errmsg="数据库异常")

        if facilites:
            # 表示有合法的设施数据
            # 保存设施数据
            house.facilities = facilites
            try:
                db.session.add(house)
                db.session.commit()
                current_app.loggrt.info(house)
            except Exception as e:
                current_app.logger.error(e)
                db.session.rollback()
                return jsonify(errno=RET.DBERR, errmsg="保存数据失败")

    # 保存数据成功
    return jsonify(errno=RET.OK, errmsg="保存成功", data={"house_id": house.id})


@api.route("/house/image", methods=["POST"])
@login_required
def save_house_image():
    """保存房屋图片
        参数： 图片  房屋ID
    """
    # flask获取参数的方式,
    # 直接传文件 request.files["参数名"] request.files.get("参数名")
    # 表单传文件 request.form["参数名"] request.form.get("参数名")
    # get请求 request.args["参数名"] request.args.get("参数名")
    # post request.get_json()
    # image_file1 = request.files.get("house_image")
    image_file = request.files["house_image"]
    house_id = request.get_json().get("house_id")
    print(house_id)
    print(image_file)
    if not all([house_id, image_file]):
        return jsonify(errno=RET.PARAMERR, errmsg="参数错误")

    # 判断house_id 的正确性
    try:
        house = House.query.get(house_id)
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmsg="数据库异常")

    if house is None:
        return jsonify(errno=RET.DBERR, errmsg="房屋不存在")

    image_data = image_file
    # 保存图片到七牛中
    try:
        file_name = storage(image_data)
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.THIRDERR, errmsg="上传图片失败")

    # 保存数据信息到数据库中
    house_image = HouseImage(house_id=house_id, url=file_name)
    db.session.add(house_image)

    # 处理房屋的主图片
    if not house.index_image_url:
        house.index_image_url = file_name
        db.session.add(house)

    try:
        db.session.commit()
    except Exception as e:
        current_app.logger.error(e)
        db.session.rollback()
        return jsonify(error=RET.DBERR, errmsg="保存图片数据异常")

    img_url = constants.QUNIU_URL_DOMAIN + file_name

    return jsonify(error=RET.OK, errmsg="保存成功", data={"img_url": img_url})

@api.route("/user.houses", methods=["GET"])
@login_required
def get_user_houses():
    """获取房东发布的房源信息"""
    user_id = g.user_id

    try:
        user = User.query.get(user_id)
        houses = user.houses
    except Exception as e:
        current_app.logging.error(e)
        return jsonify(errno=RET.DBERR, errmsg="获取数据失败")

    # 将查询到的房屋信息转换为字典存放在列表中
    houses_list = []
    if houses:
        for house in houses:
            houses_list.append(house.to_basic_dict())
    return jsonify(errno=RET.OK, errmsg="ok", data={"houses": houses_list})



def get_house_index():
    """获取主页幻灯片展示的房屋信息"""
    # 冲缓存中尝试获取数据
    try:
        ret = redis_store.get("home_page_data")
    except Exception as e:
        current_app.logging.error(e)
        ret = None

    if ret:
        current_app.logging.info("hit house index info redis")
        return "{'errno':0, 'errmsg':'ok', 'data':'%s'}" % ret, 200, {"Content-Type":"application/json"}
    else:
        try:
            # 查询数据库，返回房屋订单数目最多的5条数据
            houses = House.query.order_by(House.order_count.desc()).limit(constants.HOME_PAGE_MAX_HOUSES)
        except Exception as e:
            current_app.logging.error(e)
            return jsonify(errno=RET.DBERR, errmsg="查询数据失败")

        if not houses:
            return jsonify(errno=RET.NODATA, errmsg="查询无数据")

        houses_list = []
        for house in houses:
            # 如果房屋未设置主图片，则跳过
            if not house.index_image_url:
                continue
            houses_list.append(house.to_basic_dict())

        # 将数据转换为json，并保存到redis缓存中
        json_houses = json.dumps(houses_list)

        try:
            redis_store.setex("house_page_data", constants.HOME_PAGE_DATA_REDIS_EXPIRES, json_houses)
        except Exception as e:
            current_app.logger.error(e)
        return "{'error':0, 'errmsg':'ok', 'data':%s}" % json_houses, 200, {'Content-Type':'application/json'}

















