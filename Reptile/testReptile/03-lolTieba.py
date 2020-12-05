# -*- coding:utf-8 -*-

from selenium import webdriver
import time
import json

class LOLTieba:
    def __init__(self):
        self.start_url = "http://tieba.baidu.com/mo/q----,sz@320_240-1-3---2/m?kw=lol&pn=0&lp=9001"
        self.driver = webdriver.Chrome()

    def get_content_list(self):
        li_list = self.driver.find_elements_by_xpath("//div[@class='i']")
        print(li_list)
        content_list = []

        for li in li_list:
            item={}
            item['title'] = li.find_element_by_xpath("./a").text

            content_list.append(item)

        next_url = self.driver.find_elements_by_link_text("下一页")
        next_url = next_url[0] if len(next_url) > 0 else None
        return content_list, next_url

    def save_content_list(self, content_list):
        print(content_list)
        with open("tieba.json", "w") as f:
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



if __name__ == '__main__':
    tieba = LOLTieba()
    tieba.run()