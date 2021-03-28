import scrapy
import json
from tencent.items import TencentItem


class HrSpider(scrapy.Spider):
    name = 'hr'
    allowed_domains = ['tencent.com']
    urls = 'https://careers.tencent.com/tencentcareer/api/post/Query?pageSize=100&pageIndex='

    # 设置页码
    set_pageIndex = 1

    start_urls = [urls+str(set_pageIndex)]

    def parse(self, response):
        try:
            content = json.loads(response.body.decode())
            jobs = content["Data"]["Posts"]
            for job in jobs:
                item = TencentItem()
                item['CategoryName'] = job['CategoryName']
                item['LastUpdateTime'] = job['LastUpdateTime']
                item['PostURL'] = job['PostURL']
                item['CountryName'] = job['CountryName']
                item['LocationName'] = job['LocationName']
                item['RecruitPostName'] = job['RecruitPostName']
                item['BGName'] = job['BGName']
                yield item

            # for job in jobs:
            #     item = {}
            #     item['CategoryName'] = job['CategoryName']
            #     item['LastUpdateTime'] = job['LastUpdateTime']
            #     item['PostURL'] = job['PostURL']
            #     item['CountryName'] = job['CountryName']
            #     item['LocationName'] = job['LocationName']
            #     item['RecruitPostName'] = job['RecruitPostName']
            #     item['BGName'] = job['BGName']
            #     yield item

            # 页码设置
            self.set_pageIndex += 1
            next_url = self.urls + str(self.set_pageIndex)
            print(next_url)
            print('-'*100)

            yield scrapy.Request(next_url, callback=self.parse)

        except TypeError:
            print('爬虫结束')

    # def parse(self, response):
    #     print(response.body.decode())
    #     # quote_list = response.css("div.recruit-list").extract()
    #     quote_list = response.xpath("//div[@class='recruit-wrap recruit-margin']/div")
    #     for quote in quote_list:
    #         yield {
    #             'title': quote.xpath('a/h4/text()').get(),
    #             'text': quote.css('./div.recruit-text::text').get()
    #         }

#
# import scrapy
#
#
# class HrSpider(scrapy.Spider):
#     name = 'hr'
#     start_urls = [
#         'http://quotes.toscrape.com/tag/humor/',
#     ]
#
#     def parse(self, response):
#         quote_list = response.css('div.quote')
#         for quote in quote_list:
#
#             # yield {
#             #     'author': quote.xpath('span/small/text()').get(),
#             #     'text': quote.css('span.text::text').get(),
#             # }
#
#             item = {}
#             item['author'] = quote.xpath('span/small/text()').get()
#             item['text'] = quote.css('span.text::text').get()
#             print(item)
#             yield item