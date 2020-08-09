import requests

session = requests.session()

headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36"}
post_url = "http://www.renren.com/api/callback"
# post_data = {"email":"mr_mao_hacker@163.com", "password":"alarmchime"}
post_data = {
    "code": "071fs4oy1H9DGb0uQQny1cz2oy1fs4o5",
    "state": "eyJzcmMiOiJ3eCJ9"
}

# 使用session发送post请求，cookie保存在其中
res = session.get(post_url, data=post_data, headers=headers)
# print(res.content)

# 保存页面
with open("renren.html", "w", encoding="utf-8") as f:
    f.write(res.content.decode())

# session进行请求登录之后才能访问的地址
# session.get("", headers=headers)