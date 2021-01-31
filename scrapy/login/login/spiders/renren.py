import scrapy
import re

class RenrenSpider(scrapy.Spider):
    name = 'renren'
    allowed_domains = ['renren.com']
    start_urls = ['http://www.renren.com/974361808/profile']


    def start_requests(self):
        cookies = "anonymid=k9s0c65y2om8pj; _r01_=1; taihe_bi_sdk_uid=dc98311ffc7de226cb1f79afdd705b6f; jebe_key=bf8a72df-0519-4da7-b1df-362082dfd8d0%7C92e70cb2bde7172939cddc8f15fdd3b4%7C1588663804895%7C1%7C1588663805116; ick_login=c4088f0e-05b4-45aa-bdf0-9b08f1473ad5; taihe_bi_sdk_session=02916b8090c4c5873f420e06488a9481; ick=2cb82a29-88ff-4992-af3c-666c7117e519; __utmc=151146938; __utmz=151146938.1598678110.1.1.utmcsr=renren.com|utmccn=(referral)|utmcmd=referral|utmcct=/; first_login_flag=1; wpsid=15883893825150; __utma=151146938.1079666667.1598678110.1598678110.1598690302.2; _de=D5FD513C20B9124F1FF9E00605E6865D; _ga=GA1.2.1079666667.1598678110; depovince=GW; jebecookies=9732a44a-efa5-4faf-8686-e74c8b388e0a|||||; p=eda31466730955aa5025a3e80268615f8; ln_uact=15701229789; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; t=2c81d9d01c4857e6bd01807353ee3a3e8; societyguester=2c81d9d01c4857e6bd01807353ee3a3e8; id=974361808; xnsid=a9818e26; ver=7.0; loginfrom=null; wp_fold=0"
        cookies = {i.split("=")[0]:i.split("=")[1] for i in  cookies.split('; ')}

        yield scrapy.Request(
            self.start_urls[0],
            callback=self.parse,
            cookies=cookies
        )

    def parse(self, response):
        print(re.findall("王维", response.body.decode()))
        yield scrapy.Request(
            "http://www.renren.com/974361808/profile?v=info_timeline",
            callback=self.parse_detail
        )

    def parse_detail(self, response):
        print(re.findall("王维", response.body.decode()))