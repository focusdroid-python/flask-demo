## scrapy

```
sudo update-alternatives --install /usr/bin/python python /usr/bin/python2 100
sudo update-alternatives --install /usr/bin/python python /usr/bin/python3 150

执行上面两句命令即可将2.7版本切换成python3.6版本，想要查看是否切换成功：

shanlei@shanlei-Lenovo-ideapad-110-15ISK:~$ python --version

python3切换成python2
shanlei@shanlei-Lenovo-ideapad-110-15ISK:~$ sudo update-alternatives --config python

```

#### 为什么需要scrapy
- 提高效率，多线程爬取数据

#### 安装scrapy，创建项目
- [scrapy链接](https://scrapy-chs.readthedocs.io/zh_CN/0.24/intro/install.html)
```
安装scrapy框架，安装前python --version
pip install Scrapy

1. 创建一个scrapy项目
    scrapy startproject mySpider
    
2. 生成一个爬虫
    scrapy genspider itcast 'itcast.cn'
  
  # 启动爬虫
  scrapy crawl itcast
  scrapy crawl 爬虫名称
  
  focusdroid@focusdroid:~/flask/scrapy/mySpider$ scrapy crawl itcast
  focusdroid@focusdroid:~/flask/scrapy/mySpider$ scrapy crawl 爬虫名称
    
3. 提取数据
    完善spider，使用xpath等方法
    
4. 保存数据
    pipeline中保存数据

```

### scrapy 获取相关信息的方法
```
1. extract
item["name"] = li.xpath(".//h2/text()").extract()[0]
2. extract_first() 获取第一个
```

### scrapy项目中的配置
```
1. logging
    要让项目打印日志，首先在settings.py中配置日志打印的级别
    LOG_LEVEL = "WARNING" # warning以上的都可以打印
    LOG_FILE = "./log.log" # 保存日志文件存储目录

2. 使用pipelines.py文件中的item，需要在settings.py解注释，才能使用
    ITEM_PIPELINES = {
        'mySpider01.pipelines.Myspider01Pipeline': 300,
    }
````

### python中的日志使用
```
- scrapy 
    - settings中设置LOG_LEVEL="WARNING"
    - settings中设置LOG_FILE="./a.log" # 设置日志保存位置，设置后终端不会显示日志内容
    - import logging,实例化logger的方式在任何文件中使用logger输出内容

- 普通项目中 
    - import logging
    - logging.basicConifg(...) # 设置日志输出样式，格式 
    - 实例化一个logger = logging.getLogger(__name__)
    - 在任何py文件中调用logger
    
    # -*- coding:utf-8 -*-
import logging

# logging.basicConfig() # 日志输出样式

logging.basicConfig(level=logging.INFO,
                    format='levelname:%(levelname)s filename: %(filename)s',
                    datefmt='%a %d %b %Y %H:%M:%S', filename='./my.log', filemode='w')


logger = logging.getLogger(__name__)

if __name__ == '__main__':
    logger.info('this is a info log')
    logger.info('this is a info log1')


```
#### scrapy.Request知识点
```
scrapy.Request(url, [callback, method='GET', headers, body, cookies, meta, dont_filter=False])
注： 一般文档中方括号中的参数表示可选参数
callback： 指定传入的url交给那个解析函数去处理
meta：实现在不同解析函数之间解析数据的，meta默认会携带部分信息，比如下载延迟，请求深度等
dont_filter： 让scrapy的去重不会过滤当前url，scrapy默认有url去重的功能，对需要的重复请求的url有重要用途
```
#### scrapy中的CrawlSpider
- 常见爬虫 scrapy genspiden -t crawl 爬虫名 allow_domain
- 常见的start_url，对应的响应会进过rules提取url地址
- 完善rules，添加Rule`Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True)`
- 注意点：
    - url地址不完整，crawlspider会自动补充完章之后再请求
    - parse函数不能定义，他有特殊的功能需要实现
    - callback：连接提取器提取出来的url地址对应的响应交给他处理
    - follow：连接提取器提取出来的url地址对用的url响应是否继续被rules来过滤

```
生成crawlspider的命令：
    scrapy genspider -t craw csdn "csdn.cn"
    这个可以自动生成分页数据
    LinkExtractor更多常见参数：
    allow：满足括号中正则表达式的URL会被提取
