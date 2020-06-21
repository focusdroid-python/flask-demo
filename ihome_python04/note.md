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
２．选择第三方服务，　七牛云存储
