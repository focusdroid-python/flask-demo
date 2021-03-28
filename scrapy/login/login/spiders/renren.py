import scrapy
import re


class RenrenSpider(scrapy.Spider):
    name = 'renren'
    allowed_domains = ['renren.com']
    start_urls = ['http://www.renren.com/974361808/profile']

    def start_requests(self):
        cookies = "anonymid=k9s0c65y2om8pj; _r01_=1; taihe_bi_sdk_uid=dc98311ffc7de226cb1f79afdd705b6f; jebe_key=bf8a72df-0519-4da7-b1df-362082dfd8d0%7C18333670b0ee1f54e006adc80fdd7f23%7C1588568014097%7C1%7C1588568014407; jebe_key=bf8a72df-0519-4da7-b1df-362082dfd8d0%7C92e70cb2bde7172939cddc8f15fdd3b4%7C1588663804895%7C1%7C1588663805116; JSESSIONID=abcQCcacpRCLo6Lv4O4qx; ick_login=c4088f0e-05b4-45aa-bdf0-9b08f1473ad5; taihe_bi_sdk_session=02916b8090c4c5873f420e06488a9481; ick=2cb82a29-88ff-4992-af3c-666c7117e519; __utmc=151146938; first_login_flag=1; __utma=151146938.1079666667.1598678110.1598678110.1598690302.2; _de=D5FD513C20B9124F1FF9E00605E6865D; _ga=GA1.2.1079666667.1598678110; ln_uact=15701229789; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; id=974361808; ver=7.0; wp_fold=0; depovince=GW; jebecookies=24492088-cf66-4fdc-8bf2-a73dab2f1554|||||; p=414d536dfb48b4d07076bd980e03f1068; t=326817c06928fbd075e10801f0a423368; societyguester=326817c06928fbd075e10801f0a423368; xnsid=121915b8; loginfrom=null"
        cookies = {item.split("=")[0]:item.split("=")[1] for item in cookies.split('; ')}
        print('*'*100)
        print(cookies)
        yield scrapy.Request(
            self.start_urls[0],
            callback=self.parse,
            cookies=cookies
        )

    def parse(self, response):
        print(re.findall("王维", response.body.decode()))
