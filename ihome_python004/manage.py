# -*- coding:utf-8 -*-

from flask import Flask
from flask_sqlalchemy import SQLALchemy
from flask_session import Session
from flask_wtf import CSRFProtect
from config import Config
import redis

from ihome import create_app

app = create_app("develop")

# 数据库
db = SQLALchemy(app)

# 创建redis连接对象
redis_store = redis.StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT)

# 利用flask-session，将session数据保存到redis中
Session(app)

# 为flask补充CSRF防护机制
CSRFProtect(app)



@app.route("/index")
def index():
    return "index page"

if __name__ == '__main__':
    app.run()