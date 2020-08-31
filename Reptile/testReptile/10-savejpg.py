# -*- coding:utf-8 -*-
import requests


# 发送请求
res = requests.get("https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1598700123689&di=6de826e8057524cb6f6a622410ba8a3e&imgtype=0&src=http%3A%2F%2Fpic1.win4000.com%2Fpic%2F7%2F50%2Fa3b8291036.jpg")

# 保存
with open("a.jpg", "wb") as f:
    f.write(res.content)

