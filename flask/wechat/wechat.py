# coding:utf-8

from flask import Flask, request, abort, render_template
import hashlib
import xmltodict
import time
import urllib2
import json

#　常量
# 微信token令牌
WECHAT_TOKEN = "focus"

app = Flask(__name__)

@app.route("/wechat8000", methods=['GET','POST'])
def wechat():
    """对接微信服务器"""
    # 接受微信服务器发送的参数
    signature = request.args.get("signature")
    timestamp = request.args.get("timestamp")
    nonce = request.args.get("nonce")

    # 校验参数
    if not all([signature, timestamp, nonce]):
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
        # 表示微信发送的请求
        if request.method == 'GET':
            # 表示第一次接入微信服务器验证
            echostr = request.args.get('echostr')
            if not echostr:
                abort(400)
            return echostr
        elif request.method == 'POST':
            # 表示微信服务器转发消息过来
            xml_str = request.data
            # 对xml字符串进行解析
            xml_str = xmltodict.parse(xml_str)

            # 对xml字符串进行解析
            xml_dict = xmltodict.parse(xml_str)
            xml_doct = xml_dict.get('xml')

            # 提取消息类型
            msg_type = xml_dict.get('MsgType')

            if msg_type == 'text':
                # 文本消息
                # 构造返回值，经由微信服务器回复给用户的消息
                resp_dict = {
                    'xml': {
                        'ToUserName': xml_dict.get('FormUserName'),
                        'FormUserName': xml_dict.get('ToUserName'),
                        'CreateTime': int(time.time()),
                        'MsgType': 'text',
                        'Content': xml_dict.get('Content')
                    }
                }
            else:
                resp_dict = {
                    'xml': {
                        'ToUserName': xml_dict.get('FormUserName'),
                        'FormUserName': xml_dict.get('ToUserName'),
                        'CreateTime': int(time.time()),
                        'MsgType': 'text',
                        'Content': 'focusdroid'
                    }
                }
            # 讲字典转换为xml字符串
            resp_xml_str = xmltodict.unparse(resp_dict)
            # 将消息数据给微信服务器
            return resp_xml_str

@app.route("/wechat8000/index")
def index():
    '''让用户通过微信访问网页页面视图'''
    # 从微信服务器中哪用户的资料数据
    # １．　拿去code参数
    code = request.args.get("code")
    if not code:
        return u"缺失code参数"

    # 2.向微信服务器发送http请求，获取access_token
    url = ""     # 微信获取access_token的链接进行拼接

    # 使用urllib2中的ｕｒｌｏｐｅｎ发送骑牛
    # 如果只传网址url参数，则默认使用http的get请求方式，返回响应对象
    response = urllib2.urlopen(url)

    # 获取响应体中的数据，微信返回json数据
    json_str = response.read()
    resp_dict = json.loads(json_str)

    # 提取access_token
    if 'errcode' in resp_dict:
        return u'获取access_token失败'

    access_token = resp_dict.get('access_token')
    open_id = resp_dict.get('openid')

    # 3. 像微信服务器发送http请求，获取用户的资料数据
    url = 'https://api.weixin.qq.com/sns/userinfo?access_token=%s&openid=%s&lang=zh_CN'%(access_token, open_id)

    response = urllib2.urlopen(url)

    # 读取微信传回的json的响应体数据
    user_json_str = response.read()
    user_dict_data = json.loads(user_json_str)

    if 'errcode' in user_dict_data:
        return '获取用户信息失败'




    # 将用户页面填充到页面中
    return render_template('index.html', user=user_dict_data)


if __name__ == "__main__":
    app.run(port=8000, debug=True)