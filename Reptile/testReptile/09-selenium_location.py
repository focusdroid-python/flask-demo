# -*- coding:utf-8 -*-

from selenium import webdriver

driver = webdriver.Chrome()

# driver.get('https://www.qiushibaike.com/')
driver.get("https://www.baidu.com/s?wd=python&rsv_spt=1&rsv_iqid=0xc0eea8a8000163a0&issp=1&f=8&rsv_bp=1&rsv_idx=2&ie=utf-8&rqlang=cn&tn=baiduhome_pg&rsv_enter=1&rsv_dl=tb&oq=%25E7%25B3%2597%25E4%25BA%258B%25E7%2599%25BE%25E7%25A7%2591&rsv_btype=t&inputT=3196&rsv_t=4138cZptg4wLCm5MYBNHfMIYiPn1syaLhodHh2U2KcFWwvMnwWwl6wFn4a%2FM1OxcAEyO&rsv_pq=b18d270d00012cc2&sug=%25E7%25B3%2597%25E4%25BA%258B%25E7%2599%25BE%25E9%25BB%2591%25E6%259C%25A8%25E5%25A4%25A7%25E8%25B5%259B&rsv_sug3=53&rsv_sug1=35&rsv_sug7=100&rsv_sug2=0&rsv_sug4=3196&rsv_sug=1")

# ret = driver.find_elements_by_xpath("//div[@class='recommend-article']/ul/li")
# print(ret)
#
# for li in ret:
#     print(li.find_element_by_xpath(".//a[@class='recmd-content']").text)
#     print(li.find_element_by_xpath(".//a[@class='recmd-content']").get_attribute("href"))


link = driver.find_element_by_link_text("下一页 >").get_attribute('href')
link1 = driver.find_element_by_partial_link_text("下一页").get_attribute('href')
print(link)
print(link1)



driver.quit()
