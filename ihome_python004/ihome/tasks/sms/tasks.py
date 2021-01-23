# -*- coding:utf-8 -*-

from ihome.tasks.main import celery_app
from ihome.yuntongxun.sms import CCP

@celery_app.task
def send_sms(to, datas, temp_id):
    """发送短信的异步任务
    celery -A ihome.tasks.task_sms worker -l info
    可以把发送短信的模块和异步任务单独独立出来也是可以使用的
    """
    ccp = CCP()
    return ccp.send_template_sms(to, datas, temp_id)