# -*- coding:utf-8 -*-

from selenium import webdriver
import time

# selenium不支持PhantomJS下面的代码提供支持
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

# 实例化一个浏览器
driver = webdriver.Chrome(chrome_options=chrome_options)

# 设置窗口大小
# driver.set_window_size(1920, 1080)
driver.maximize_window()
# 发送请求
driver.get("https://www.baidu.com/")
#
# driver.save_screenshot("./baidu1.png")
print(driver.page_source)
print(driver.current_url)


# driver获取cookie
# cookies = driver.get_cookies()
#
# print(cookies)
# print("*"*100)
#
# cookies = {i["name"]: i["value"] for i in cookies}
# print(cookies)

# 退出浏览器
time.sleep(5)
driver.quit()

