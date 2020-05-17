# coding:utf-8

from werkzeug.routing import BaseConverter


# 定义一个正则转换器
class ReConverter(BaseConverter):
    """"""
    def __init__(self, url_map, regex):
        '''调用父类方法'''
        super(ReConverter, self).__init__(url_map)
        # 保存正则表达式
        self.regex = regex