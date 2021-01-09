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





















