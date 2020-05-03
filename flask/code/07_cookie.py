# coding:utf-8

from flask import Flask, make_response, request
import json

app = Flask(__name__)

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



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)