# coding:utf-8
from flask import Flask
from flask_sqlalchemy import SQLALchemy
from flask_session import Session
from flask_wtf import CSRFProtect　# csrf防护机制

import redis

app = Flask(__name__)


class Config(object):
    '''配置信息'''
    DEBUG = True

    SECRET_LEY = "AAFEBaegnbsa"

    # 数据库
    SQLALCHEMY_DATABASES_URI = "mysql://root:mysql@127.0.0.1:3306/ihome_python04"
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    # redis
    REDIS_HOST = "192.168.0.106"
    REDIS_PORT = 6379

    # flask-session配置 https://pythonhosted.org/Flask-Session/
    SESSION_TYPE = "redis"
    SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST, port=REDIS_HOST)
    SESSION_USE_SIGNER = True # 对cookie中的session_id进行隐藏
    PERMANENT_SESSION_LIFETIME = 604800 # session过期时间设置



app.config.from_object(Config)

db = SQLALchemy(app) # 连接数据库

# 使用redis, 创建redis连接对象
redis_store = redis.StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT)

# 利用flask_session将session数据保存到redis中
Session(app)

# 为flask补充csrf防护
CSRFProtect(app)





@app.route('/index')
def index():
    return 'index page'

if __name__ == '__main__':
    app.run()