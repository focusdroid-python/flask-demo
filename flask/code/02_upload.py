# coding:utf-8

from flask import Flask, request

app = Flask(__name__)

@app.route('/index')
def index():
    return 'test'

@app.route('/upload', methods=['POST'])
def upload():
    '''文件上传'''
    file_obj = request.files.get('pic')
    if file_obj is None:
        # 表示没有发送文件
        return '未上传文件'

    # #将文件保存到本地
    # # 创建一个文件
    # f = open('./demo.png', 'wb')
    # # 2. 向文件写内容
    # data = file_obj.read()
    # f.write(data)
    # # 3. 关闭文件
    # f.close()
    # return '上传成功'

    # 直接使用上传的对象保存
    file_obj.save('./demo.png')
    return '上传成功服务器已经保存'





if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)