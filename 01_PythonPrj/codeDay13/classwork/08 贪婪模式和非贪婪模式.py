"""
● 贪婪模式
    贪婪模式在整个表达式匹配成功的前提下，尽可能多的匹配。正则默认就是贪婪模式
● 非贪婪模式
    在修饰匹配次数的特殊符号后再加上一个?问号，则可以使匹配次数不定的表达式尽可能少的匹配
"""
import re

# 贪婪模式 (默认)
print(re.search('\w+go', '你好123goodgo'))


# 非贪婪模式  \w   {1,}
# 贪婪
print(re.search('你\w+', '你好kfjsdklsfdjklf'))
# 非贪婪
print(re.search('你\w+?', '你好kfjsdklsfdjklf'))
# 贪婪
print(re.search('\w+', '你好kfjsdklsfdjklfjad'))
# 非贪婪
print(re.search('\w+?', '你好kfjsdklsfdjklfjad'))


# 案例
str1 = '<html><head></head><body><h1>标题</h1></body></html>'
# 贪婪
print(re.search('<.+>', str1))
# 非贪婪
print(re.search('<.+?>', str1))

