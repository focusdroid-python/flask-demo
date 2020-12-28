import scrapy


class ItcastSpider(scrapy.Spider):
    name = 'itcast' # 爬虫名
    allowed_domains = ['itst.cn'] # 允许爬虫的范围
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml'] # 最来是请求的url address

    def parse(self, response):
        # 处理start-url地址响应的
        # ret = response.xpath("//div[@class='main_bot']/h2/text()").extract()
        # print(ret)

        # 分组
        li_list = response.xpath("//div[@class='maincon']/ul[@class='clears']/li")
        for li in li_list:
            item = {}
            item["name"] = li.xpath(".//h2/text()").extract_first()
            item["title"] = li.xpath(".//h2/span/text()").extract_first()
            # print(item)
            # Spider must return request, item, or None
            yield item # 传给pipelines,



