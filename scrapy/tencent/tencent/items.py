# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TencentItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    CategoryName = scrapy.Field()
    LastUpdateTime = scrapy.Field()
    PostURL = scrapy.Field()
    CountryName = scrapy.Field()
    LocationName = scrapy.Field()
    RecruitPostName = scrapy.Field()
    BGName = scrapy.Field()

class JDItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    CategoryName = scrapy.Field()
    LastUpdateTime = scrapy.Field()
    PostURL = scrapy.Field()
    CountryName = scrapy.Field()
    LocationName = scrapy.Field()
    RecruitPostName = scrapy.Field()
    BGName = scrapy.Field()


class YAMAXUNItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    CategoryName = scrapy.Field()
    LastUpdateTime = scrapy.Field()
    PostURL = scrapy.Field()
    CountryName = scrapy.Field()
    LocationName = scrapy.Field()
    RecruitPostName = scrapy.Field()
    BGName = scrapy.Field()
