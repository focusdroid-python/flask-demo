# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class YangguangItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    id = scrapy.Field()
    state = scrapy.Field()
    title = scrapy.Field()
    href = scrapy.Field()
    sleepTime = scrapy.Field()
    time = scrapy.Field()
    content_title = scrapy.Field()
    content_img = scrapy.Field()
    content = scrapy.Field()

