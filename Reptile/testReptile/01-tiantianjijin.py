# -*- coding:utf-8 -*-
from selenium import webdriver
import time
import json


class  TTjijin:
    def __init__(self):
        self.start_url = "http://fund.eastmoney.com/data/fundranking.html#tall;c0;r;szzf;pn50;ddesc;qsd20191124;qed20201124;qdii;zq;gg;gzbd;gzfs;bbzt;sfbb"
        self.driver = webdriver.Chrome()
        self.total_content = []

    def get_content_list(self):
        td_list = self.driver.find_elements_by_xpath("//table[@id='dbtable']/tbody/tr")
        content_list = []
        for td in td_list:
            item={}
            item["id"] = td.find_element_by_xpath("./td["+1+"]")

            content_list.append(item)
        next_url = self.driver.find_element_by_link_text('下一页')
        next_url = next_url[0] if len(next_url) > 0 else None
        return content_list, next_url

    def save_content_list(self, content_list):
        print(content_list)


    def run(self):
        self.driver.get(self.start_url)

        content_list, next_url = self.get_content_list()

        self.save_content_list(content_list)


if __name__ == "__main__":
    tt = TTjijin()
    tt.run()

