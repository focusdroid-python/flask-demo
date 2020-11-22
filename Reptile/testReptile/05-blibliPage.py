# -*- coding:utf-8 -*-
import requests
from lxml import etree
import json

class BliBli:
    def __init__(self, site_name):
        self.site_name = site_name
        self.start_url = "https://search.bilibili.com/video?keyword="+site_name+"&page={}"
        self.headers = {
            "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
            "cookie": "uuid=FDA0E6C6-969D-F5DB-AB50-96A8E70DE50188272infoc; buvid3=05855B56-14D7-4FB0-8119-8E64659792F9138403infoc; bfe_id=5db70a86bd1cbe8a88817507134f7bb5"
        }

    def crete_url(self):
        return [self.start_url.format(i) for i in range(1, 3)]

    def get_parse(self, url):
        print(url)
        res = requests.get(url, headers = self.headers)
        return res.content.decode()

    def get_content_list(self, html_str):
        html = etree.HTML(html_str)
        div_list = html.xpath("//ul[contains(@class,'video-list')]/li")
        content_list = []
        print(div_list)
        print(len(div_list))
        for div in div_list:
            item = {}
            item["title"] = div.xpath("./a/@title")[0] if len(div.xpath(".//div[contains(@class, 'headline')]/a/@title")) > 0 else None
            item["href"] = div.xpath("./a/@href")[0] if len(div.xpath(".//div[contains(@class, 'headline')]/a/@href")) > 0 else None

            content_list.append(item)
        return content_list

    def save_content_list(self, content_list):
        file_path = self.site_name+'.json'
        with open(file_path, "a", encoding="utf-8") as f:
            for content in content_list:
                f.write(json.dumps(content, ensure_ascii=False, indent=2))
        print("保存成功!")




    def run(self):
        url_list = self.crete_url()
        for url in url_list:
            html_str = self.get_parse(url)

            content_list = self.get_content_list(html_str)
            print(content_list)
            self.save_content_list(content_list)


if __name__ == "__main__":
    bli = BliBli("鬼畜调教")
    bli.run()
