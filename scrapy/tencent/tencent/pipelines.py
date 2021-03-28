# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

from pymongo import MongoClient
from tencent.items import TencentItem

client = MongoClient()
collection = client['tencent']['hr']


class TencentPipeline:
    def process_item(self, item, spider):
        if isinstance(item, TencentItem):
            print('开始写入数据库start')
            collection.insert(dict(item))
            print('开始写入数据库成功end')
        return item
