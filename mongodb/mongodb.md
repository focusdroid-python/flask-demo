### mongodb数据库
```
# > 易扩展: NoSQL
# > 大数据量,高性能
# 灵活的数据模型

1.
# sudo apt-get install -y mongodb-org
sudo apt-get install mongodb
https://docs.mongodb.com/manual/tutorial/install-mongodb-on-ubuntu

mongodb -help

# sudo service mongod start
# sudo service mongod stop
# sudo service mongod restart
#查看是否启动成功 ps ajx|grep mongod
#配置文件的位置 /etc/mongod.conf
# 默认端口 27017
# 日志位置: /var/log/mongodb/mongod.log
# 

2.
# 解压
# tar -zvf mongodb-linux-x86_640ubuntu18.04-3.40.tgz
# 移动到/usr/local
# sudo mv -r mongodb-linux-x86_640ubuntu18.04-3.40/ /usr/local/mongodb
# 将可执行文件添加到Path路径中 
# export PATH=/usr/local/mongodb/bin:$PATH
# 启动 mongod --config /usr/local/mongodb/mongod.conf




 #启动数据库  mongo
# mongod -help
# exit or ctrl+c


# 关于database的基础命令
# 当前所在的数据库: db
show dbs
# 查看所有的数据库 show db /show databases

# 切换数据库 use db_name

# 删除当前的数据库 db.dropDatabase()

## 关于集合的基础命令
# 不手动创建集合
# 向不存在的集合第一次加入数据,集合会被创建出来
# 手动创键集合:
# db.createCollection(name, options)
# db.createCollection("stu")
# db.createCollection("sub",{capped: true, size:10})
# 参数capped: 默认值为false表示不设置上限
# 参数size: 当capped的  true,需要指定此参数表示上限大小,当文档达到上限,    qiandeshujuhuibeifugai
查看集合 show collections
删除集合 db.集合名称.drop()


ObjectID
String
Boolean
Integer
Double
Arrays
Object
Null
Timestamp
Date

插入
db.集合.insert(focument)
db.stu.insert({name:'tree', age: 18})
db.stu.insert({_id: ObjectId("5fcb65a2e754f8ed43cb01fb"),name:'tree', age: 18})
插入文档时,如果不指定_id参数的时候,mongDB会成为文档分配一个唯一的ObjectId

保存
db.集合.save(document)
如果文档的_id已经存在则修改,如果文档的_id不存在则添加

```

### mongodb插入数据
- db.collection.insert({}) 插入数据,_id存在就报错
- db.collection.save({}) 插入数据,覆盖之前已经存在的id

### 查询数据
- db.collection.find()
- 
### 更新
- db.集合名称.update(<query>,<update>,{multi:<blloean>})
- query  查询条件
- update 更新操作符
- multi  可选,默认是false,表示只更新找到的第一条记录,值为true表示把满足条件的文档全部更新
- 修改name为002的数据替换为{name:"000"}
    db.test100.update({name: "002"},{name:"000"})
- 把name为000的数据name的值更新为张三
    db.test100.update({name: "000"},{$set:{name:"张三"}})
### 删除
- db.集合名称.remove(<query>,{justOne:<boolean>})
- query: 删除的文档的条件
- justOne: 如果设置为true或1,则只删除一条,默认false,表示删除多条

### 数据查询(高级)
- find()
    db.集合名称.find({条件文档})
- findOne() 查询, 只返回第一个
    db.集合名称.findOne({条件文档})
- pretty() 将结果格式化
    db.集合名称.find({条件文档}.pretty)
    
- 等于 默认是等于判断,没有运算符
- 小于 $lt
- 小于等于 $lte
- 大于 $gt
- 大于等于 $gte
- 不等于 $ne
- db.stu.find({age:{$gte:18}})
- 范围运算符
- $in
- db.stu.find({age:{$in:[18,28,38]}})

- and
    查询年龄大于或等于18,并且性别为true的学生,
    db.stu.find({age:{$gte:18}, address: ''})
- or
    查询年龄大于18,或性别为false的学生
    db.stu.find({$or:[{age:{$gt:18}},{address:''}]})
