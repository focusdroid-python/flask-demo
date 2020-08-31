# -*- coding:utf-8 -*-
import requests

proxies = {
    "http":"114.230.126.112:14398",
    "https":"114.230.126.112:14398"
}

headers = {
    "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"
}

res = requests.get("https://www.baidu.com", proxies=proxies,headers=headers)
print(res.status_code)