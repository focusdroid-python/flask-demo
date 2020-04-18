# coding:utf-8

from flask import Flask
from flask_mail import Mail, Message


app = Flask(__name__)

# 配置邮件：　服务器 / 端口 / 传输层安全协议 / 邮箱名 / 密码
app.config.update(
    DEBUG=True,
    MAIL_SERVER='smtp.qq.com',
    MAIL_PORT=465,
    MAIL_USE_TLS = True,
    MAIL_USERNAME = '840254112@qq.com',
    MAIL_PASSWORD = 'Wangxu19940412'
)

mail = Mail(app)

@app.route('/')
def index():
    # sender　发送方，　recipients接收方列表 
    msg = Message('This is test', sender='840254112@qq.com', recipients=['focusdroid@163.com'])

    # 邮件内容
    msg.body = 'Flask test mail'

    # 发送邮件
    mail.send(msg)
    print('mail sent')
    return 'sent success'



if __name__ == '__main__':
    app.run(debug=True)