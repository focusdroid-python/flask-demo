# -*- coding:utf-8 -*-
from selenium import webdriver
import time
import json

class DouyuSpider:
    def __init__(self):
        self.start_url = "https://www.douyu.com/directory/all"
        self.driver = webdriver.Chrome()

    def get_content_list(self):
        li_list = self.driver.find_elements_by_xpath("//ul[@class='layout-Cover-list']/li")
        content_list = []
        for li in li_list:
            item = {}
            item["room_title"] = li.find_element_by_xpath(".//h3[@class='DyListCover-intro']").get_attribute("title")
            item["room_img"] = li.find_element_by_xpath(".//div[@class='DyListCover-imgWrap']/div/img").get_attribute("src")
            item["room_cate"] = li.find_element_by_xpath(".//span[@class='DyListCover-zone']").text
            item["anchor_name"] = li.find_element_by_xpath((".//div[@class='DyListCover-userName']")).text
            item["watch_num"] = li.find_element_by_xpath(".//span[@class='DyListCover-hot']").text

            content_list.append(item)
            # 获取下一页的元素
        next_url = self.driver.find_elements_by_xpath("//li[@title='下一页']")
        print(next_url)
        next_url = next_url[0] if len(next_url) > 0 else None


        return content_list, next_url

    def save_content_list(self, content_list):
        print(content_list)
        print("*"*100)
        with open('douban.json', 'w', encoding='utf-8') as f:
            f.write(json.dumps(content_list, ensure_ascii=False))


    def run(self):
        # 1. start_url
        # 2. 发送请求,获取响应
        self.driver.get(self.start_url)
        time.sleep(3)
        # 3. 提取数据,提取下一页的按钮
        content_list, next_url = self.get_content_list()
        print(next_url)
        # 4. 保存数据
        self.save_content_list(content_list)
        # 5. 点击下一页元素,循环
        while next_url is not None:
            print(next_url)
            next_url.click()
            time.sleep(5)
            content_list, next_url = self.get_content_list()
            self.save_content_list(content_list)


if __name__ == "__main__":
    douyu = DouyuSpider()
    douyu.run()
