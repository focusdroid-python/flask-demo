# coding:utf-8

from flask import Flask
# 第二种方法
from goods import get_goods
from user import register

from orders import app_orders
from cart import app_cart

app = Flask(__name__)

# 第二种方法
app.route('/get_goods')(get_goods)
app.route('/register')(register)

# 注册蓝图
# app.register_blueprint(app_orders) #　Map([<Rule '/get_orders' (HEAD, OPTIONS, GET) -> app_orders.get_orders>,
app.register_blueprint(app_orders, url_prefix='/orders') # 添加前缀　Map([<Rule '/orders/get_orders' (HEAD, OPTIONS, GET) -> app_orders.get_orders>,
app.register_blueprint(app_cart, url_prefix='/cart')


@app.route('/')
def index():
    # 循环引入，解决办法推迟一方的导入，让另一方先完成
    # from user import register
    # from goods import get_goods
    return 'index page'

if __name__ == '__main__':
    print(app.url_map)
    app.run(debug=True)