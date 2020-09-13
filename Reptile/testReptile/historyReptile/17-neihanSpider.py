# -*- coding:utf-8 -*-
import requests
import re
import json

class Neihan:
    def __init__(self):
        self.start_url = "http://www.neihanshequ.com/"
        self.start_url_temp = "http://neihansshuqu.com/joke/?js_json=1&app_name=neihanshequ_web&max_time={}"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"
        }

    def parse_url(self, url): # 发送请求
        res = requests.get(url, headers=self.headers)
        return res.content.decode()

    def get_first_page_content_list(self, html_str):
        content_list = re.findall(r"<p>(.*?)</p>", html_str, re.S)
        print(content_list)
        return content_list

    def save_content_list(self, content_list):
        with open("neihan.txt", "a", encode="utf-8") as f:
            for content in content_list:
                f.write(json.dumps(content, ensure_ascii=False))
        print("构造下一页的url地址")

    def get_content_list(self, json_str): # 提取从第二页开始的数据
        dict_ret = json.loads(json_str)
        data = dict_ret["data"]["data"]
        content_list = [i["group"]["content"] for i in data]
        max_time = dict_ret["data"]["max_time"]
        return content_list, max_time



    def run(self):
        # 1.  start_url
        # 2. 发送请求
        html_str = self.parse_url(self.start_url)
        # 3. 提取数据
        content_list, max_time = self.get_first_page_content_list(html_str)
        # 4. 保存
        self.save_content_list(content_list)
        # 5. 构造下一页的url地址
        while True:
            next_url = self.start_url_temp.format(max_time)
            # 6. 发送请求，获取响应
            json_str = self.parse_url(next_url)
            # 7. 提取数据，提取max_time
            content_list = self.get_content_list(json_str)
            # 8. 保存
            self.save_content_list(content_list)
            # 9. 循环５-８步
            next_url = self.start_url_temp.format(max_time)



if __name__ == "__main__":
    neihan = Neihan()
    neihan.run()