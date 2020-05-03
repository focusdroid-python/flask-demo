### 
```
格式转换
# str --->   bytes
In [2]: a = '王旭'

In [3]: type(a)
Out[3]: str

In [4]: b = a.encode()

In [5]: type(b)
Out[5]: bytes

In [6]: b.decode()
Out[6]: '王旭'

In [7]: b.decode('utf8')
Out[7]: '王旭'

In [8]: b.decode('utf-8')
Out[8]: '王旭'



```
### 爬虫的概念
- 爬虫是模拟浏览器发送请求，获取响应
### 爬虫的流程
- url ---> 发送请求，　获取响应 ---> 提取数据 ---> 保存
- 发送请求，获取响应 ---> 提取url

```python
import json
t = json.loads("{}")
```
### url形式
```
形式：　scheme://host[:port#]/path/../[?query-string][#anchor]

scheme:协议
host: 服务器的ｉｐ地址
port: 服务器的端口
path： 访问资源的路径
query: 参数
anchor: 锚点
```
### http请求形式
```

```
### 
```
通用爬虫：通常指搜索引擎的爬虫
聚焦爬虫：针对个别网站
```
###爬虫学习　
```
１．基础知识
２．requests的使用
３．数据提取方法
４．动态网页数据
５．scrapy
６．scrapy redis
```
### 爬虫要根据当前url地址对应的响应为准，当前url地址的elements的内容和ｕｒｌ的响应不一样
### 页面上的数据在哪里
　-　当前url地址对应的响应中
　-　其他的url地址对应的响应中
    　-　比如在ajax中
　-　js生成的
    　-　部分数据在响应中
    　-　全部通过

### 浏览器和爬虫获取的数据不一样，因为浏览器有ｊｓ可以修改数据

###　通过ｒｅｑｕｅｓｔs向百度首页发送请求，获取百度首页的数据
```
response = requests.get(url)
断言　assert 假设的意思
assert response.statuc_code == 200
## 为什么要带上header？
模拟浏览器，欺骗浏览器，获取和浏览器一样的内容
header的形式：字典
headers = {
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36
}
用法：　requests.get(url, headers = headers)

In [31]: headers = {"User-Agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.
    ...: 3865.120 Safari/537.36"}

In [32]: response = requests.get("http://www.baidu.com", headers=headers)

In [33]: response.content.decode()

## 发送带参数的请求
参数格式：字典
kw = {'wd': 'focusdroid'}
用法:requests.get(url, params=kw)

```
### 判断请求是否成功
```python
import requests

assert response.status_code == 200

```
### url编码
 - `https://www.baidu.com/?wd=%E7%8E%8B%E6%97%AD`
 
 - `url = "https://www.baidu.com?wd={}".format('王旭')
res = requests.get(url, headers=headers)`

### 字符串格式化的另一种方式
```python
In [37]: "王{}旭".format(1)
Out[37]: '王1旭'

In [38]: "王{}旭".format("a")
Out[38]: '王a旭'

In [39]: "王{}旭".format([1,2,3])
Out[39]: '王[1, 2, 3]旭'

In [40]: "王{}旭{}".format({"a":2})

In [41]: "王{}旭{}".format({"a":2},2)
Out[41]: "王{'a': 2}旭2"

url = "https://www.baidu.com?wd={}".format('王旭')
res = requests.get(url, headers=headers)

print(res.status_code)
print(res.request.url)

```












