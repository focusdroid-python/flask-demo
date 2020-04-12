# coding:utf-8


from flask import Flask, request, make_response, abort, jsonify
import json

app = Flask(__name__)

@app.route('/index')
def index():
    # json就是字符串
    data = {
        "name": "focusdroid",
        "age": 30
    }
    # json_str = json.dumps(data)  # 转成字符串
    # dict_dic = json.loads(json_str)  # 将json转成字典

    # json_str = json.dumps(data)
    # return json_str, 200, {'Content-Type':'application/json'}

    # return jsonify(data)
    return jsonify(city='beijingshi', country='china')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)