# coding:utf-8

from . import api
from ihome.utils.commons import login_required
from ihome.models import Order
from flask import g, jsonify, current_app
from ihome.utils.response_code import RET
from alipay import AliPay
import os


@api.route("/ordres/<int:order_id>/payment", methods=["POST"])
@login_required
def order_pay(order_id):
    """发起支付宝支付"""

    user_id = g.user_id
    # 判断订单状态
    try:
        order = Order.query.filter(Order.id == order_id, Order.user_id==user_id, Order.status == "WAIT_PAYMENT").first()
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(error=RET.PARAMERR, errmsg="数据库异常")

    if order is None:
        return jsonify(error=RET.NODATA, errmsg="订单数据异常")


    # 创建支付宝sdk的工具对象
    alipay = AliPay(
        appid="2016102100731698", # 沙箱环境的appid
        app_notify_url=None,  # 默认回调url
        app_private_key_string=os.path.join(os.path.dirname(__file__), "keys/app_private_key.pem"), # 私钥
        # 支付宝的公钥，验证支付宝回传消息使用，不是你自己的公钥,
        alipay_public_key_string=os.path.join(os.path.dirname(__file__), "keys/alipay_public_key.pem"), # 支付宝公钥,
        sign_type="RSA2",  # RSA 或者 RSA2
        debug = True  # 默认False
    )

    # 手机网站支付，需要跳转到https://openapi.alipay.com/gateway.do? + order_string
    order_string = alipay.api_alipay_trade_wap_pay(
        out_trade_no="20161112", # 订单编号
        total_amount=str(order.amount / 100.0), # 总金额
        subject=u"爱我家租房　%s" % order.id, # 订单标题
        return_url="http://127.0.0.1:5000/", # 返回的连接地址
        notify_url=None  # 可选, 不填则使用默认notify url
    )

