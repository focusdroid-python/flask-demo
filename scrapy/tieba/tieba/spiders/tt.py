import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class TtSpider(CrawlSpider):
    name = 'tt'
    allowed_domains = ['sun0769.com']
    start_urls = ['http://wzzdg.sun0769.com/political/index/politicsNewest']

    rules = (
        Rule(LinkExtractor(allow=r'/political/index/politicsNewest\?id=1&page=\d+'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = {}
        # item['test'] = '1231313213213123132132132123'
        item['id'] = response.xpath("//ul[@class='title-state-ul']/li//span[@class='state1']/text()").get()
        item['next_url'] = response.xpath("//a[@class='arrow-page prov_rota']/@href").get()
        item['title'] = response.xpath("//ul[@class='title-state-ul']/li/span[@class='state3']/a/text()").extract()
        item['status'] = response.xpath("//ul[@class='title-state-ul']/li/span[@class='state2']/text()").extract()
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        # return item
        print(item)