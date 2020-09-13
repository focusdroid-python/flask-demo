# -*- coding:utf-8 -*-
from flask import Flask
from config import config_map
from flask_sqlalchemy import SQLALchemy


# 数据库
db = SQLALchemy()


# 工厂模式
def create_app(config_name):
    """
    创建appa对象
    :param config_name: str 配置模式的名字　("develop", "product")
    :return:
    """
    app = Flask(__name__)

    # 根据配置模式的名字获取配置参数的类
    config_clss = config_map.get(config_name)
    app.config.from_object(config_clss)

    # 使用app初始化db
    db.init_app(app)
    return app