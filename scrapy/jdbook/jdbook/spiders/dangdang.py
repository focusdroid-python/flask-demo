import scrapy
from scrapy_redis.spiders import RedisSpider
from copy import deepcopy

class DangdangSpider(RedisSpider):
# class DangdangSpider(scrapy.Spider):
    name = 'dangdang'
    allowed_domains = ['dangdang.com']
    # start_urls = ['http://book.dangdang.com/'] # http://book.dangdang.com/
    redis_key = "dangdang"


    def parse(self, response):
        # 大分类
        div_list = response.xpath("//div[@class='con flq_body']/div")
        for div in div_list:
            item = {}
            item["b_cate"] = div.xpath("./dl/dt/text()").extract()
            item["b_cate"] = [i.strip() for i in item["b_cate"] if len(i.strip())>0]
            # 获取中间分类
            dl_list = div.xpath("./div//div[@class='inner_dl']")
            for dl in dl_list:
                item["m_cate"] = dl.xpath("./dt//text()").get()
                item["m_cate"] = [i.strip() for i in item["m_cate"] if len(i.strip())>0]
                # 获取小分类
                a_list = div.xpath("./dd/a")
                for a in a_list:
                    item["s_href"] = a.xpath("./@href").get()
                    item["s_title"] = a.xpath("./@title").get()
                    print(item)
    #                 if item["s_href"] is not None:
    #                     yield scrapy.Request(
    #                         item["s_href"],
    #                         callback=self.parse_book_list,
    #                         meta={"item": deepcopy(item)},
    #                         headers={
    #                             "Referer": "http://baby.dangdang.com/"
    #                         }
    #                     )
    #
    #
    #
    # def parse_book_list(self, response):
    #     item = response.meta["item"]
    #     li_list = response.xpath("//ul[@class='list_aa']/li")
    #     for li in li_list:
    #         item["book_img"] = li.xpath("./a/img/@src").get()
    #         item["book_href"] = li.xpath("./a/@href").get()
    #         item["name"] = li.xpath("./p[@class='name']/a/@title").get()
    #         item["num"] = li.xpath("./p[@class='price']//span[@class='num']/text()").get()
    #         item["tail"] = li.xpath(".//p[@class='price']//span[@class='tail']/text()").get()
    #         print(item)


