# Flask
`flask基础`
> 初始化参数
```
import_name
static_url_path
static_folder 默认static
template_folder 默认templates
```
> 配置参数
```
# 配置参数的使用方式
# 1, 使用配置文件
# app.config.from_pyfile('config.cfg')
# 2.
# class Config(object):
#     DEBUG = True

# app.config.from_object(Config)

# 3.
app.config['DEBUG'] = True
```

## abort
```
abort
使用abort函数可以立即终止视图函数的执行并可以返回给前端特定的信息

@app.errorhandler  自定义错误处理

```
## 响应信息
```
响应信息一般在浏览器的Response headers中显示，
在flask中一般有以下几种定义header的方法
#1. 使用元祖，返回自定义的响应信息
    return 'index page', 400, [('focusdroid', 'python'), ('city', 'name')]
    return 'index page2', 400, {'name':'王旭', 'age':30}
例子：
city: name
Content-Length: 10
Content-Type: text/html; charset=utf-8
Date: Sun, 29 Mar 2020 10:40:20 GMT
focusdroid: python
Server: Werkzeug/0.12.2 Python/2.7.17

# 2. 使用make_response 来构造信息(来自flask)
    resp = make_response('index page2')
    resp.status = '888 itcast'
    resp.headers['city'] = '中国上海市'
    return resp

### 字典转字符串
import json
data = {
        "name": "focusdroid",
        "age": 18
    }
json_str = json.dumps(data) # 转成字符串

dict_dic = json.loads(json_str) # 将json转成字典

# 2. 使用flask的jsonify
jsonify(data)
```

## cookie和session的使用
```
@app.route('/set_cookie')
def set_cookie():
    resp = make_response('success')
    # 设置cookie, 默认有效期是临时cookie，浏览器关闭就失效
    resp.set_cookie('name', '王旭')
    resp.set_cookie('age', '26')
    # max_age设置有效期， 单位 秒
    resp.set_cookie('city', 'xi;an', max_age=3600)
    return resp

@app.route('/get_cookie')
def get_cookie():
    name = request.cookies.get('name')
    age = request.cookies.get('age')
    city = request.cookies.get('city')
    data = {
        'name': name,
        'age': age,
        'city': city
    }
    json_str = json.dumps(data)
    return json_str


@app.route('/del_cookie')
def del_cookie():
    resp = make_response('del success')
    # 删除cookie
    resp.delete_cookie('name')
    return resp


### session

session_dict = {
    '1': {},
    '2': {}
}

app = Flask(__name__)

# falsk的session需要用到的秘钥字符串（必须设置） secrt_key
app.config['SECRET_KEY'] = 'aeebtaefgbagfbaefb'

# flask默认把数据保存到cookie中


@app.route('/login')
def login():
    global session_dict
    session_dict['1'] = '全局保存1'
    # 设置session数据
    session['name'] = 'python'
    session['mobile'] = '15701229789'
    return 'login success'

@app.route('/index')
def index():
    # 获取session数据
    name = session.get('name')
    # mobile = session.get('mobile')
    return 'hello %s ' % name

```

## 函数钩子
```

@app.route('/hello')
def hello():
    print('hello 被执行')
    return 'hello page'

@app.before_first_request
def handle_before_first_request():
    '''在第一次请求处理之前先被执行'''
    print('handle_before_first_request 被执行')

@app.before_request
def handle_before_request():
    '''在每次请求之前被执行'''
    print('handle_before_request 被执行')

@app.after_request
def handle_after_request(response):
    '''在每次请求（视图函数处理）之后都被执行，前提是视图函数没有出现异常'''
    print('handle_after_request 被执行')
    return response

@app.teardown_request
def handle_teardown_request(response):
    '''在每次请求（视图函数处理）之后都被执行，无论视图函数是否出现异常，都被执行，工作在非调试模式是 debug=Flase'''
    return response

结论：
handle_before_first_request 被执行
handle_before_request 被执行
handle_after_request 被执行

```
## 请求上下文和应用上下文
```

```

## Flask-script扩展命令行
```
# coding:utf-8

from flask import Flask, request, current_app
from flask_script import Manager # 启动命令的管理类

app = Flask(__name__)

# 创建Manager管理对象
manager = Manager(app)



@app.route('/index')
def index():
    return 'index page'



if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=3000, debug=True)
    # 通过管理对象启动flask
    manager.run()

# 启动在虚拟环境中这样使用
python 10flaks_script runserver -h 0.0.0.0 -p 3000
```

