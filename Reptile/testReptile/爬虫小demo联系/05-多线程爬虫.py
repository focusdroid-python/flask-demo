# -*- coding:utf-8 -*-
import requests
from lxml import etree
import threading
from queue import Queue


class QiubaiSpdier:
    def __init__(self):
        self.url_temp = "https://www.qiushibaike.com/8hr/page/{}/"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36",
            "Host": "www.qiushibaike.com"
        }
        self.url_queue = Queue()
        self.html_queue = Queue()
        self.content_queue = Queue()

    def get_url_list(self):
        # return [self.url_temp.format(i) for i in range(1, 14)]
        for i in range(1,14):
            self.url_queue.put(self.url_temp.format(i))

    def parse_url(self):
        while True:
            url = self.url_queue.get()
            print(url)
            print('*'*50)
            # response = requests.get(url, headers=self.headers)
            # return response.content.decode()

            response = requests.get(url, headers=self.headers)
            self.html_queue.put(response.content.decode())
            self.url_queue.task_done()

    def get_content_list(self):
        while True:
            html_str = self.html_queue.get()
            html = etree.HTML(html_str)
            content_list = []
            div_list = html.xpath("//div[@class='recommend-article']/ul") #
            for div in div_list:
                item={}
                # item["title_img"] = div.xpath("./li/a/img/@src")
                # item["title_img"] = item["title_img"][0] if len(item["title_img"]) > 0 else None
                item["title"] = div.xpath("./li/div[@class='recmd-right']/a/text()")
                # item["title"] = item["title"][0] if len(item["title"]) > 0 else None

                # item["content"] = div.xpath("./li[@class='content']/span/text()")
                # item["author_gender"] = div.xpath(".//div[contains(@class, 'articleGender')]/@class")
                # item["author_gender"] = item["author_gender"][0].split(" ")[-1].replace("Icon", "") if len(item["author_gender"]) > 0 else None
                # item["author_age"] = div.xpath(".//div[contains(@class,'articleGender')]/text()")
                # item["author_age"] = item["author_age"][0] if len(item["author_age"]) > 0 else None

                # item["content_img"] = div.xpath(".//div[@class='thumb']/a/img/src")
                # item["content_img"] = item["content_img"][0] if len(item["content_img"])>0 else None

                # item["author_img"] = div.xpath(".//div[@class='author clearfix]//img/@src")
                # item["author_img"] = item["author_img"][0] if len(item["author_img"]) > 0 else None
                # item["stats_vote"] = div.xpath(".//div[@xlass='stats-vote']/i/text()")
                # item["stats_vote"] = item["stats_vote"][0] if len(item["stats_vote"]) > 0 else None
                content_list.append(item)
            self.content_queue.put(content_list)
            self.content_queue.task_done()

    def save_content_list(self): # 保存数据
        while True:
            content_list = self.content_queue.get()
            for i in content_list:
                print(i)
            # self.content_queue.task_done()

    def run(self): # 实现主要逻辑
        thread_list = []
        # 1.　url_list　
        t_url = threading.Thread(target=self.get_url_list)
        thread_list.append(t_url)

        # 2.　遍历，发送请求，获取响应
        for i in range(20):
            t_parse = threading.Thread(target=self.parse_url)
            thread_list.append(t_parse)
        # ３．　提取数据
        for i in range(20):
            t_html = threading.Thread(target=self.get_content_list)
            thread_list.append(t_html)
        # ４．　保存
        t_save = threading.Thread(target=self.save_content_list)
        thread_list.append(t_save)

        for t in thread_list:
            t.setDaemon(True)
            t.start()

        for q in [self.url_queue, self.content_queue, self.html_queue]:
            q.join() # 让主线程等待阻塞，　等待队列的任务完成之后再完成
        print("主线程结束")

if __name__ =="__main__":
    qiubai = QiubaiSpdier()
    qiubai.run()