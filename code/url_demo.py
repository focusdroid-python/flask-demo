# coding:utf-8

from flask import Flask, redirect, url_for
# 创建flask应用
# __name__表示当前模块的名字
app = Flask(__name__)

# 转换器
# @app.route('/goods/<int:goods_id>') # 数字类型
@app.route('/')
def index():
    '''定义视图函数'''
    return 'Hello Flask'

@app.route('/post_only', methods=['POST', 'GET'])
def poet_only():
    return 'index222'

@app.route('/hello', methods=['GET'])
def hello():
    return 'hello'

@app.route('/hello', methods=['POST'])
def hello2():
    return 'hello2'

@app.route('/hi')
@app.route('/hi2')
def hi():
    return 'hi hi hi'

@app.route('/login')
def login():
    #url = '/'
    url = url_for('index') # 在括号中写视图的名字
    return redirect(url)


if __name__ == '__main__':
    # app启动
    print(app.url_map)
    app.run(host='0.0.0.0', port=3000, debug=True)