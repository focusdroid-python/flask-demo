import requests


response = requests.get("https://www.baidu.com/img/dong_f6764cd1911fae7d460b25e31c7e342c.gif")

with open("a.gif", "wb") as f:
    f.write(response.content)