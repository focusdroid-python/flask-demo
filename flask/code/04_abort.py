# coding:utf-8

from flask import Flask, request, abort

app = Flask(__name__)

@app.route('/login', methods=['GET'])
def login():
    # name = request.form.get('name')
    # pwd = request.form.get('password')
    name = ''
    pwd = ''
    if name != 'admin' and pwd != 'admin':
        # 使用abort函数可以立即终止视图函数的执行并可以返回给前端特定的信息
        abort(666)
    return 'login success'


@app.errorhandler(400)
def hangle_404_err(err):
    '''定义错误处理方法'''
    #  这个函数的返回值会是前端用欧冠胡看到的最终结果
    return '出现了404错误信息，错误信息%s ' % err



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)