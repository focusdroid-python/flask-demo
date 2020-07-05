# coding:utf-8
import redis

class Config(object):
    '''配置信息'''


    SECRET_LEY = "AAFEBaegnbsa"

    # 数据库
    SQLALCHEMY_DATABASE_URI = 'mysql://root:mysql@127.0.0.1:3306/ihome_python04'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    # SQLALCHEMY_DATABASE_URI = '127.0.0.1'

    # redis
    # REDIS_HOST = '192.168.0.108'
    REDIS_HOST = '127.0.0.1'
    REDIS_PORT = 6379

    # flask-session配置 https://pythonhosted.org/Flask-Session/
    SESSION_TYPE = "redis"
    SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT)
    # SESSION_USE_SIGNER = True # 对cookie中的session_id进行隐藏
    # SESSION_USE_SIGNER
    PERMANENT_SESSION_LIFETIME = 604800 # session过期时间设置


class DevlopmentConfig(Config):
    """开发模式配置信息"""
    DEBUG = True


class ProductionConfig(Config):
    """生产环境配置信息"""
    pass


config_map = {
    "develop": DevlopmentConfig,
    "product": ProductionConfig
}