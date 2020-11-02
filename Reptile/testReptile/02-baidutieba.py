# -*- coding:utf-8 -*-
import requests
from lxml import etree
import json

class BaiduSipder:
    def __init__(self, tieba_name):
        self.tieba_name = tieba_name
        self.start_url = "http://tieba.baidu.com/mo/q----,sz@320_240-1-3---2/m?kw="+tieba_name+"&pn=0"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Linux; Android 8.0.0; Nexus 6P Build/OPP3.170518.006) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Mobile Safari/537.36"
        }

    def parse_url(self, url): # 发送请求获取相应
        print(url)
        response = requests.get(url,headers=self.headers)
        return response.content

    def get_content_list(self, html_str): # 提取数据
        html = etree.HTML(html_str)
        div_list = html.xpath("//div[contains(@class,'i')]")
        content_list = []

        for div in div_list:
            item = {}
            item["title"] = div.xpath("./a/text()")[0] if len(div.xpath("./a/text()")) > 0 else ''
            item["href"] = div.xpath("./a/@href")[0] if len(div.xpath("./a/@href")) > 0 else ''
            item["img_list"] = self.get_img_list(item["href"], [])
            content_list.append(item)

        next_url = html.xpath("//a[text()='下一页']/@href")[0] if len(html.xpath("//a[text()='下一页']/@href")) > 0 else None
        return content_list, next_url



    def get_img_list(self, detail_url, total_img_list): # 获取帖子的所有图片

        # 3.2 请求列表页的url地址，获取详情页的第一页
        detail_html_str = self.parse_url(detail_url)
        # 3.3 提取详情页第一页的图片，提取下一页的地址
        detail_html = etree.HTML(detail_html_str)
        # 3.4 请求详情页下一页的地址，进入循环3.2--3.4
        img_list = detail_html.xpath("//img[@class='BDE_Image']@src")
        total_img_list.extend(img_list)

        detail_next_url = detail_html.xpath("//a[text='下一页']/@href")
        if len(detail_next_url) > 0:
            detail_next_url = detail_next_url[0]
            return self.get_content_list(detail_next_url, total_img_list)

        return img_list

    def save_content_list(self, content_list):
        file_path = self.tieba_name=".txt"
        with open(file_path,"a") as f:
            for content in content_list:
                f.write(json.dumps(content, ensure_ascii=False, indent=2))



    def run(self):
        next_url = self.start_url
        while next_url is not None:
            # 1.start_url
            # 2.发送请求，获取响应
            html_str = self.parse_url(next_url)

            # 3.提取数据，获取下一页的ｕｒｌ地址
                # 3.1 提取列表页的url地址和标题
                # 3.2 请求列表页的url地址，获取详情页的第一页
                # 3.3 提取详情页第一页的图片，提取下一页的地址
                # 3.4 请求详情页下一页的地址，进入循环3.2--3.4
                # 3.5
            content_list, next_url = self.get_content_list(html_str)
            # 4.保存数据
            self.save_content_list(content_list)
            # 5.　重复２－５


if __name__ == '__main__':
    tieba_name = 'lol'
    tieba = BaiduSipder(tieba_name)
    tieba.run()