import scrapy
import re

class GithubSpider(scrapy.Spider):
    name = 'github'
    allowed_domains = ['github.com']
    start_urls = ['https://github.com/login']

    def parse(self, response):
        authenticity_token = response.xpath("//input[@name='authenticity_token']/@value").get()
        webauthn_support = response.xpath("//input[@name='webauthn-support']/@value").get()
        webauthn_iuvpaa_support = response.xpath("//input[@name='webauthn-iuvpaa-support']/@value").get()
        timestamp = response.xpath("//input[@name='timestamp']/@value").get()
        timestamp_secret = response.xpath("//input[@name='timestamp_secret']/@value").get()
        commit = response.xpath("//input[@name='commit']/@value").get()
        post_data = dict(
            login = 'weexss@163.com',
            password = 'Asmie1234',
            timestamp = timestamp,
            timestamp_secret = timestamp_secret,
            commit = commit,
            authenticity_token = authenticity_token,
            webauthn_support = webauthn_support,
            webauthn_iuvpaa_support = webauthn_iuvpaa_support
        )

        yield scrapy.FormRequest(
            self.start_urls[0],
            formdata=post_data,
            callback=self.after_login
        )

    def after_login(self,response):
        # with open('a.html', 'w', encoding='utf-8') as f:
        #     f.write(response.body.decode())
        print(re.findall("asmieuser", response.body.decode()))