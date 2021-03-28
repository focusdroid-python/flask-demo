import scrapy
import re

class Github2Spider(scrapy.Spider):
    name = 'github2'
    allowed_domains = ['github.com']
    start_urls = ['https://github.com/login']

    def parse(self, response):
        yield scrapy.FormRequest.from_response(
            response, # 自动冲response中寻找from表单
            formdata={"login":"weexss@163.com", "password":"Asmie1234"},
            callback=self.after_login
        )

    def after_login(self, response):
        print(re.findall("New repository", response.body.decode()))