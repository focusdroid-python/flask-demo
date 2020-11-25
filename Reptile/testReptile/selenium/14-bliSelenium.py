# -*- coding:utf-8 -*-

from selenium import webdriver
import time
import json

class Bli:
    def __init__(self):
        self.start_url = "https://search.bilibili.com/video?keyword=鬼畜调教&order=click"
        self.driver = webdriver.Chrome()
        self.total_list=[]

    def get_content_list(self):
        li_list = self.driver.find_elements_by_xpath("//ul[@class='video-list clearfix']/li")
        content_list = []
        for li in li_list:
            item={}
            item["title"] = li.find_element_by_xpath("./a[@class='img-anchor']").get_attribute('title')

            content_list.append(item)
        next_url = self.driver.find_elements_by_xpath("//li[@class='page-item next']")
        next_url = next_url[0] if len(next_url) > 0 else None

        return content_list, next_url

    def save_content_list(self, content_list,):
        print(content_list)
        print("*"*100)
        self.total_list.extend(content_list)
        with open("B.json", "w") as f:
            f.write(json.dumps(self.total_list, ensure_ascii=False))


    def run(self):
        self.driver.get(self.start_url)
        time.sleep(3)
        content_list, next_url = self.get_content_list()

        self.save_content_list(content_list)

        while next_url is not None:
            next_url.click()
            time.sleep(5)
            content_list, next_url = self.get_content_list()

            self.save_content_list(content_list)


if __name__ == "__main__":
    bli = Bli()
    bli.run()
