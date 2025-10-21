"""
定义一个高级字符串工具类，具有如下方法:
   将给定字符串反转（传入abcd返回dcba）
"""


# 1 input输入
class StrTools:
    def __init__(self):
        self.str = input('输入一个字符串进行反转: ')

    def reverse(self):
        return self.str[::-1]

s = StrTools()
print(s.reverse())

print('===' * 20)


# 2 传参
class Tools:
    def __init__(self, str1):
        self.str = str1

    def reverse(self):
        return self.str[::-1]

s = Tools('abcd')
print(s.reverse())