## 数据库设置
```
falsk-SQLAlchemy数据库
数据库安装
sudo apt-get install mysql-server
sudo apt-get install mysql-client

sudo apt-get install libmysqlclient-dev

 

在falsk安装数据库
pip install falsk-sqlalchmy

要连接mysql数据库，仍需要安装falsk-mysqldb
pip install flask-mysqldb
```
##  在flask中使用sql语句
```

In [2]: Role.query.all()
Out[2]: [<db_demo.Role at 0x7fb78d1d17d0>, <db_demo.Role at 0x7fb78d1d1890>]

In [3]: li = Role.query.all()

In [4]: r = li[0]

In [5]: r
Out[5]: <db_demo.Role at 0x7fb78d1d17d0>

In [6]: type(r)
Out[6]: db_demo.Role

In [7]: r.name
Out[7]: u'admin'


In [12]: r = Role.query.first()

In [13]: r.name
Out[13]: u'admin'

# 传一个主键的值
In [14]: r = Role.query.get(2)

In [15]: r.name
Out[15]: u'focusdroid'


##　另外一种查询方式
In [18]: db.session.query(Role).all()
Out[18]: [<db_demo.Role at 0x7fb78d1d17d0>, <db_demo.Role at 0x7fb78d1d1890>]

In [19]: db.session.query(Role).get(2)
Out[19]: <db_demo.Role at 0x7fb78d1d1890>

In [20]: db.session.query(Role).first()
Out[20]: <db_demo.Role at 0x7fb78d1d17d0>


＃＃＃　过滤器
In [22]: User.query.filter_by(name='tree')
Out[22]: <flask_sqlalchemy.BaseQuery at 0x7fb78d107cd0>

In [23]: User.query.filter_by(name='tree').all()
Out[23]: [<db_demo.User at 0x7fb78d118490>]

In [24]: User.query.filter_by(name='tree').first()
Out[24]: <db_demo.User at 0x7fb78d118490>

In [25]: user = User.query.filter_by(name='tree').first()

In [26]: user.name
Out[26]: u'tree'

In [27]: user.email
Out[27]: u'tree@163.com'

##### 过滤器方法
＃＃＃＃＃ 
filter()     把过滤器添加到原查询上，返回一个新查询
filter_by()　把等值过滤器添加到原查询，上，返回一个新查询
limit()　　　　使用指定的值限定查询返回的结果
offset()　　　偏移原查询返回的结果，返回一个新查询
order_by()　　根据指定条件对原查询结果进行排序，但会一个新查询
group_by()　　根据指定条件对原查询结果进行分组，返回一个新查询

### 过滤器中的完成方法filter()
In [41]: user = User.query.filter(User.name=='tree', User.role_id==1).first()

In [42]: user.name
Out[42]: u'tree'

In [43]: user.email
Out[43]: u'tree@163.com'

》》》　如果是使用all(),即使一些这种形式
In [46]: user = User.query.filter(User.name=='tree', User.role_id==1).all()

In [47]: user[0]
Out[47]: <db_demo.User at 0x7fb78d118490>

In [48]: u = user[0]

In [49]: u.name
Out[49]: u'tree'

In [50]: u.email
Out[50]: u'tree@163.com'

### sql查询中的　或　
In [52]: from sqlalchemy import or_

In [53]: User.query.filter(or_(User.name=='tree', User.email.endswith('163.com'))).all()
Out[53]: 
[<db_demo.User at 0x7fb78d118490>,
 <db_demo.User at 0x7fb78d1448d0>,
 <db_demo.User at 0x7fb78d144c10>]

In [54]: li = User.query.filter(or_(User.name=='tree', User.email.endswith('163.com'))).all()

In [55]: li[0].name
Out[55]: u'tree'

In [56]: li[2].name
Out[56]: u'\u663e\u793a'

In [57]: li[3].name
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)
<ipython-input-57-57e9e5e9f016> in <module>()
----> 1 li[3].name

IndexError: list index out of range

In [58]: li[1].name
Out[58]: u'focus'

＃＃＃　offset()偏移　　跳过几条

In [60]: User.query.offset(2).all()
Out[60]: [<db_demo.User at 0x7fb78d12f990>, <db_demo.User at 0x7fb78d144c10>]

In [61]: li = User.query.offset(2).all()

In [62]: li[0].name
Out[62]: u'\u5317\u4eac\u5e02'

In [63]: li[1].name
Out[63]: u'\u663e\u793a'

跳过一条，取出两条
In [66]: li = User.query.offset(1).limit(2).all()

In [67]: li
Out[67]: [<db_demo.User at 0x7fb78d1448d0>, <db_demo.User at 0x7fb78d12f990>]

In [68]: li[0].email
Out[68]: u'focus@163.com'

In [69]: li[1].email
Out[69]: u'beijing@126.com'


＃＃＃　排序order_by()
In [76]: User.query.order_by(User.id.desc()).all()
Out[76]: 
[<db_demo.User at 0x7fb78d144c10>,
 <db_demo.User at 0x7fb78d12f990>,
 <db_demo.User at 0x7fb78d1448d0>,
 <db_demo.User at 0x7fb78d118490>]

In [77]: li = User.query.order_by(User.id.desc()).all()

In [78]: li[0].email
Out[78]: u'asmie@163.com'

In [79]: li[1].email
Out[79]: u'beijing@126.com'

In [80]: li[2].email
Out[80]: u'focus@163.com'


## 分组group_by()
In [84]: from sqlalchemy import func

In [85]: db.session.query(User.role_id, func.count(User.role_id)).group_by(User.role_id)
Out[85]: <flask_sqlalchemy.BaseQuery at 0x7fb78d128390>

In [86]: db.session.query(User.role_id, func.count(User.role_id)).group_by(User.role_id).all()
Out[86]: [(1, 2), (2, 2)]


```
## 查询之后信息显示
```
class User(db.Model):
    '''用户表'''
    __tablename__ = 'tbl_users' # 指明数据库表名

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    email = db.Column(db.String(128), unique=True)
    password = db.Column(db.String(128))
    role_id = db.Column(db.Integer, db.ForeignKey('tbl_roles.id'))

    def __repr__(self):
        return 'User object: name=%s'% self.name

In [4]: User.query.get(1)
Out[4]: User object: name=tree


```
## 数据库的修改和删除
```
In [5]: user = User.query.get(1)

In [6]: user.name
Out[6]: u'tree'

In [7]: user.name = 'trees'

In [8]: user.name
Out[8]: 'trees'

>>>>>> 在数据库中修改
In [9]: db.session.add(user)

In [10]: db.session.commit()
＃＃＃＃　更新方法
In [13]: User.query.filter_by(name='focus').update({'name':'focusdroidss'})
Out[13]: 1L

In [14]: db.session.commit()


＃＃＃＃＃　删除方法
In [15]: user = User.query.get(3)

In [16]: db.session.delete(user)

In [17]: db.session.commit()
mysql> select * from tbl_users;
+----+--------------+-----------------+-------------+---------+
| id | name         | email           | password    | role_id |
+----+--------------+-----------------+-------------+---------+
|  1 | trees        | tree@163.com    | tree1234    |       1 |
|  2 | focusdroidss | focus@163.com   | focus1234   |       2 |
|  3 | 北京市       | beijing@126.com | beijing1234 |       1 |
|  4 | 显示         | asmie@163.com   | asmie1234   |       2 |
+----+--------------+-----------------+-------------+---------+
4 rows in set (0.00 sec)

mysql> select * from tbl_users;
+----+--------------+---------------+-----------+---------+
| id | name         | email         | password  | role_id |
+----+--------------+---------------+-----------+---------+
|  1 | trees        | tree@163.com  | tree1234  |       1 |
|  2 | focusdroidss | focus@163.com | focus1234 |       2 |
|  4 | 显示         | asmie@163.com | asmie1234 |       2 |
+----+--------------+---------------+-----------+---------+



```
##　数据库迁移
```
pip install flask-migrate

database.py

初始化
python database.py db init

执行，　创建自动迁移脚本
 python database.py db migrate
# python database.py db migrate -m 'add mobile'  # 添加ｈｉｓｔｏｒｙ信息


INFO  [alembic.runtime.migration] Context impl MySQLImpl.
INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
INFO  [alembic.env] No changes in schema detected.


# 添加新字段之后，更新数据库
python database.py  db upgrade


＃ 降级
 python database.py db history # 查询历史的字段添加
61fe446d96f3 -> 5a00875d9eb8 (head), add mobile
<base> -> 61fe446d96f3, empty message


python database.py db downgrade 61fe446d96f3
降级为　61fe446d96f3　状态
```
## 发邮件操作
```
pip install flask-mail



```


































