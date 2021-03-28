import scrapy
import urllib

class TbSpider(scrapy.Spider):
    name = 'tb'
    allowed_domains = ['baidu.com']
    start_urls = ['http://tieba.baidu.com/mo/q----.sz@320_240-1-3---2/m?kw=%E6%9D%8E%E6%AF%85&lp=5011']

    def parse(self, response):
        # 根据帖子进行分组
        div_list = response.xpath("//div[contains(@class, 'i')]")
        for div in div_list:
            item = {}
            item['title'] = div.xpath("./a/text()").get()
            item['href'] = div.xpath("./a/@href").get()
            item['img_list'] = []
            if item['href'] is not None:
                # item['href'] = urllib.parse.urljoin(response.url, item['href'])
                yield scrapy.Request(
                    item['href'],
                    callback = self.parse_detail,
                    meta = {"item": item}
                )
        next_url = response.xpath("//a[text()='下一页']/@href").extract_first()
        if next_url is not None:
            urllib.parse.urljoin(response.url, next_url)
            yield scrapy.Request(
                next_url,
                callback=self.parse,
            )

    def parse_detail(self, response):
        item = response.meta['item']
        item['img_list'].extend(response.xpath("//div[@class='i']/a/@href"))

        next_url = response.xpath("//a[text()='下一页']/@href").extract_first()
        if next_url is not None:
            urllib.parse.urljoin(response.url, next_url)
            yield scrapy.Request(
                next_url,
                callback=self.parse_detail,
                meta={"item": item}
            )
        else:
            print(item)
            yield item