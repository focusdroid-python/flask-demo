# -*- coding:utf-8 -*-
from . import api


@api.route("/get_image_code/<image_code_id>")
def get_image_code(image_code_id):
    """
    获取图片验证码
    :param image_code_id: 图片验证码编号
    :return:　验证码图片
    """
    # 获取参数
    # 检验参数
    # 业务逻辑处理，生成验证码操作
    # 将验证码真实值与编号存到redis中
    # 返回值
    return 'get_image_code'