- 
    查询年龄大于18的学生性别为男生,并且名字是gr
    db.stu.find({$or:[{age:{$gte:18}}, {address: '''}], name:'gr'})
    
- 正则表达式
    db.products.find({sku: /^abc/})
    db.products.find({sku: {$regex: '789$'}})
- limit() 用于读取指定数量的文档
    db.集合名称.find().limit(number)

- skip() 用于跳过指定数量的文档
    db.集合名称.find().skip(number)
   
- 自定义查询
    使用$where后面写一个函数,返回满足条件的数据
    db.sty.find({
        $where:function(){
            return this.age>30;
        }
    })
- 投影
    在查询到的返回结果中只选择必要的字段,
    参数字段与值,值为1表示显示,值为0表示不显示
    特殊: 对于_id默认是显示的,如果不显示明确设置为0
    db.stu.find({},{_id:0,name:1,gender:1})
- 排序
    1 升序   -1降序
    db.stu.find().sort({gender:-1,age:1})
- 统计个数
    
    db.stu.find({条件}).count()
    db.stu.find({age:{$gte:18}}).count()
    db.stu.count({age:{$gt:20},address:'桃花岛'})
- 消除重复
    db.集合名称.distinct('去重字段',{条件}')
    db.stu.distinct('address',{age:{$gte:30}}')
    
    
### 编辑器写mongodb语句
```mongodb
db.stu.find(
{$or:[{},{},{}]}
)
```

### mongodb数据库备份恢复
```
mongodump -h dbhost -d dbname -o dbditectory
-h: 服务器地址,也可以指定端口号
-d: 需要备份的数据库名称
-o: 备份的数据存放位置,此目录中存放着备份出来的数据

mongodump -h 192.168.0.109:27017 -d test1 -o ~/Desktop/text1bak

- 数据库的恢复
mongorestore -h dbhost -d dbname --dir dbfirectory
-h: 服务器地址 
-d: 需要恢复的数据库实例
--dir: 备份数据所在位置
focusdroid@focusdroid:~/mondodbtest$ mongorestore -d test --dir ./
mongorestore -h 192.168.0.109:27017 -d test --dir 路径

```
### mongodb聚合
```
- 聚合是基于数据处理的聚合管道,每个文档通过一个由多个极端组成的管道,可以对每个阶段进行分组/过滤等功能,然后经过一系列处理,输出响应的结果,

- db.集合名称.aggregat(管:{表达式}道
db.stu.aggregate({
    {$match: {status: "A"}},
    {$group: {_id: "$cust_id", total: {$sum:"$amount"}}}
})
```
-  常用管道
    $group  将集合中的文档分组,可用于统计结果
    $match  过滤数据,只输出符合条件的文档
    $project  修改输入文档的结构,如重命名/增加/删除字段/创建计算结果
    $sort  将输入文档排序后输出
    $limit  限制聚合管道返回的文档数
    $skip  跳过指定数量的文档,并返回余下的文档
    $unwind  将数组类型的字段进行拆分
    { "_id" : 1, "item" : "t-shirt", "size" : [ "S", "M", "L" ] }
> db.ts.aggregate({$unwind:"$size"})

    $unwind  将数组类型的字段进行拆分(preserveNullAndEmptyArrays:true 表示保留属性值为空的文档)
例子
db.invertory.aggregate({
    path:'$字段名称',
    preserveNullAndEmptyArrays:  <boolean>    # 防止数据丢失
})
> db.din.aggregate({$unwind:'$size'})
{ "_id" : ObjectId("5fd4677cc0cf6fde2502f0e8"), "id" : 1, "item" : "a", "size" : "A" }
{ "_id" : ObjectId("5fd4677cc0cf6fde2502f0e8"), "id" : 1, "item" : "a", "size" : "B" }
{ "_id" : ObjectId("5fd4677cc0cf6fde2502f0e8"), "id" : 1, "item" : "a", "size" : "C" }
{ "_id" : ObjectId("5fd4677cc0cf6fde2502f0e8"), "id" : 1, "item" : "a", "size" : "D" }
{ "_id" : ObjectId("5fd4677cc0cf6fde2502f0ea"), "id" : 3, "item" : "c", "size" : "M" }
{ "_id" : ObjectId("5fd4677cc0cf6fde2502f0ed"), "id" : 6, "item" : "a", "size" : null }
> db.din.aggregate({$unwind:{path:'$size', preserveNullAndEmptyArrays:true}})
{ "_id" : ObjectId("5fd4677cc0cf6fde2502f0e8"), "id" : 1, "item" : "a", "size" : "A" }
{ "_id" : ObjectId("5fd4677cc0cf6fde2502f0e8"), "id" : 1, "item" : "a", "size" : "B" }
{ "_id" : ObjectId("5fd4677cc0cf6fde2502f0e8"), "id" : 1, "item" : "a", "size" : "C" }
{ "_id" : ObjectId("5fd4677cc0cf6fde2502f0e8"), "id" : 1, "item" : "a", "size" : "D" }
{ "_id" : ObjectId("5fd4677cc0cf6fde2502f0e9"), "id" : 2, "item" : "b" }
{ "_id" : ObjectId("5fd4677cc0cf6fde2502f0ea"), "id" : 3, "item" : "c", "size" : "M" }
{ "_id" : ObjectId("5fd4677cc0cf6fde2502f0eb"), "id" : 4, "item" : "d" }
{ "_id" : ObjectId("5fd4677cc0cf6fde2502f0ec"), "id" : 5, "item" : "e", "size" : null }
{ "_id" : ObjectId("5fd4677cc0cf6fde2502f0ed"), "id" : 6, "item" : "a", "size" : null }




db.din.insert([
    {id: 1, item:'a', size: ['A','B','C','D']},
    {id: 2, item:'b', size: [   ]},
    {id: 3, item:'c', size:  'M'},
    {id: 4, item:'d'},
    {id: 5, item:'e', size: null},
    {id: 6, item:'a', size: [null]},
])

    db.ts.aggregate({$match:{username:'tree'}},{$unwind:'$rags'},{$group:{_id:null,sum:{$sum:1}}})

    
    $sum 计算总和 $sum:1 表示以一倍计数
    $avg  计算平均值
    $min  获取最小值
    $max  获取最大值
    $push  在结果文档中插入值到一直数组中
    $first  根据资源文档的排序获取第一个文档数据
    $last  根据资源文档的排序获取最后一个文档数据
    db.stu.aggregate({
        $group:{_id: "address"}
    })
      
- 
- 
- 

### mongodb索引
```
索引: 以提升查询速度

测试: 插入10万条数据到数据库中

for(i = 0;i<100000;i++){
    db.t256.insert({name:'test'+i, age:i})
}
db.t1.find({name: 'test10000'})
db.t1.find({name: 'test10000'}).explain('executionStats')


建立索引的对比
语法：db.集合.ensureIndex({属性：1})，，1表示升序，-1表示降序
具体操作：db.t1.ensureIndex({name:1})
db.t1.find({name:'test100000'}).explain('executionStats')
sort操作的时候指定升序或者降序没有区别，只是相对于sort效果会好点

在默认情况下索引字段的值可以相同
1. 创建唯一索引（索引的值是唯一的）
db.t1.exsureIndex({name:1},{unique: true})
2. 建立联合索引（什么时候需要联合索引）【多个字段判断唯一数据的可以使用联合索引】
db.t1.exsureIndex({name:1,age:1})
3. 查看当前集合的所有索引
db.t2.getINdexes()
4. 删除索引
db.t1.dropIndex('索引名称')

```

### 爬虫数据去重，实现增量式爬虫
- 使用数据库建立关键字段（一个或多个）索引进行去重，
  
- URL地址进行去重，
  - 使用场景：
      - url地址对应的数据不会变的情况,url地址能够唯一判别一个条数据的情况
  - 思路：    
      - url存在redis中
      - 拿到url地址，判断url在redis的url的集合中是存在的
      - 存在：说明url已经请求国，不在请求
      - 不存在：url没有被请求过，请求，把该url存入redis的集合中
  - 布隆过滤器：
    - 使用多个加密算法url地址，得到多个值
    - 往对应值的位置把结果设置为1
    - 新来一个url地址，一样通过加密算法生成多个值
    - 如果对应值位置的值全为1，说明这个url地址已经抓过
    - 否则没有抓过，把对应的位置的值设置为1
    - 
- 数据本身进行去重
- 选择特定的字段，使用加密算法（MD5，sha1）讲字段记性加密，生成字符串，存入redis集合
- 后续新来一条数据，同样的方法机型加密，如果得到的字符串在redis中存在，说明数据存在，对数据进行更讯，否则说明数据不存在，直接插入
    
    
### 在python中使用mongodb
```python
from pymongo import MongoClict
# pip install pymongo 安装pymongodb

class TestMongo:
    def __init__(self):
        pass
        
```
```
# pip install pymongo 安装pymongodb
# -*- coding:utf-8 -*-
from pymongo import MongoClient

# 实例化client，建立连接
client = MongoClient(host="127.0.0.1", port=27017)

collection = client["test"]["t251"]

# 插入一条数据
# ret = collection.insert({'name': 'tree', 'age': 15})
# print(ret)

# 插入多条数据
data_list = [
    {"name":"test{}".format(i)} for i in range(10)
]
collection.insert_many(data_list)

```
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    


