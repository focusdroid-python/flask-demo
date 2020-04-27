# coding:utf-8

from flask import Flask, request, abort
import hashlib

#　常量
# 微信token令牌
WECHAT_TOKEN = "focus"

app = Flask(__name__)

@app.route("/wechat8000")
def wechat():
    """对接微信服务器"""
    # 接受微信服务器发送的参数
    signature = request.args.get("signature")
    timestamp = request.args.get("timestamp")
    nonce = request.args.get("nonce")
    echostr = request.args.get("echostr")

    # 校验参数
    if not all([signature, timestamp, nonce, echostr]):
        abort(400)

    # 按照微信的流程进行计算签名
    li = [WECHAT_TOKEN, timestamp, nonce]

    # 排序
    li.sort()

    #　拼接字符串
    temp_str = "".join(li)

    # 进行sha1加密, 因为获取到的是一个对象，所以使用hexdigest进行获取签名
    sign = hashlib.sha1(temp_str).hexdigest()

    # 与请求的计算签名值与请求的签名参数进行对比，如果相同，则证明请请求来自微信
    if signature != sign:
        #　表示请求不是微信的
        abort(403)
    else:
        return echostr


if __name__ == "__main__":
    app.run(port=8000, debug=True)