## flask前后端分离项目开发步骤
- 初始化项目
```
1. db mysql
2. redis
3. wtf csrf
4. session
5. 日志
```
 -  分析需求
 -  编写代码
 -  编写单元测试
 -  自测
 -  接口文档


- 项目中添加mysql
- 项目中安装redis


### 初始化项目
```python
from flask import Flask


app = Flask(__name__)

@app.route("/index")
def index():
    return "index page"

if __name__ == '__main__':
    app.run()
```
### 项目中添加mysql
```python
- from flask_sqlalchemy import SQLALchemy
# 需要SQLALchemy这个包

# -*- coding:utf-8 -*-

from flask import Flask
from flask_sqlalchemy import SQLALchemy


app = Flask(__name__)


class Config(object):
    """配置信息"""
    DEBUG = True

    SECRET_KEY = "KHJHANFkjnkjnkjnbjKJNBK348u8"

    # 数据库配置信息
    SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3306/ihome_python004"
    SQLALCHEMY_TRACK_MODIFICATIONS = True

app.config.from_object(Config)

db = SQLALchemy(app)

@app.route("/index")
def index():
    return "index page"

if __name__ == '__main__':
    app.run()
```

### 项目中安装redis
```python
- 安装flask-session
https://flask-session.readthedocs.io/en/latest/
# -*- coding:utf-8 -*-

from flask import Flask
from flask_sqlalchemy import SQLALchemy

import redis

app = Flask(__name__)


class Config(object):
    """配置信息"""
    DEBUG = True

    SECRET_KEY = "KHJHANFkjnkjnkjnbjKJNBK348u8"

    # 数据库配置信息
    SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3306/ihome_python004"
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    # redis
    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379

app.config.from_object(Config)
# 数据库
db = SQLALchemy(app)

# 创建redis连接对象
redis_store = redis.StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT)

@app.route("/index")
def index():
    return "index page"

if __name__ == '__main__':
    app.run()
```

### 配置flaskk-session
```python
# -*- coding:utf-8 -*-

from flask import Flask
from flask_sqlalchemy import SQLALchemy
from flask_session import Session
from flask_wtf import CSRFProtect
import redis

app = Flask(__name__)


class Config(object):
    """配置信息"""
    DEBUG = True

    SECRET_KEY = "KHJHANFkjnkjnkjnbjKJNBK348u8"

    # 数据库配置信息
    SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3306/ihome_python004"
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    # redis
    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379

    # flask-session配置
    SESSION_TYPE = "redis"
    SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT)
    SESSION_USE_SIGNER = True #　对cookie中session_id进行隐藏处理
    PERMANENT_SESSION_LIFETIME = 86400 # session数据的有效期，单位秒

app.config.from_object(Config)
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
```
### 生成csrf_token
```python
# -*- coding:utf-8 -*-
from . import api
from ihome import modules, db
import logging
from flask import current_app, make_response
from flask_wtf import csrf

@api.route("/index")
def index():
    current_app.logger.error("error manager")
    current_app.logger.warn("warn manager")
    current_app.logger.info("info manager")
    current_app.logger.debug("debug manager")

    # 创建一个csrf_token值
    csrf_token = csrf.generate_csrf()

    # falsk提供的返回静态文件的方法
    resp = make_response()

    # 设置cookie
    resp.set_cookie("csrf_token", csrf_token)

    return resp


```

### 注册
```
- 在前端访问验证码的时候可以在前端生成一uuid这样保证访问的唯一性
```

### 短信验证码
```

```

接口文档
1. 接口名称
1. 描述
1. url
1. 请求方式
1.  传入参数
1. 返回值

借口:获取图片验证码
描述:前端访问，可以获取到验证码图片

url: /api/v1.0.image_codes/<image_code_id>

传入参数:
    格式：　参数是查询字符串　　请求体的表单　　json  xml
    名字　　　        类型　　　是否必须　　　说明
    image_code_id   字符串　　　是　　　　 验证码图片编号
    
返回值：
    格式：　正常：图片　　　　异常： json
    名字　　　　　　类型　　　　　　是否必传　　　　　说明
    error       字符串　　　　　　　否　　　　　　错误代码
    errmsg      字符串　　　　　　　否　　　　　　错误内容
    
    示例：
    errno=RET.DBERR, errmsg="保存图片验证码信息失败"

### redis命令使用文档
```
http://redisdoc.com/index.html
```

3. 图片服务
> 1. 保存到程序本地
> 1. 备份的问题
> 1. 多机存储问题
>
>
>
### 文件存储解决方案
> 1. 自己搭建文件存储系统 FastDFS 快速分布式文件存储系统, HDFS Hadoop分布式文件系统
> 1. 选择第三方 七牛云存储
> 1. 