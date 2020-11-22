# -*- coding:utf-8 -*-

from selenium import webdriver
import time
# 实例化一个浏览器
driver = webdriver.Chrome()

# 发送请求
driver.get("https://www.baidu.com")

# 元素定位的方法
driver.find_element_by_id("kw").send_keys("python")
time.sleep(1)
driver.find_element_by_id("su").click()

time.sleep(5)
# 关闭程序,退出浏览器
driver.quit()