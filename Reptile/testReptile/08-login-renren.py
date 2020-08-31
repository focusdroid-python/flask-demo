# -*- coding:utf-8 -*-

import requests

session = requests.session()
post_url = "http://www.renren.com/PLogin.do"
post_data = {"email":"mr_mao_hacker@163.com", "password":"alarmchime"}
headers = {
    "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"
}

# 使用session发送请求，cookie保存在其中
session.post(post_url, data=post_data, headers=headers)

# 在使用session进行请求登陆之后才能访问的地址
res = session.get("http://www.renren.com/327550029/profile", headers=headers)


print(res)

# 保存页面w
with open("renren1.html", "w", encoding="utf-8") as f:
    f.write(res.content.decode())
