#coding:utf-8

import unittest
from login import app
import json


class LoginTest(unittest.TestCase):
    """构造单元测试案例"""
    def setUp(self):
        """在执行其他函数之前先执行这个"""
        # 设置flask工作在测试模式下
        app.config['TESTING'] = True

        app.testing = True


        # 创建进行web请求的客户端，使用flask提供的
        self.client = app.test_client()

    def test_empty_user_name_password(self):
        '''测试用户名密码不完整的情况'''

        # 利用client客户端模拟发送web请求
        # ret = client.post('/login', data={})
        ret = self.client.post('/login', data={'user_name':'admin','password':'python'})

        # ret是试图返回的响应对象
        res = ret.data

        # 因为login试图返回的是ｊｓｏｎ字符串
        resp = json.loads(res)
        print(resp)

        # 拿到返回值之后进行断言测试
        self.assertIn('code', resp)
        self.assertEqual(resp['code'], 1)

    def test_wrong_user_name_password(self):
        """测试用户名或密码错误"""
        ret = self.client.post('/login', data={"user_name":"itcase", "password":"123"})
        # ret是试图返回的响应对象
        res = ret.data

        # 因为login试图返回的是ｊｓｏｎ字符串
        resp = json.loads(res)
        print(resp)

        # 拿到返回值之后进行断言测试
        self.assertIn('code', resp)
        self.assertEqual(resp['code'], 1)


if __name__ == '__main__':
    unittest.main()