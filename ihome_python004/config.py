# coding:utf-8
import redis


class Config(object):
    """配置信息"""
    SECRET_KEY = "ihjoINBIOJIjuni89789890"

    # 数据库
    SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3306/ihome_python004"
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    # SQLALCHEMY_DATABASE_URI = "mysql://root:Asmie1234@49.233.195.154:3306/ihome_python004"
    # SQLALCHEMY_TRACK_MODIFICATIONS = True

    # redis配置
    REDIS_HOST = "127.0.0.1"
    # REDIS_HOST = "192.168.0.108"
    REDIS_PORT = 6379

    # flask-session配置
    SESSION_TYPE = "redis"
    SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT)
    # SESSION_USE_SIGNER = True # 对cookie中session的进行隐藏
    PERMANENT_SESSION_LIFETIME = 86400 # session数据的有效期，单位:秒

class DevelopmentConfig(Config):
    """开发模式的配置信息"""
    DEBUG = True


class ProductionConfig(Config):
    """生产环境的配置信息"""
    pass

config_map = {
    "develop": DevelopmentConfig,
    "product": ProductionConfig
}