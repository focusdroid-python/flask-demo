# coding:utf-8

# f = open('./1.txt', 'wb')
# # 2. 向文件写内容
# try:
#     f.write('这是一个测试写入文字')
# except Exception:
#     pass
# finally:
#     f.close()
#

# 上写文管理器
# with open('./1.txt', 'wb') as f:
#     f.write('测试写入文字')
#     f.write('测试写入文字2')
#     f.write('测试写入文字3')
#     f.write('测试写入文字4')
#     f.write('测试写入文字5')

class Foo(object):
    def __enter__(self):
        '''进入with语句的时候被with调用'''
        print('exter called')

    def __exit__(self, exc_type, exc_val, exc_tb):
        '''离开with语句的时候被with调用'''
        print('exc_type %s'% exc_type)
        print('exc_val %s'% exc_val)
        print('exc_tb %s'% exc_tb)
        print('exit called')


with Foo() as foo:
    print('测试文字')
    a = 1 / 0
    print('结束测试！！！')