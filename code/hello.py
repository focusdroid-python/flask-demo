# coding:utf-8

from flask import Flask, current_app

# 创建flask应用
# __name__表示当前模块的名字
app = Flask(
    __name__,
    static_url_path='/python')

# 配置参数的使用方式
# 1, 使用配置文件
# app.config.from_pyfile('config.cfg')
# 2.
class Config(object):
    DEBUG = True
    NAME = 'focusdroid'

app.config.from_object(Config)

# 3.
# app.config['DEBUG'] = True

@app.route('/')
def index():
    '''定义视图函数'''
    # 获取配置参数
    # 1. 直接从全局对象中app的config字典中取值
    # print(app.config.get('NAME'))
    # 2. 通过倒入的currentapp
    print(current_app.config.get('NAME'))
    return 'Hello flask'

if __name__ == '__main__':
    # app启动
    app.run(host='0.0.0.0', port=3000, debug=True)