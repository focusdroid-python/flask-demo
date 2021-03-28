import scrapy
from yangguang.items import YangguangItem
import time

class YgSpider(scrapy.Spider):
    name = 'yg'
    allowed_domains = ['sun07691.com']
    start_urls = ['http://wzzdg.sun0769.com/political/index/politicsNewest']

    def parse(self, response):
        print(self.hello)
        print('--'*1000)
        li_list = response.xpath("//ul[@class='title-state-ul']/li")
        for li in li_list:
            item = YangguangItem()
            item['id'] = li.xpath("./span[@class='state1']/text()").extract_first()
            item['title'] = li.xpath("./span[@class='state3']/a/text()").extract_first()
            item['href'] = li.xpath("./span[@class='state3']/a/@href").extract_first()
            item['href'] = 'http://wzzdg.sun0769.com/'+item['href']
            item['public_date'] = li.xpath("./span[@class='state5']/text()").extract_first()
            item['sleep_date'] = li.xpath("./span[@class='state4']/text()").extract_first()

            yield scrapy.Request(
                item['href'],
                callback = self.parse_detail,
                meta={'item':item}
            )

            # 翻页
            next_url = response.xpath("//a[@class='arrow-page prov_rota']/@href").get()
            next_url = 'http://wzzdg.sun0769.com'+next_url
            if next_url is not None:
                yield scrapy.Request(
                    next_url,
                    callback=self.parse
                )


    def parse_detail(self, response): # 处理详情页
        item = response.meta['item']
        item['content'] = response.xpath("//div[@class='details-box']/pre/text()").extract()
        item['contnet_img'] = response.xpath("div[@class='clear details-img-list Picture-img']//img/@src").extract()
        # item['content_img'] = [""]
        # print(item)
        yield item

        time.sleep(5)