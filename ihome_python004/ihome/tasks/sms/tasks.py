# -*- coding:utf-8 -*-

from ihome.tasks.main import celery_app
from ihome.yuntongxun.sms import CCP

@celery_app.task
def send_sms(to, datas, temp_id):
    """发送短信的异步任务
    celery -A ihome.tasks.task_sms worker -l info
    """
    ccp = CCP()
    ccp.send_template_sms(to, datas, temp_id)