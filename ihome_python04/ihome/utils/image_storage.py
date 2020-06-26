# -*- coding: utf-8 -*-
# flake8: noqa

from qiniu import Auth, put_data
import qiniu.config

# 需要填写你的 Access Key 和 Secret Key
access_key = 'reZVGERsw2iRU5NwhkXyOf5ZSV4_rRhj-z-9sbGZ'
secret_key = '5mf5IraVSQpK532r1wr1yVvISkvCQtMjsatPAIFy'


def storage(file_data):
    """
        上传到七牛
        :Params file_data: 要上传的文件数据
        :return
    """

    # 构建鉴权对象
    q = Auth(access_key, secret_key)

    #要上传的空间
    bucket_name = 'ihome-python004'

    # 生成上传 Token，可以指定过期时间等
    token = q.upload_token(bucket_name, None, 3600)

    ret, info = put_data(token, None, file_data)

    if info.status_code == 200:
        # 表示上传成功,返回文件名
        return ret
    else:
        # 上传失败
        raise Exception("上传七牛服务器失败")
    print(info)
    print("*"*20)
    print(ret)

if __name__ == "__main__":
    with open("./1.jpg", "rb") as f:
        file_data = f.read()
        storage(file_data)