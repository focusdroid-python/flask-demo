import scrapy
from copy import deepcopy


class SuningSpider(scrapy.Spider):
    name = 'suning'
    allowed_domains = ['suning.com']
    start_urls = ['https://book.suning.com/']

    def parse(self, response):
        # 获取大分类分组
        li_list = response.xpath("//div[@class='menu-list']/div[@class='menu-item']")
        # son_list = response.xpath("//div[@class='menu-list']/div[@class='menu-item']/dl/dd/a")
        for  li in li_list:
            item = {}
            item['type'] = li.xpath("./dl/dt/h3/a/text()").extract_first()
            item['type_href'] = li.xpath("./dl/dt/h3/a/@href").extract_first()

            a_list = li.xpath("./dl/dd/a")
            for a in a_list:
                item['s_text'] = a.xpath("./text()").get()
                item['s_href'] = a.xpath("./@href").get()
                if item['s_href'] is not None:
                    yield scrapy.Request(
                        item['s_href'],
                        callback=self.parse_book_list,
                        meta={'item': deepcopy(item)}
                    )
        # for son_href in son_list:
        #     item = {}
        #     item['s_text'] = son_href.xpath("./text()").get()
        #     item['s_href'] = son_href.xpath("./@href").get()
        #     print(item)

    def parse_book_list(self, response):
        item = response.meta['item']
        # 图书列表也分组
        li_list = response.xpath("//div[@class='filter-results productMain clearfix  temporary']/ul[@class='clearfix']/li")
        for  li in li_list:
            item['book_name'] = li.xpath(".//div[@class='res-info']//p[@class='sell-point']//a/@title").get()
            item['book_img'] = li.xpath(".//div[@class='res-img']//img/@src").get()
            # item['book_img'] = 'https:'+item['book_img']
        print(item)


















