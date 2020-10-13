# coding=utf-8
from CCPRestSDK import REST

#主帐号
accountSid= '8aaf07087249953401728cd13b4420f1';

#主帐号Token
accountToken= '16ef490ff19044788942064de145d1e8';

#应用Id
appId='8aaf07087249953401728cd13c4a20f8';

#请求地址，格式如下，不需要写http://
serverIP='app.cloopen.com';

#请求端口 
serverPort='8883';

#REST版本号
softVersion='2013-12-26';

  # 发送模板短信
  # @param to 手机号码
  # @param datas 内容数据 格式为列表 例如：['12','34']，如不需替换请填 ''
  # @param $tempId 模板Id

class CCP(object):
    """自己封装发送短信的类属性"""
    # 用来保存类属性
    instance = None

    def __new__(cls):
        # 判断ＣＣＰ类有没有已经创建好的对象，如果没有，创建一个对象，并且保存
        # 如果有，则保存的对象直接返回
        if cls.instance is None:
            obj = super(CCP, cls).__new__(cls)

            # 初始化REST SDK
            obj.rest = REST(serverIP, serverPort, softVersion)
            obj.rest.setAccount(accountSid, accountToken)
            obj.rest.setAppId(appId)

            cls.instance = obj

        return cls.instance


    """自己封装的发送短信的辅助类"""

    # sendTemplateSMS(手机号码,内容数据,模板Id)
    def send_template_sms(self, to, datas, temp_id):
        result = self.rest.sendTemplateSMS(to, datas, temp_id)
        status_code = result.get("statusCode")
        if status_code == "000000":
            # 表示短信发送成功
            return 0
        else:
            # 表示发送失败
            return -1

if __name__ == "__main__":
    ccp = CCP()
    ret = ccp.send_template_sms("15701229789", ["1234", "5"], 1)
    print(ret)