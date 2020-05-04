import requests

headers = {
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1"
}


data1 = {
"query": "爬虫"
}

first_url = "https://fanyi.baidu.com/langdetect"

res1 = requests.post(first_url, data=data1,headers=headers)
print(res1.content.decode())


data = {
    "query": "爬虫",
    "from": "zh",
    "to": "en",
    "token": "4df0e2d73753ea261214fad1ba5fcbb7",
    "sign": "253813.474180"
}

post_url = "https://fanyi.baidu.com/basetrans"

response = requests.post(post_url, data=data, headers=headers)
print(response.content.decode("unicode-escape"))
print('end')