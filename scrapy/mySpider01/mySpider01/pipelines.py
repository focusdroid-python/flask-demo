# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import logging

logger = logging.getLogger(__name__)


class Myspider01Pipeline:
    def process_item(self, item, spider):
        if spider.name == "itcast": # 可以使用spider进行判断
        # if item["come_from"] == "itcast":
            logger.warning('-'*10)
        return item



class Myspider01Pipeline2:
    def process_item(self, item, spider):
        if item["come_from"] == "jd":
            pass
        return item
