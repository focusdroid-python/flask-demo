# -*- coding:utf-8 -*-

from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("https://mail.qq.com/")

# 切换到iframe
driver.switch_to.frame("login_frame")

driver.find_element_by_id("u").send_keys("840254112@qq.com")
# driver.find_element_by_id("p").send_keys("WangXu19940412")

time.sleep(5)
driver.quit()