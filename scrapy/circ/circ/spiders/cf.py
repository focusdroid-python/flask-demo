import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import re

class CfSpider(CrawlSpider):
    name = 'cf'
    allowed_domains = ['suning.com']
    start_urls = ['https://list.suning.com/1-502320-0.html']

    rules = (
        # LinkExtractor 连接提取器，提取url地址
        # callback 提取url地址的response会交给callback处理
        # follow 当前url地址的响应是够重新进过rules来提取url
        Rule(LinkExtractor(allow=r'/1-502320-\d+\-0-0-0-0-14-0-4.html'), callback='parse_item', follow=True),
        # Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
        # Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        print('start')
        li_list = response.xpath("//div[@id='filter-results']//ul//li")
        for li in li_list:

            item = {}
            item['title'] = li.xpath(".//div[@class='res-info']//p[@class='sell-point']/a/@title").get()
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
            print(item)
        # return item
