# coding:utf-8

li1 = [1,2,3,4,5,6]
# li2 = [5,8,7,6,5,4]
li2 = [5,8]

def add(num1, num2):
    return num1 + num2

ret1 = map(add , li1, li2)


def add_self(num):
    return num + 2
ret2 = map(add_self, li1)

print(ret1)
print(ret2)
print(list(ret1))
print(list(ret2))