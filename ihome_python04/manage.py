# coding:utf-8
from flask import Flask, session
from flask_sqlalchemy import SQLALchemy
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

app.config.from_object(Config)

db = SQLALchemy(app) # 连接数据库

# 使用redis, 创建redis连接对象
redis_store = redis.StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT)






@app.route('/index')
def index():
    session[] =
    session.get()
    return 'index page'

if __name__ == '__main__':
    app.run()