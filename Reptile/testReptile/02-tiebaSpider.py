# -*- coding:utf-8 -*-
import requests
from lxml import etree
import json

class TiebaSpider:
    def __init__(self, tieba_name):
        self.tieba_name = tieba_name
        self.start_url = "http://tieba.baidu.com/mo/q----,sz@320_240-1-3---2/m?kw="+self.tieba_name+"&lp=5011&lm=&pn=0"
        self.part_url = "http://tieba.baidu.com/mo/q----,sz@320_240-1-3---2/"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Linux; Android 8.0.0; Nexus 6P Build/OPP3.170518.006) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Mobile Safari/537.36"
        }

    def parse_url(self, url):# 发送请求，获取相应
        print("----------请求url----------------")
        print(url)
        res = requests.get(url, headers=self.headers)
        print(res)
        print("-----------请求返回response-------------------")
        return res.content

    def get_content_list(self, html_str): # 提取数据
        html = etree.HTML(html_str)
        div_list = html.xpath("//div[contains(@class, 'i')]")
        content_list = []
        for div in div_list:
            item = {}
            item["title"] = div.xpath("./a/text()")[0] if len(div.xpath("./div/a/text()")) > 0 else None
            item["href"] = div.xpath("./a/@href")[0] if len(div.xpath("./div/a/@href")) > 0 else None
            item["img_list"] = self.get_img_list(item["href"], [])
            content_list.append(item)
        # 提取下一页的url地址
        next_url = html.xpath("//a[text()='下一页']/@href")[0] if len(html.xpath("//a[text()='下一页']/@href")) > 0 else None
        return content_list, next_url



    def get_img_list(self, detail_url, total_img_list): # 获取帖子所有的图片
        # 3.2 请求列表页的地址，获取详情页的第一页
        detail_html_str = self.parse_url(detail_url)
        detail_html = etree.HTML(detail_html_str)
        # 3.3 提取详情页的第一页的图片，获取下一页的地址
        img_list = detail_html.xpath("//img[@class='BDE_Image']/@src")
        total_img_list.extend(img_list)
        # 3.4 请求详情页下一页的地址，进入循环3.2---3.4步
        detail_next_url = detail_html.xpath("//a[text()='下一页']/@href")
        if len(detail_next_url) > 0:
            detail_next_url = detail_next_url[0]
            return self.get_img_list(detail_next_url, total_img_list)

        return total_img_list

    def save_content_list(self, content_list): # 保存数据
        file_path = self.tieba_name+".txt"
        with open(file_path, "a") as f:
            for content in content_list:
                f.write(json.dumps(content,ensure_ascii=False, indent=2))

        print("保存成功")



    def run(self): # 实现主要逻辑
        # print("----------启动"+self.tieba_name+"爬虫---------------------")
        next_url = self.start_url
        while next_url is not None:
            # 1. start_url
            # 2. 发送请求获取响应
            print("-----------爬虫请求发送开始start------------------")
            html_str = self.parse_url(next_url)
            print("------------爬虫请求发送结束end------------------")
            # 3.　提取数据，提取下一页的url地址
                # 3.1 提取列表页的地址和标题
                # 3.1 请求列表页的地址，获取详情页的第一页
                # 3.1 提取详情页的第一页的图片，获取下一页的地址
                # 3.1 请求详情页下一页的地址，进入循环3.2---3.4步
            content_list, next_url = self.get_content_list(html_str)
            # 4.　保存数据
            self.save_content_list(content_list)
            # 5.　请求下一页的url地址，进入循环2-5步

if __name__ == '__main__':
    tieba = TiebaSpider('lol')
    tieba.run()
