# -*- coding: utf-8 -*-
# flake8: noqa
from qiniu import Auth, put_data, etag
import qiniu.config

#需要填写你的 Access Key 和 Secret Key
access_key = 'reZVGERsw2iRU5NwhkXyOf5ZSV4_rRhj-z-9sbGZ'
secret_key = '5mf5IraVSQpK532r1wr1yVvISkvCQtMjsatPAIFy'


def storage(file_data):
    """
    上传文件到七牛
    :param file_data 要上传的文件数据
    :return:
    """
    #构建鉴权对象
    q = Auth(access_key, secret_key)

    #要上传的空间
    bucket_name = 'ihome-python004'

    #上传后保存的文件名
    # key = 'my-python-logo.png'
    key = None

    #生成上传 Token，可以指定过期时间等
    token = q.upload_token(bucket_name, key, 3600)

    #要上传文件的本地路径
    # localfile = './sync/bbb.jpg'

    ret, info = put_data(token, key, file_data)

    print(info)
    print("*"*20)
    print(ret)

    if info.status_code == 200:
        # 表示上传成功, 返回文件名
        return ret.get("key")
    else:
        # 上传失败
        raise Exception("上传图片服务器失败")



if __name__ =="__main__":
    with open("./0.jpg", "rb") as f:
        file_data = f.read()
        storage(file_data)