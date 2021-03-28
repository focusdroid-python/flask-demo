# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class YangguangItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    id = scrapy.Field()
    title = scrapy.Field()
    href = scrapy.Field()
    public_date = scrapy.Field()
    sleep_date = scrapy.Field()
    contnet_img = scrapy.Field()
    content = scrapy.Field()

