# -*- coding:utf-8 -*-
from selenium import webdriver


class TestSelenium:
    def __init__(self):
        self.start = ""
        self.driver = webdriver.Chrome()

    def get_content_list(self):
        li_list = self.driver.find_elements_by_xpath("")
        content_list = []
        for li in li_list:
            item = {}
            item["title"] = li.find_element_by_xpath("")
            content_list.append(item)

        next_url = self.driver.find_elements_by_link_text("下一页")
        next_url = next_url[0] if len(next_url) > 0 else None
        return content_list, next_url

    def run(self):
        self.driver.get(self.start_url)

        self.get_content_list()


if __name__ == '__main__':
    test = TestSelenium()
    test.run()
