### manage.py全局启动文件
### config.py　全局配置文件
### ihome 应用目录
    - 
### 生成数据库迁移文件
    * 首先的安装python-migrate这个包
    - python manage.py db init
    - python manage.py db migrate -m 'init table' # 这里注意一定要先导入modules这个文件，不然系统不知道这个文件就不会生成迁移文件
    -　 python manage.py db upgrade　升级一下 
    - 