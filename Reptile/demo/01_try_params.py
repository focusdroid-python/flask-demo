import requests

headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36"}
# p = {"wd": "王旭"}
# url = "http://www.baidu.com"
#
# response = requests.get(url, headers = headers, params=p)
# print(response.content.decode())
# print(response.request.url)

url = "https://www.baidu.com?wd={}".format('王旭')
res = requests.get(url, headers=headers)

print(res.status_code)
print(res.request.url)