# coding:utf-8

from . import api
from ihome.utils.common import login_required
from ihome.modules import Order
from flask import g, jsonify, current_app, request
from ihome.utils.response_code import RET
from alipay import AliPay
from ihome import constants, db
import os


@api.route("/orders/<int:order_id>/payment", methods=["POST"])
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

    # 构建让用户跳转的支付链接地址
    pay_url = constants.ALIPAY_URL_PREFIX + order_string
    return jsonify(error=RET.OK, errmsg="ok", data={"pay_url": pay_url})

def save_order_payment_result():
    """保存订单支付结果"""
    alipay_dict = request.form.to_dict()

    # 对支付宝的数据进行分离，提取出支付宝的签名参数sign和剩下的其他数据
    alipay_sign = alipay_dict.pop("sign")

    # 创建支付宝sdk的工具对象
    alipay_client = AliPay(
        appid="2016102100731698", # 沙箱环境的appid
        app_notify_url=None,  # 默认回调url
        app_private_key_string=os.path.join(os.path.dirname(__file__), "keys/app_private_key.pem"), # 私钥
        # 支付宝的公钥，验证支付宝回传消息使用，不是你自己的公钥,
        alipay_public_key_string=os.path.join(os.path.dirname(__file__), "keys/alipay_public_key.pem"), # 支付宝公钥,
        sign_type="RSA2",  # RSA 或者 RSA2
        debug = True  # 默认False
    )

    # 借助工具验证参数的合法性
    # 如果确定参数是支付宝的，返回True,否则返回Flase
    result = alipay_client.verify(alipay_dict, alipay_sign)

    if result:
        # 修改数据库的订单状态
        order_id = alipay_dict.get("out_trade_no")
        trade_no = alipay_dict.get("trade_no")

        try:
            Order.query.filter_by(id=order_id).update({"status":"WAIT_COMMENT", "trade_no":trade_no})
            db.session.commit()
        except Exception as e:
            current_app.logger.error(e)
            db.session.rollback

    return jsonify(error=RET.OK, errmsg="ok")

