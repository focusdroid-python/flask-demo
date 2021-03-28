import scrapy
import json
from tencent.items import TencentItem

class HrSpider(scrapy.Spider):
    name = 'hr'
    allowed_domains = ['tencent.com']
    url = 'https://careers.tencent.com/tencentcareer/api/post/Query?pageSize=100&pageIndex='

    # 设置页码
    set_pageIndex = 1

    start_urls = [url+str(set_pageIndex)]
    print(start_urls)

    def parse(self, response):
        # 在爬虫中如果是借口这种的话是可以直接使用借口提取数据，
        # 如果是后端返回模板使用xpath直接页面获取
        try:
            content = json.loads(response.body.decode())
            jobs = content['Data']['Posts']
            for job in jobs:
                # item = {}
                item = TencentItem()
                item['CategoryName'] = job['CategoryName']
                item['LastUpdateTime'] = job['LastUpdateTime']
                item['PostURL'] = job['PostURL']
                item['CountryName'] = job['CountryName']
                item['LocationName'] = job['LocationName']
                item['RecruitPostName'] = job['RecruitPostName']
                item['BGName'] = job['BGName']
                yield item

            # 翻页操作
            self.set_pageIndex += 1

            next_url = self.url + str(self.set_pageIndex)

            print(next_url)

            yield scrapy.Request(next_url, callback=self.parse)
        except TypeError:
            print('爬虫结束')
