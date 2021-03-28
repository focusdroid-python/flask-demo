import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class Tt1Spider(CrawlSpider):
    name = 'tt1'
    allowed_domains = ['sun0769.com']
    start_urls = ['http://wzzdg.sun0769.com/political/index/politicsNewest']

    rules = (
        Rule(LinkExtractor(allow=r'/political/index/politicsNewest\?id=1&page=\d+'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        li_list = response.xpath("//ul[@class='title-state-ul']/li")
        for li in li_list:
            item = {}
            item["id"] = li.xpath("./span[@class='state1']/text()").get()
            item['title'] = li.xpath("./span[@class='state3']/a/text()").get()
            item['detail'] = li.xpath("./span[@class='state3']/a/@href").get()
            item['detail'] = 'http://wzzdg.sun0769.com'+item['detail']
            yield scrapy.Request(
                item['detail'],
                callback=self.parse_detail,
                meta={"item":item}
            )

    def parse_detail(self, response):
        item = response.meta['item']
        item['detail_title'] = response.xpath("//div[@class='width-12 mr-three']/div[@class='mr-three']/p[@class='focus-details']/text()").get()
        item['detail_username'] = response.xpath("//div[@class='width-12 mr-three']/div[@class='mr-three']/div[@class='focus-date clear focus-date-list']/span[@class='fl details-head']/text()").get()
        item['detail_content'] = response.xpath("//div[@class='width-12 mr-three']/div[@class='mr-three']/div[@class='details-box']/pre/text()").get()

        print(item)

