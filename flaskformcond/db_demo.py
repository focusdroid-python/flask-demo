# coding:utf-8

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

class Config(object):
    '''配置参数'''
    # sqlalchemy的配置参数
    SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3306/db_python04"
    # 设置sqlalchemy自动更新跟踪数据库
    SQLALCHEMY_TRACK_MODIFICATIONS = True

app.config.from_object(Config)

# 创建数据库sqlalchemy工具对象
db = SQLAlchemy(app)

# ihome -> ih_user  数据库名缩写——表名
# tbl_user tbl_表名

class Role(db.Model):
    '''用户角色、身份表'''
    __tablename__ = 'tbl_roles'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique=True)
    users = db.relationship('User', backref='role')

    def __repr__(self):
        '''定义之后，可以让显示对象的时候更直观'''
        return 'Role object: name=%s'% self.name

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



@app.route('/')
def index():
    return 'index page'



if __name__ == '__main__':
    # 清除数据库里所有的数据
    db.drop_all()

    # 创建所有的表
    db.create_all()

    # 创建对象
    role1 = Role(name='admin')
    # session记录对象任务
    db.session.add(role1)
    # 提交任务到数据库
    db.session.commit()

    role2 = Role(name='focusdroid')
    db.session.add(role2)
    db.session.commit()


    us1 = User(name='tree', email='tree@163.com', password='tree1234', role_id=role1.id)
    us2 = User(name='focus', email='focus@163.com', password='focus1234', role_id=role2.id)
    us3 = User(name='北京市', email='beijing@126.com', password='beijing1234', role_id=role1.id)
    us4 = User(name='显示', email='asmie@163.com', password='asmie1234', role_id=role2.id)

    # 一次保存多条数据
    db.session.add_all([us1, us2, us3, us4])
    db.session.commit()

