# -*- coding:utf-8 -*-

from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from ihome import constants
from . import db


class BaseModel(object):
    '''模型基类，为每个模型补充创建时间与更新时间'''

    create_time = db.Column(db.DateTime, default=datetime.now) # 记录的创建时间
    update_time = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now) # 记录的更新时间

class User(BaseModel, db.Model):
    '''用户'''
    __tablename__ = "ih_user_profile"

    id = db.Column(db.Integer, primary_key=True) # 用户编号
    name = db.Column(db.String(32), unique=True, nullable=False) # 用户昵称
    password_hash = db.Column(db.String(128), nullable=False) # 加密的密码
    mobile = db.Column(db.String(11), unique=True, nullable=False) # 手机号
    real_name = db.Column(db.String(32)) # 真实姓名
    id_card = db.Column(db.String(20)) # 身份证号
    avatar_url = db.Column(db.String(128)) # 用户头像路径
    houses = db.relationship("House", backref="user") # 用户发布的房屋
    orders = db.relationship("Order", backref="user") # 用户下的订单

    @property
    def password(self):
        """获取password属性时被调用"""
        raise AttributeError("不可读")

    @password.setter
    def password(self, passwd):
        """设置password属性时被调用，设置密码加密"""
        self.password_hash = generate_password_hash(passwd)

    def check_password(self, passwd):
        """检查密码正确性"""
        return check_password_hash(self.password_hash, passwd)

    def to_dict(self):
        """将对象转换为字典数据"""
        user_dict = {
            "user_id": self.id,
            "name": self.name,
            "mobile": self.mobile,
            "avatar": constants.QINIU_DOMIN_PREFIX + self.avatar_url if self.avatar_url else "",
            "create_time": self.create_time.strftime("%Y-%m-%d %H:%M:%S"),
        }
        return user_dict

    def auth_to_dict(self):
        """将实名信息转换成字典数据"""
        auth_dict = {
            "user_id": self.id,
            "real_name": self.real_name,
            "id_card": self.id_card
        }
        return auth_dict



class Area(BaseModel, db.Model):
    """城区"""

    __tablename__ = "ih_area_info"

    id = db.Column(db.Integer, primary_key=True) # 区域编号
    name = db.Column(db.String(32), nullable=False) # 区域名字
    houses = db.relationship("House", backref="area") # 区域的房屋

    def to_dict(self):
        """将对象转换成字典数据"""
        area_dict = {
            "aid": self.id,
            "aname": self.name
        }
        return area_dict

# 房屋设施表，建立房屋设施的多对多关系
house_facility = db.table(
    "ih_house_facility",
    db.Column("house_id", db.Integer, db.ForeignKey("ih_house_info.id"), primary_key=True), # 房屋编号
    db.Column("facility_id", db.Integer, db.ForeignKey("ih_facility_info_id"), primary_key=True) # 设施编号
    # db.Column("create_time", db.DateTime, default=datetime.now),
    # db.Column("update_time", db.DateTime, default=datetime.now, onupdate=datetime.now)
)

class House(BaseModel, db.Model):
    """房屋信息"""

    __tablename__ = 'ih_house_info'

    id = db.Column(db.Integer, primary_key=True) # 房屋编号
    user_id = db.Column(db.Integer, db.ForeignKey("ih_user_profile.id"), nullable=False) # 房屋主任的用户id
    area_id = db.Column(db.Integer, db.ForeignKey("ih_area_info.id"), nullable=False) # 归属地的区域编号
    title = db.Column(db.Sting(64), nullable=False) # 标题
    price = db.Column(db.Integer, default=0) # 单价
    address = db.Column(db.String(512), default="") # 地址
    room_count = db.Column(db.Integer, default=1) # 房间数目
    acreage = db.Column(db.Integer, default=0) # 房屋面积
    unit = db.Column(db.String(32), default="") # 房屋单元，如几室几厅
    capacity = db.Column(db.Integer, default=1) # 房屋容纳的人数
    beds = db.Column(db.String(32), default="") # 房屋床铺的配置
    deposit = db.Column(db.Integer, default=0) # 房屋押金
    min_days = db.Column(db.Integer, default=1) # 最少入住天数
    max_days = db.Column(db.Integer, default=0) # 最多入住天数
    order_count = db.Column(db.Integer, default=0) # 预定完成该订单的房间数
    index_image_url = db.Column(db.String(256), default="") # 房屋主图片路径
    facilities = db.relationship("Facility", secondary=house_facility) # 房屋的设施
    images = db.relationship("HouseImage") # 房屋的图片
    orders = db.relationship("Order", backref="house") # 房屋的订单

    def to_basic_dict(self):
        """将信息转换成字典"""
        house_dict = {
            "house_id": self.id,
            "title":self.title,
            "price":self.price,
            "area_name":self.area.name,
            "img_url":self.constants.QINIU_DOMIN_PREFIN + self.index_image_url if self.index_image_url else "",
            "room_count":self.room_count,
            "order_count":self.order_count,
            "address":self.address,
            "user_avatar":self.constants.QINIU_DOMIN_PREFIX + self.user.avatar_url if self.user.avatar_url else "",
            "ctime":self.create_time.strftime("%Y-%m-%d")
        }
        return house_dict

    def to_full_dict(self):
        """将详细信息装换成字典信息"""
        house_dict = {
            "hid": self.id,
            "user_id": self.user_id,
            "user_name": self.user_name,
            "user_avatar": self.constants.QINIU_DOMIN_PREFIX + self.user.avatar_url if self.user.avatar_url else "",
            "title": self.title,
            "price": self.price,
            "address": self.address,
            "room_count": self.room_count,
            "acreage": self.acreage,
            "unit": self.unit,
            "capacity": self.capacity,
            "beds": self.beds,
            "deposit": self.deposit,
            "max_days": self.max_days,
            "min_days": self.min_days,
        }


class Facility(BaseModel, db.Model):
    """设施信息"""

    __tablename__ = "ih_facility_info"

    id = db.Column(db.Integer, primary_key=True) # 设施编号
    name = db.Column(db.String(32), nullable=False) # 设施名字