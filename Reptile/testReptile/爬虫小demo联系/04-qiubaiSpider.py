# -*- coding:utf-8 -*-
import requests
from lxml import etree

class QiubaiSpider:
    def __init__(self):
        self.start_url = "https://www.qiushibaike.com/8hr/page/{}/"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"
        }


    def get_url_list(self):
        return [self.start_url.format(i) for i in range(1, 2)]

    def get_parse(self, url): # 发送请求，获取数据
        response = requests.get(url, headers=self.headers)
        return response.content.decode()

    def get_content_list(self, html_str):
        html = etree.HTML(html_str)

        div_list = html.xpath("//div[@class='recommend-article']/ul")
        content_list = []
        for div in div_list:
            item = {}
            item["title"] = div.xpath("./li/div/a/text()")
            item["title"] = self.get_all_title(item["title"], {}, "title")
            item["author"] = div.xpath(".//span[@class='recmd-name']/text()")
            item["author"] = self.get_all_title(item["author"], {}, "author")

            content_list.append(item)
        return content_list

    def get_all_title(self, all_title, list_name, attr_name):
        d_list = []
        for i in all_title:
            list_name = {}
            list_name[attr_name] = i

            d_list.append(list_name)
        return d_list


    def save_content_list(self, content_list):
        for i in content_list:
            print(i)



    def run(self): # 实现主要逻辑
        # 1. start_url
        url_list = self.get_url_list()
        # 2. 发送请求，获取响应
        for url in url_list:
            html_str = self.get_parse(url)
        # 3. 提取数据
            content_list = self.get_content_list(html_str)
        # 4. 保存
            self.save_content_list(content_list)



if __name__ == "__main__":
    qiubai = QiubaiSpider()
    qiubai.run()