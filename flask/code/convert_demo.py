# coding:utf-8

from flask import Flask, current_app, redirect, url_for
from werkzeug.routing import BaseConverter
# 创建flask应用
# __name__表示当前模块的名字
app = Flask(__name__)

# 转换器
# @app.route('/goods/<int:goods_id>') # 数字类型
@app.route('/goods/<int:id>')
def goods_detail(id):
    '''定义视图函数'''
    print(id)
    return 'goods detail page'

# 1. 定义自己的转换器
class MobileConverter(BaseConverter):
    def __init__(self, url_map):
        super(MobileConverter, self).__init__(url_map)
        self.regex = r'1[3478]\d{9}'
# 11
app.url_map.converters['mobile'] = MobileConverter


# 12定义自己的转换器
class RegexConverter(BaseConverter):
    ''''''
    def __init__(self, url_map, regex):
        # 调用父类的初始化方法
        super(RegexConverter, self).__init__(url_map)
        # 将正则表达式的参数保存到对象的属性中，falsk会去使用这个属性进行路由的正则匹配
        self.regex = regex

    def to_python(self, value):
        ''''''
        print('python方法被调用')
        print(value)
        return value


    def to_url(self, value):
        '''url_for的方法被调用'''
        print('url方法被调用%s'%value)
        return '15702222222'



# 12. 将自定义转换器添加到flask应用中
app.url_map.converters['re'] = RegexConverter

@app.route('/send/<re(r"1[3478]\d{9}"):mobile>')
def send_sms(mobile):
    return 'send sms to %s' % mobile
# @app.route('/send/<mobile:mobile_num>')
# def send_sms(mobile_num):
#     return 'send sms to %s' % mobile_num

@app.route('/index')
def index():
    url = url_for('send_sms', mobile_num='15702222222')
    return redirect(url)


# @app.route('/call/<re(r""):tel>')
# def call_tel():


if __name__ == '__main__':
    # app启动
    print(app.url_map)
    app.run(host='0.0.0.0', port=3000, debug=True)