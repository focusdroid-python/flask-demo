import scrapy
import logging

logger = logging.getLogger(__name__)

class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['itcast.cn']
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml']

    def parse(self, response):
        # extract和get的区别就是  extract是获取一个列表。get只能获取一个元素
        # ret = response.xpath("//ul[@class='clears']/li/div[@class='main_bot']/h2/text()").extract()
        # ret_title = response.xpath("//ul[@class='clears']/li/div[@class='main_bot']/h2/span/text()").extract()
        # # ret = response.xpath("//ul[@class='clears']/li/div[@class='main_bot']/h2/text()").get()
        # print(ret, ret_title)


        # 分组
        li_list = response.xpath("//div[@class='maincon']/ul[@class='clears']/li")
        for li in li_list:
            item = {}
            item['name'] = li.xpath("./div[@class='main_bot']/h2/text()").get()
            item['title'] = li.xpath("./div[@class='main_bot']/h2/span/text()").get()
            logger.warning(item)
            # print(item)
            yield item