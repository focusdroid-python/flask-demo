#coding=gbk

#coding=utf-8

#-*- coding: UTF-8 -*-  

from CCPRestSDK import REST
import ConfigParser

#���ʺ�
accountSid= '8aaf07087249953401728cd13b4420f1';

#���ʺ�Token
accountToken= '16ef490ff19044788942064de145d1e8';

#Ӧ��Id
appId='8aaf07087249953401728cd13c4a20f8';

#�����ַ����ʽ���£�����Ҫдhttp://
serverIP='app.cloopen.com';

#����˿� 
serverPort='8883';

#REST�汾��
softVersion='2013-12-26';

  # ����ģ�����
  # @param to �ֻ�����
  # @param datas �������� ��ʽΪ�б� ���磺['12','34']���粻���滻���� ''
  # @param $tempId ģ��Id

class CCP(object):
    """�Լ���װ���Ͷ��ŵ�������"""
    # ��������������
    instance = None

    def __new__(cls):
        # �жϣãã�����û���Ѿ������õĶ������û�У�����һ�����󣬲��ұ���
        # ����У��򱣴�Ķ���ֱ�ӷ���
        if cls.instance is None:
            obj = super(CCP, cls).__new__(cls)

            # ��ʼ��REST SDK
            obj.rest = REST(serverIP, serverPort, softVersion)
            obj.rest.setAccount(accountSid, accountToken)
            obj.rest.setAppId(appId)

            cls.instance = obj

        return cls.instance


    """�Լ���װ�ķ��Ͷ��ŵĸ�����"""
    def send_template_sms(self, to, datas, temp_id):
        result = self.rest.sendTemplateSMS(to, datas, temp_id)
        # for k, v in result.iteritems():
        #     if k == 'templateSMS':
        #         for k, s in v.iteritems():
        #             print('%s:%s' % (k, s))
        #     else:
        #         print('%s:%s' % (k, v))
        status_code = result.get("statusCOde")
        if status_code == "000000":
            # ��ʾ���ŷ��ͳɹ�
            return 0
        else:
            # ��ʾ����ʧ��
            return 1

if __name__ == "__main__":
    ccp = CCP()
    ret = ccp.send_template_sms("15701229789", ["1234", "5"], 1)
    print(ret)
# ccp = CCP()
# ccp.send_template_sms()
# ccp.send_template_sms()
# ccp.send_template_sms()
#
#
# ccp2 = CCP()


#sendTemplateSMS(�ֻ�����,��������,ģ��Id)