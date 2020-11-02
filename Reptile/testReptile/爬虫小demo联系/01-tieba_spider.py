# -*- coding:utf-8 -*-
import requests
from lxml import etree

class TiebaSpider:
    def __init__(self, tiebaname):
        self.start_url = "https://tieba.baidu.com/mo/q----,sz@320_240-1-3---2/m?kw="+tiebaname+"&pn={}"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"
        }

    def parse_url(self, url): # 发送请求，获取响应
        response = requests.get(url, headers=self.headers)
        return response.content.decode()

    def get_content_list(self, html_str): # 提取数据
        html = etree.HTML(html_str)
        div_list = html.xpath("//div[contains(@class, 'i')]") # 根据div分组
        for div in div_list:
            item = {}
            item["title"] = div.xpath("./a/text()")[0] if len(div.xpath("./a/text()")) > 0 else None
            item["href"] = div.xpath("./a/@href")[0] if len(div.xpath("./a/@href")) > 0 else None
            item["img_list"] = self.get_img_list(item["href"])

    def get_img_list(self, detail_url): # 获取帖子中的所有图片
        pass


    def run(self): # 实现主要逻辑
        # １．　start url
        # ２．　发送请求，获取响应
        html_str = self.parse_url(self.start_url)
        # 3. 提取数据　提取下一页的ｕｒｌ地址
            # 3.1 提取列表页的url地址和标题
            # 3.2　请求列表页的url地址，获取详情页的第一页
            # 3.3 提取详情页的第一页的图片，提取下一页的地址
            # 3.4 请求详情页下一页的地址，进入循环３．２－３．４
        # ４. 保存数据
        # ５. 请求下一页的url地址，进入循环２－５页
        pass


if __name__ == "__main__":
    tieba = TiebaSpider()
    tieba.run()
