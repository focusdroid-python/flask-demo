# -*- coding:utf-8 -*-

from selenium import webdriver
import time

driver = webdriver.Chrome()


driver.get("https://accounts.douban.com/passport/login")
# time.sleep(2)

driver.find_element_by_id("username").send_keys("15701229789")
driver.find_element_by_id("password").send_keys("Asmie1234")

time.sleep(5)
driver.find_element_by_class_name("btn-account").click()

# 获取cookie
cookies = {i["name"]: i["value"] for i in driver.get_cookies()}

print(cookies)


time.sleep(5)
driver.quit()


