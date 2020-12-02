# -*- coding:utf-8 -*-
from selenium import webdriver
import time
import json

class Qiushibaike:
    def __init__(self):
        self.start_url = "https://www.qiushibaike.com/text/"
        self.driver = webdriver.Chrome()
        self.total_content = []

    def get_content_list(self):
        div_list = self.driver.find_elements_by_xpath("//div[@class='col1 old-style-col1']/div")
        content_list = []
        for div in div_list:
            item = {}
            item['name'] = div.find_element_by_xpath("./div[@class='author clearfix']/a/h2").text
            item['gender'] = div.find_element_by_xpath("./div[@class='author clearfix']/div").text
            item['content'] = div.find_element_by_xpath(".//div[@class='content']/span").text
            item['stats'] = div.find_element_by_xpath(".//span[@class='stats-vote']/i").text
            item['statsComments'] = div.find_element_by_xpath(".//span[@class='stats-comments']/a[@class='qiushi_comments']/i").text


            content_list.append(item)

        next_url = self.driver.find_elements_by_link_text("下一页")
        next_url = next_url[0] if len(next_url) > 0 else None
        return content_list, next_url


    def save_content_list(self, content_list):
        print(content_list)
        with open("qiubai.json", "w") as f:
            f.write(json.dumps(content_list, ensure_ascii=False))




    def run(self):
        self.driver.get(self.start_url)

        content_list, next_url = self.get_content_list()

        self.save_content_list(content_list)

        while next_url is not None:
            next_url.click()
            time.sleep(3)
            content_list, next_url = self.get_content_list()

            self.save_content_list(content_list)





if __name__ == "__main__":
    qiushi = Qiushibaike()
    qiushi.run()
