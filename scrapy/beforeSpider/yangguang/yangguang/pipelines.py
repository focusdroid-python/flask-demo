# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import re
from pymongo import MongoClient

class YangguangPipeline:
    def open_spider(self, spider):
        # spider.hello = 'world'
        client = MongoClient()
        self.collention = client["test"]["test"]

    def process_item(self, item, spider):
        item['content'] = self.process_content(item['content'])
        print(item)
        return item

    def process_content(self, content):
        # 清洗数据
        content = [re.sub(r"\n|\s",'',i) for i in content]
        content = [i for i in content if len(i) > 0] # q去除列表中的空字符串
        return content

