# -*- coding:utf-8 -*-

import requests


class TiebaSpider:
    def __init__(self, tieba_name):
        self.tieba_name = tieba_name
        self.url_temp = "https://tieba.baidu.com/f?kw="+tieba_name+"&ie=utf-8&pn={}"
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"}

    def get_utl_list(self):
        '''构造url列表'''
        url_list = []
        for i in range(1000):
            url_list.append(self.url_temp.format(i*50))
        return url_list

    def parse_url(self, url):
        '''发送请求，获取响应'''
        print(url)
        res = requests.get(url, headers=self.headers)
        return res.content.decode()

    def save_html(self, html_str, page_num):
        '''保存html字符串'''
        file_path = "{}-第{}页.html".format(self.tieba_name, page_num)
        with open(file_path, 'w', encoding="utf-8") as f:
            f.write(html_str)

    def run(self):
        """实现贴吧逻辑"""
        # 1. 构造url列表
        url_list = self.get_utl_list()
        # ２.　遍历,发送请求，获取响应
        for url in url_list:
            html_str = self.parse_url(url)

            # 3.　保存
            page_num = url_list.index(url)+1
            self.save_html(html_str, page_num)


if __name__ == '__main__':
    tieba_spider = TiebaSpider("李毅")
    tieba_spider.run()