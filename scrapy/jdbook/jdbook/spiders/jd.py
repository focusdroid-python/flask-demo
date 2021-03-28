import scrapy
import json

class JdSpider(scrapy.Spider):
    name = 'jd'
    allowed_domains = ['jd.com']
    refer_start = 'https://book.jd.com/'
    # start_urls = ['https://book.jd.com/booksort.html']
    start_urls = ['https://pjapi.jd.com/book/sort?source=bookSort&callback=jsonp_1615990658447_57145']

    def parse(self, response):
        print(response.body.decode())

    # def parse(self, response):
    #     dt_list = response.xpath("//div[@class='mc']/dl/dt") # 大分类列表
    #     for dt in dt_list:
    #         item = {}
    #         item['b_cate'] = dt.xpath("./a/text()").extract_first()
    #         print(item)
    #         # em_list = dt.xpath("./following-sibling::dd[1]/em)")
    #         # for em in em_list:
    #         #     item['s_href'] = em.xpath("./a/@href").extract_first()
    #         #     item['s_text'] = em.xpath("./a/text()").extract_first()
    #
    #             # if item['s_href'] is not None:
    #             #     item['s_href'] = 'https://'+item['s_href']
    #             #     yield scrapy.Request(
    #             #         item['s_href'],
    #             #         callback=self.book_detail,
    #             #         meta={'item': item}
    #             #     )
    #
    # def book_detail(self, response): #解析列表页
    #     item = response.meta['item']
    #     li_list = response.xpath("ul[@class='gl-warp clearfix']/li")
    #     for li in li_list:
    #         item["book_img"] = li.xpath("./div[@class='gl-i-wrap']/div[@class='p-img']//a/img/@src").get()
    #         item["book_img"] = 'https:'+item["book_img"]
    #         item["book_title"] = li.xpath("./div[@class='p-name']/a/em/text()").get()
    #         item["book_hover_title"] = li.xpath("./div[@class='p-name']/a/@title").get()
    #         item["book_price"] = li.xpath("./div[@class='p-price']/strong/i/text()").get()
    #     print(item)

