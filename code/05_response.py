# coding:utf-8

from flask import Flask, request, abort, Response, make_response

app = Flask(__name__)

@app.route('/index')
def index():
    #1. 使用元祖，返回自定义的响应信息
    #       响应体         状态码  响应头
    # return 'index page', 400, [('focusdroid', 'python'), ('city', 'name')]
    # return 'index page2', 400, {'name':'王旭', 'age':30}
    # return 'index page2', '666 itcast status', {'name':'王旭', 'age':30}


    # 2. 使用make_response 来构造信息
    resp = make_response('index page2')
    resp.status = '888 itcast'
    resp.headers['city'] = '中国上海市'
    return resp



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)