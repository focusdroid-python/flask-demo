# coding:utf-8

import requests

headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"}

# params = {"wd": "传智播客"}
#
# url_temp = "https://www.baidu.com/s?"
#
#
# res = requests.get(url_temp, headers=headers, params=params)
#
#
# print(res.status_code)
# print(res.request.url)
# print(res.request.path_url)

url = "https://www.baidu.com/s?wd={}".format("传智播客")

res = requests.\
    get(url, headers=headers)

print(res.status_code)
print(res.request.url)
print(res.request.path_url)