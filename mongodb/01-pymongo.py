# -*- coding:utf-8 -*-
from pymongo import MongoClient

# 实例化client，建立连接
client = MongoClient(host="127.0.0.1", port=27017)

collection = client["test"]["t251"]

# 插入一条数据
# ret = collection.insert({'name': 'tree', 'age': 15})
# print(ret)

# 插入多条数据
# data_list = [
#     {"name":"test{}".format(i)} for i in range(10)
# ]
# collection.insert_many(data_list)

# 查询一个数据
# ret1 = collection.find_one()
# print(ret1)

# 查询所有记录
# ret2 = collection.find()
# print(ret2)
# for i in ret2:
#     print(i)

# 更新一条数据
# collection.update_one({'name':'test1'}, {'$set':{'name':'new_test_100'}})

# 更新多条数据
# collection.update_many({'name':'test2'}, {'$set':{'name':'new_test_222'}})


# 删除一条数据
# collection.delete_one({'name':'test1'})

# 删除多条数据
collection.delete_many({'name':'test2'})