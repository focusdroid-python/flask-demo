import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import re

class CfSpider(CrawlSpider):
    name = 'cf'
    allowed_domains = ['baidu.com']
    start_urls = ['http://baidu.com/']

    # 定义提取url规则的
    # LinkExtractor 链接提取
    # callback 提取出来的url地址的response会交给callback处理
    # follow 当前的url地址的响应是够重新过rules来提取url地址000
    #
    rules = (
        # Rule(LinkExtractor(allow=r'前后端未分离的当条数据的详情连接'), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=r'/web/site0/tab52040/info\d+\.html'), follow=True),

        # Rule(LinkExtractor(allow=r'下一页（翻页）连接'), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=r'/web/site0/tab52040/module14430/page\d+\.html'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = {}
        item["title"] = re.findall('<h4 class="recruit-title">(.*?)</h4>', response.body.decode())[0]
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        return item
