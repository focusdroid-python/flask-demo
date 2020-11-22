# -*- coding:utf-8 -*-

from selenium import webdriver
import time
import json

class Bli:
    def __init__(self):
        self.start_url = "https://search.bilibili.com/video?keyword=%E9%AC%BC%E7%95%9C%E8%B0%83%E6%95%99"
        self.driver = webdriver.Chrome()

    def get_content_list(self):
        li_list = self.driver.find_elements_by_xpath("//ul[@class='video-list clearfix']/li")
        content_list = []
        for li in li_list:
            item = {}
            item["title"] = li.find_element_by_xpath("./a").get_attribute("title")
            item["href"] = li.find_element_by_xpath("./a").get_attribute("href")
            item["watch_num"] = li.find_element_by_xpath(".//span[@class='so-icon watch-num']").text
            item["time"] = li.find_element_by_xpath(".//span[@class='so-icon time']").text
            item["anthor"] = li.find_element_by_xpath(".//a[@class='up-name']").text

            content_list.append(item)
        next_url = self.driver.find_elements_by_xpath("//li[@class='page-item next']")
        next_url = next_url[0] if len(next_url) > 0 else None

        return content_list, next_url

    def save_contnet_list(self, content_list):
        print(content_list)
        print("*"*100)
        with open("blibliSelenium.json", 'w') as f:
            f.write(json.dumps(content_list, ensure_ascii=False))

    def run(self):

        self.driver.get(self.start_url)
        time.sleep(3)
        content_list, next_url = self.get_content_list()

        self.save_contnet_list(content_list)

        while next_url is not None:
            next_url.click()
            time.sleep(5)
            content_list, next_url = self.get_content_list()
            self.save_contnet_list(content_list)



if __name__ == "__main__":
    bli = Bli()
    bli.run()