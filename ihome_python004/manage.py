# coding:utf-8


from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import redis



app = Flask(__name__)


class Config(object):
    """配置信息"""
    DEBUG = True

    SECRET_KEY = "ihjoINBIOJIjuni89789890-00-"

    # 数据库
    SQLALCHEMY_DATABASE_URL = "mysql://root:mysql@127.0.0.1:3306/ihome_python004"
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    # redis配置
    # REDIS_HOST = "127.0.0.1"
    REDIS_HOST = "192.168.0.108"
    REDIS_PORT = 6379

# 导入到app中
app.config.from_object(Config)
# 创建数据库　db
db = SQLAlchemy(app)

# 创建redis连接对象
redis_store = redis.StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT)




@app.route("/index")
def index():
    return 'index page'


if __name__ == "__main__":
    app.run()

