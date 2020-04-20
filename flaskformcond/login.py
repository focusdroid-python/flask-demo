#coding:utf-8

from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/login', methods=['POST'])
def login():
    # 接收参数
    user_name = request.form.get('user_name')
    password = request.form.get('password')
    # 参数判断
    if not all([user_name, password]):
        res = {
            'code': 1,
            'message': 'invalid params'
        }
        return jsonify(res)
    if user_name == 'admin' and password == 'python':
        res = {
            'code': 200,
            'message': 'login success'
        }
        return jsonify(res)
    else:
        res = {
            'code': 2,
            'message': 'warning username or password'
        }
        return jsonify(res)


    # 决定返回值

if __name__ == '__main__':
    app.run(debug=True)