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
### 发送post请求
```
用法: resquests.post(url, data, headers)
```
### 使用代理
```
用法: requests.get("https://www.google.com", proxies=proxies，　headers=headers, times=0)
proxies = {
    "http":"http://67.228.221.221",
    "https":"https://67.228.221.221"
}
# 为什么爬虫需要使用代理
１．让服务器以为不是同一个客户端在请求
２．防止我们的真实地址被泄露，防止被追究

- 准备一堆ip地址，组成ip池，随机选择一个ip来使用
- 如何选择代理ip，让使用次数较少的ip地址有更大的可能性被用到
    - {"ip":"ip", "times":"0"}
    - [{},{},{},{}],对这个ip的列表进行排序，按照使用次数进行排序
    - 选择使用次数较少的10个，从中选择一个
- 检查ip可用性
   - 可以使用requests添加超时参数，判断ip地址的质量
   - 
```
### request中的cookie session区别
```
cookie数据存放在客户的浏览器上，session数据放在服务骑上
cookie
携带一堆cookie进行请求，把cookie组成cookie池

```

### 请求登录之后的网站的思路
```
实例化session
先使用session发送请求，登陆网站，把cookie保存在session中
在使用session请求登录之后才能访问的网站，session能够使用自动的携带登陆成功时保存在其中的cookie，进行请求

```
### 不发送post请求，使用cookie获取登录后的页面
```
- cookie过期时间很长的网站
- 在cookie过期之前拿到所有数据
- 配合其他程序一起使用，其他程序专门获取cookie
```
### 字典推导式，列表推导式
```python
cookies = "anonymid=k9s0c65y2om8pj; depovince=GW; _r01_=1; JSESSIONID=abcNfoYyDySYUa1KYbEhx; ick_login=1f120d53-226f-48b0-85aa-6fa23c2aea8f; taihe_bi_sdk_uid=dc98311ffc7de226cb1f79afdd705b6f; taihe_bi_sdk_session=91d2d67ef0387cdfd5c5b98a2adb89de; jebe_key=bf8a72df-0519-4da7-b1df-362082dfd8d0%7C18333670b0ee1f54e006adc80fdd7f23%7C1588568014097%7C1%7C1588568014407; ick=115383c1-78f2-4270-9a54-2136b5ae3d95; wp_fold=0; XNESSESSIONID=3ab59dd30b97; WebOnLineNotice_974361808=1; first_login_flag=1; ln_uact=15701229789; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; jebe_key=bf8a72df-0519-4da7-b1df-362082dfd8d0%7C92e70cb2bde7172939cddc8f15fdd3b4%7C1588570052591%7C1%7C1588570052691; jebecookies=fbd2ce92-afdd-406f-aa64-8c77424f55e6|||||; _de=D5FD513C20B9124F1FF9E00605E6865D; p=f4322106a294e3621012a0b8624141118; t=1c4aeb703428602f1361c3618e467c7e8; societyguester=1c4aeb703428602f1361c3618e467c7e8; id=974361808; xnsid=21d68637; loginfrom=syshome"

cookies = {i.split("=")[0]:i.split("=")[1] for i in cookies.split("; ")}
print(cookies)

[self.url_temp.format(i * 50) for i in range(1000) ]
```

### 获取登录后的页面的三种方式
 - 实例化session,使用session发送post请求，在使用其他获取登录后的页面
 - headers中添加cookie键，值为cookie字符串
 - 在请求方法中添加cookies参数，接受字典形式的cookie，字典形式的cookie中的键是cookie的name对应的值，值是cookie中value对应的值

### 
- requests的底层实现就是urllib
- requests在pytnhon2和python3中通用，方法完全一样
- requests简单易用
- requests能够自动帮助我们解压(gzip等)网页内容
- (requests中文文档)["https://requests.readthedocs.io/zh_CN/latest"]

### requestsw中解决编解码的问题方法
- response.content.decode() 类型: bytes
- response.content.decode("gbk")
- response.text  设置response.eccoding = "utf-8" 类型: str

### requests保存图片
```
with open("a.gif", "wb") as f:
    f.write(response.content)

其中　wb表示二进制文件  
    　w 表示文本文件（字符串文件）
```
### 寻找登录的post地址
- 在from表单中寻找action对应的url地址
    -　post的数据是input标签中的name的值作为键,真正的用户名和密码作为值的字典，post的url地址就是action对应的url地址
    
- 抓包

### 寻找js
- 








