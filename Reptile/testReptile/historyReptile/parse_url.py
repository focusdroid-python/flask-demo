# -*- coding:utf-8 -*-

import requests
# from retrying import retry

headers = {
"User-Agent":"Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Mobile Safari/537.36"
}

# @retry(stop_max_attempt_number=3)
def _parse_url(url, methods, data, proxies):
    print("*"*30)
    if methods =="POST":
        response = requests.post(url, data=data,headers=headers, proxies=proxies)
    else:
        response = requests.post(url, headers=headers, proxies=proxies, timeout=3)

    assert response.status_code == 200
    return response.content.decode()


def parse_url(url, methods='GET', data=None, proxies={}):
    try:
        html_str = _parse_url(url, methods, data, proxies)
    except:
        html_str = None

    return html_str


if __name__ == "__main__":
    url = "www.baidu.com"
    print(_parse_url(url))
