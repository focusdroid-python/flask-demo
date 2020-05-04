import requests

headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36"}


data = {
    "from": "zh",
    "to": "en",
    "query": "爬虫",
    "transtype": "translang",
    "simple_means_flag": "3",
    "sign": "253813.474180",
    "token": "4df0e2d73753ea261214fad1ba5fcbb7",
    "domain": "common"
}
post_url = "https://fanyi.baidu.com/v2transapi?from=zh&to=en"

res = requests.post(post_url, data=data, headers=headers)
print(res.content.decode())