```

### scrapy模拟登陆
- 1. 直接携带cookie（settings.py直接用）
- 2. 找到发送post请求的url地址，带上信息，发送请求
  
- scrapy模拟登陆值携带cookie
  - 应用场景：
    - 1. cookie过期时间很长，常见于一些不规范的网站
    - 2. 能在cookie过期之前把所有的数据拿到
    - 3. 配合其他程序使用比如使用selenium把登录之后的cookie获取到保存到本地，
         scrapy发送请求之前先读取本地cookie

### scrapy中使用cookies
```python
import scrapy
import re
class RenrenSpider(scrapy.Spider):
    name = 'renren'
    allowed_domains = ['renren.com']
    start_urls = ['http://www.renren.com/974361808/profile']


    def start_requests(self):
        cookies = "anonymid=k9s0c65y2om8pj; _r01_=1; taihe_bi_sdk_uid=dc98311ffc7de226cb1f79afdd705b6f; jebe_key=bf8a72df-0519-4da7-b1df-362082dfd8d0%7C92e70cb2bde7172939cddc8f15fdd3b4%7C1588663804895%7C1%7C1588663805116; ick_login=c4088f0e-05b4-45aa-bdf0-9b08f1473ad5; taihe_bi_sdk_session=02916b8090c4c5873f420e06488a9481; ick=2cb82a29-88ff-4992-af3c-666c7117e519; __utmc=151146938; __utmz=151146938.1598678110.1.1.utmcsr=renren.com|utmccn=(referral)|utmcmd=referral|utmcct=/; first_login_flag=1; wpsid=15883893825150; __utma=151146938.1079666667.1598678110.1598678110.1598690302.2; _de=D5FD513C20B9124F1FF9E00605E6865D; _ga=GA1.2.1079666667.1598678110; depovince=GW; jebecookies=9732a44a-efa5-4faf-8686-e74c8b388e0a|||||; p=eda31466730955aa5025a3e80268615f8; ln_uact=15701229789; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; t=2c81d9d01c4857e6bd01807353ee3a3e8; societyguester=2c81d9d01c4857e6bd01807353ee3a3e8; id=974361808; xnsid=a9818e26; ver=7.0; loginfrom=null; wp_fold=0"
        cookies = {i.split("=")[0]:i.split("=")[1] for i in  cookies.split('; ')}

        yield scrapy.Request(
            self.start_urls[0],
            callback=self.parse,
            cookies=cookies
        )

    def parse(self, response):
        print(re.findall("王维", response.body.decode()))
        yield scrapy.Request(
            "http://www.renren.com/974361808/profile?v=info_timeline",
            callback=self.parse_detail
        )

    def parse_detail(self, response):
        print(re.findall("王维", response.body.decode()))

```

### 下载中间件
- 使用方法
  - 编写一个DOenloader Middlewares和我们编写一个pipeline一样，定义一个类，然后在setting中开启
  
- Downliader Middlewares默认的方法
    - process_request(self, request, spider)
      - 当每个request通过下载中间件时，该方法被调用
    - process_response(self, request, response, spider):
      - 当下在器完成http请求，传递响应给引擎的时候调用
    
```python
# 使用随机的user-agent和代理
import random
class RandomUserAgentMiddleware:
    def process_request(self, request, spider):
        ua = random.choice(spider.settings.get("USER_AGENTS_LISTS"))
        request.headers["User-Agent"] = ua
#         添加自定义的UA，给request的headers赋值即可


class CheckUserAgent:
    def process_response(self, request, response, spider):
        # print(dir(response))
        print(request.header["User-Agent"])

class ProxyMiddleware:
    def process_reqiuest(self, request,spider):
        request.meta["proxy"] = "http://124.115.126.14:808"
#           添加代理，需要在request的meta信息中添加proxy字段         
#           代理的形式为：协议+ip地址+端口

```
USER_AGENTS_LISTS = [
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 6.0.1; Moto G (4)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1",
    "Mozilla/5.0 (Linux; Android 8.0.0; Nexus 6P Build/OPP3.170518.006) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 8.0.0; Pixel 2 XL Build/OPD1.170816.004) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Mobile Safari/537.36",
]
```


```
  
- 在settings中放开配置就可以使用下载中间件了
```python
DOWNLOADER_MIDDLEWARES = {
   'login.middlewares.LoginDownloaderMiddleware': 543,
}

```

### scrapy模拟登录之发送post请求
-两种实现自动登录的方式
    - FormRequest 这种参数传入的格式就是字典
    - scrpay.FormRequest.from_response(
        response, - 自动从表单中找到form表单寻找登录地址
        formdata={"email":"user_name", "password":"password"}
        callback=self.parse_page
    )
```python
import scrapy
import re

