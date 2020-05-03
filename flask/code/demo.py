# coding:utf-8

from flask import Flask, current_app, redirect, url_for

# 创建flask应用
# __name__表示当前模块的名字
app = Flask(__name__)

@app.route('/')
def index():
    '''定义视图函数'''
    return 'Hello flask'

@app.route('/post_only', methods=['POST', 'GET'])
def post_only():
    return 'post only page'


@app.route('/hello')
def hello():
    return 'hello 1'

@app.route('/hello')
def hello2():
    return 'hello 2'

@app.route('/hi1')
@app.route('/hi2')
def hi():
    return 'hi'

@app.route('/login')
def login():
    url = url_for('index')
    return redirect(url)



if __name__ == '__main__':
    # app启动
    print(app.url_map)
    app.run(host='0.0.0.0', port=3000, debug=True)