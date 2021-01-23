import scrapy
from yangguang.items import YangguangItem
from tencent.settings import MONGO_HOST


class YgSpider(scrapy.Spider):
    name = 'yg'
    allowed_domains = ['sun0769.com']
    start_urls = ['http://wz.sun0769.com/political/index/politicsNewest?id=1&page=1']

    def parse(self, response):
        print('spider start')
        # 分组
        try:
            li_list = response.css('li.clear')
            for li in li_list:
                item = YangguangItem()
                item['id'] = li.css('span.state1::text').get()
                item['state'] = li.css('span.state2::text').get()
                item['title'] = li.xpath("span[@class='state3']/a[@class='color-hover']/text()").get()
                item['href'] = li.xpath("span[@class='state3']/a[@class='color-hover']/@href").get()
                item['href'] = 'http://wz.sun0769.com'+item['href']
                # item['href'] = ['http://wz.sun0769.com'+ i for i in item['href']]
                item['sleepTime'] = li.css('span.state4::text').get()
                item['time'] = li.css('span.state5::text').get()
                # print(item)
                yield scrapy.Request(item['href'], callback=self.parseDetail, meta={"item":item}) # 处理详情页面


            # 翻页
            next_url = response.xpath("//div[@class='mr-three paging-box']/a/@href").get()
            print(next_url)
            next_url = 'http://wz.sun0769.com'+ next_url
            if next_url is not None:
                yield scrapy.Request(next_url, callback=self.parse)
                print(next_url)
            # next_url = response.xpath("//a[text()='>']/@href")

        except TypeError:
            print('爬虫完成')


    def parseDetail(self, response): # 处理详情页
        item = response.meta["item"]
        item['content_title'] = response.xpath("//div[@class='mr-three']/p[@class='focus-details']/text()").get()
        item['content'] = response.xpath("//div[@class='mr-three']/div[@class='details-box']/pre/text()").extract()
        item['content_img'] = response.xpath("//div[@class='clear details-img-list Picture-img']/img/@src").extract()
        yield item
