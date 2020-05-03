# coding:utf-8

from flask import Flask, request

app = Flask(__name__)

app.route('/index', method=['POST', 'GET'])
def index():
    # request中包含前端发送过来的所有的请求数据
    # 通过request.form可以直接提取请求体中的表单格式的数据，是一个类字典的对象
    name = request.form.get('name')
    age = request.form.get('age')
    print(request)
    return 'hello name=%s, age=%s'% (name, age)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)