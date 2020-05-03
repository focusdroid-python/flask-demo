# coding:utf-8

from flask import Flask, request, session


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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)