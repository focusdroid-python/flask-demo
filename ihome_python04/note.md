###　flask项目分析
    - 1. 分析需求
    - 2. 编写代码
    - 3. 编写单元测试
    - 4. 自测
    - 5. 编写接口文档
        - 
        
### 文档地址
    -  [python-redis](https://redis-py.readthedocs.io/en/latest/)
    - redis http://redisdoc.com/index.html
    - 
    
### 图片服务
    - 1. 保存到本地，扩容(磁盘满的问题)
    - 2. 备份问题
    - 3. 多机存储问题
    - 4. 用户A  图片A
         用户B  图片B
         图片Ａ　与图片Ｂ　是同一张图片，会存放两次，浪费空间
    
    - 5. 用户１　　a.jpg
         用户２　　a.jpg
         同名图片，但不是同一张，后上传会覆盖之前的内容
         
#### 文件存储解决方案
1. 自己搭建文件存储系统　FastDFS 快速分布式文件存储系统　　HDFS Hadoop分布式文件系统
２．选择第三方服务，　七牛云存储  pip install qiniu  // 需要升级pip


### 使用celery
```
使用celery实现异步任务，　

pip install Celery


发布任务的一方
flask
django                      真正执行任务的一方

       任务发送           任务１　　获取任务处理
客户端　　－－－－－－－－>　任务２ <－－－－－－－－－－－－－　　任务处理者（worker）
                        任务３                             多进程
                        rabbitMQ MessageQueue             协程　gevent / greenlet
                        redis

                       第四方，存放结果数据,backend
                        存放worker执行之后的结果，客户端需要结果可以来查询
                         redis / mysql

celery使用方法
send_sms.delay()                                              开启celery worker 
                                                              celery -A定义任务的python模块，　worker -l info
/sms_codes/<re(r'1[34578]\d{9}'):mobile
(flask_py) focusdroid@focusdroid:~/flask/ihome_python04$ celery -A ihome.tasks.task_sms worker -l info


```