class GithubSpider(scrapy.Spider):
    name = 'github'
    allowed_domains = ['github.com']
    start_urls = ['https://github.com/login']

    def parse(self, response):
        authenticity_token = response.xpath("//input[@name='authenticity_token']/@value").get()
        webauthn_support = response.xpath("//input[@name='webauthn-support']/@value").get()
        webauthn_iuvpaa_support = response.xpath("//input[@name='webauthn-iuvpaa-support']/@value").get()
        timestamp = response.xpath("//input[@name='timestamp']/@value").get()
        timestamp_secret = response.xpath("//input[@name='timestamp_secret']/@value").get()
        commit = response.xpath("//input[@name='commit']/@value").get()
        post_data = dict(
            login = 'weexss@163.com',
            password = 'Asmie1234',
            timestamp = timestamp,
            timestamp_secret = timestamp_secret,
            commit = commit,
            authenticity_token = authenticity_token,
            webauthn_support = webauthn_support,
            webauthn_iuvpaa_support = webauthn_iuvpaa_support
        )

        yield scrapy.FormRequest(
            self.start_urls[0],
            formdata=post_data,
            callback=self.after_login
        )

    def after_login(self,response):
        with open('a.html', 'w', encoding='utf-8') as f:
            f.write(response.body.decode())
        print(re.findall("asmieuser", response.body.decode()))
```

### 总结
```
苏宁图书爬虫
    - 1. 数据重复怎么办 
    - 2. URL地址js
```

### 网站使用后端模板页面返回数据（后端接口返回数据是另外一种处理方式）
#### scrapy genspider -t crawl tt1 sun0769.com添加自动翻页
```python

# 重中之重就是？和.一定要转义
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class TtSpider(CrawlSpider):
    name = 'tt'
    allowed_domains = ['sun0769.com']
    start_urls = ['http://wzzdg.sun0769.com/political/index/politicsNewest']

    rules = (
        Rule(LinkExtractor(allow=r'/political/index/politicsNewest\?id=1&page=\d+'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = {}
        # item['test'] = '1231313213213123132132132123'
        item['title'] = response.xpath("//ul[@class='title-state-ul']/li/span[@class='state3']/a/text()").extract_first()
        item['status'] = response.xpath("//ul[@class='title-state-ul']/li/span[@class='state2']/text()").extract_first()
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        # return item
        print(item)
```
### 学习scrapy——redis
- 1. 为什么要学习scrapy_redis
    - scrapy_redis在scrapy的基础上实现了更多，更强大的功能，具体体现在，request去重，爬虫持久化，和轻松实现分布式

    
```
redis常用命令
/etc/init.d/redis-server stop redis 停止
/etc/init.d/redis-server start redis 启动
/etc/init.d/redis-server restart redis重启

 reids-cli -h <hosrname> -p <port> 远程连接redis数据库
 
 redis中
 select 1  切换到db1， 默认在db0
 keys *    查看所有的redis键
 type '键' 查看键的数据类型
 flushdb   清空当前db
 flushall  清空所有db
 http://www.redis.cn/commands.html

复习redis的使用
列表:
LPUSH mylist "world"
LRANGE mylist 0 -1
LLEN mylist

set：
SADD myset "HELLO"
SMEMBERS myset
SCARD myset
```
- scrapy-redis 使用案例 https://github.com/rmax/scrapy-redis
```python
# settings.py


SPIDER_MODULES = ['example.spiders']
NEWSPIDER_MODULE = 'example.spiders'

USER_AGENT = 'scrapy-redis (+https://github.com/rolando/scrapy-redis)'

DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"  # 指定那个去重方法给request对象去重
SCHEDULER = "scrapy_redis.scheduler.Scheduler" # 指定scheduler队列
SCHEDULER_PERSIST = True # 队列中的内容是否是持久保存，为False的时候还在关闭redis的时候清空redis
#SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderPriorityQueue"
#SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderQueue"
#SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderStack"

ITEM_PIPELINES = {
    'example.pipelines.ExamplePipeline': 300,
    # 'scrapy_redis.pipelines.RedisPipeline': 400, # scrapy_redis实现的items保存到redis的pipeline
}

LOG_LEVEL = 'DEBUG'

# Introduce an artifical delay to make use of parallelism. to speed up the
# crawl.
DOWNLOAD_DELAY = 1

REDIS_URL= "redis://127.0.0.1:6379" # 指定redis地址

# REDIS_HOST = '127.0.0.1'
# REDIS_PORT = 6379
```
### Crontab爬虫定时执行
```

```


















