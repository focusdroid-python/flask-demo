# coding:utf-8

# 图片验证码的redis有效期 单位:秒
IMAGE_CODE_REDIS_EXPIRES = 180

# 短信验证码redis有效期,　单位：秒
SMS_CODE_REDIS_EXPIRES = 300

# 发送短信验证码的间隔时间　单位：秒
SEND_SMS_CODE_INTERVAL = 60

# 限制登录错误次数
LOGIN_ERROR_MAX_TIMES = 5

# 登陆错误限制的实现 单位　：秒
LOGIN_ERROR_DORBID_TIME = 600

# 七牛的域名
QUNIU_URL_DOMAIN = "http://qc9evf10t.bkt.clouddn.com/"

# 城区信息的缓存时间, 单位是：秒
AREA_INFO_REDIS_CHCHE_EXPIRES = 7200