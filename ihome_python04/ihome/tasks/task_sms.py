# coding:utf-8


from celery import Celery
from ihome.yuntongxun.sms import CCP

# 定义celery对象
celery_app = Celery("ihome", broker="redis://192.168.0.108:6379/1")


@celery_app.tasks
def send_sms():
    """发送短信的异步任务"""
    ccp = CCP()
    ccp.send_template_sms(to, datas, temp_id )

