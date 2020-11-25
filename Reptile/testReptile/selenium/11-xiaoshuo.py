# -*- coding:utf-8 -*-

from selenium import webdriver

driver = webdriver.Chrome()


driver.get("https://www.kquanben.com/xiaoshuo/1185/")

ret = driver.find_elements_by_xpath("//div[@id='list']/dl/dd")
print(ret)

for i in ret:
    print(i.find_element_by_xpath("./a").text)
    print(i.find_element_by_xpath("./a").get_attribute("href"))
