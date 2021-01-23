import scrapy
from copy import deepcopy


class SuningSpider(scrapy.Spider):
    name = 'suning'
    allowed_domains = ['sunming.com']
    start_urls = ['https://book.suning.com/']

    def parse(self, response):
        # 1. 大分类分组
        li_list = response.xpath("//div[@class='menu-list']/div")
        for li in li_list:
            item = {}
            item['b_cate'] = li.xpath("dl/dt/h3/a/text()").get()
            # 2. 小分类分组
            item["s_cate"] = li.xpath("./dl/dd/a/text()").extract_first()

            a_list = li.xpath("./dl/dd/a")
            for a in a_list:
                item["s_href"] = a.xpath("./@href").get()
                yield scrapy.Request(
                    item["s_href"],
                    callback=self.parse_book_list,
                    meta={"item": deepcopy(item)}
                )
                print(item["s_href"])
            # item["s_href" = li.xpath("./dl/dd/a/@href")
            # for href in item["s_href"]:
            #     if href is not None:
            #         yield scrapy.Request(
            #             'https://list.suning.com/1-502320-0.html',
            #             callback=self.parse_book_list,
            #             meta={"item": deepcopy(item)}
            #         )
            #         print(href)


    def parse_book_list(self, response):
        print("图书列表信息")
        '''列表页面'''
        item = response.meta["item"]
        # 图书列表页分组
        li_list = response.xpath("//div[@id='filter-results']/ul/li")
        for li in li_list:
            item["book_name"] = li.xpath(".//div[@class='res-info']/p[@class='sell-point']/a/@title").extract_first()
            item["book_href"] = li.xpath(".//div[@class='res-info']/p[@class='sell-point']/a/@href").extract_first()
            item["book_sell"] = li.xpath(".//div[@class='res-info']/p[@class='seller oh no-more']/a/text()").extract_first()
            item["book_img"] = li.xpath(".//div[@class='img-block']//img/@src").extract_first()
            yield scrapy.Request(
                item["book_href"],
                callback=self.parse_book_detail,
                meta={"item": deepcopy(item)}
            )

    def parse_book_detail(self, response):
        """
        保存书本详情页
        :param response:
        :return:
        """
        item = response.meta["item"]
        item["price"] = response.xpath("//span[@class='mainprice']/text()")
        print(item)































