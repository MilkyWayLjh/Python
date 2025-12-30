"""
^	匹配字符串开头
$	匹配字符串结尾
^ $ 组合使用-匹配字符开始和结尾
"""
import re

# 限制开始 ^
print(re.search('^hello', 'hello123'))
print(re.search('^hello', 'ahello123'))

# 限制结尾 $
print(re.search('hello$', 'hello123'))
print(re.search('hello$', 'ahello123'))
print(re.search('hello$', 'ahello123hello'))

# ^ 和 $ 结合使用
print(re.search('^hello$', 'hello123'))
print(re.search('^hello$', 'shello'))
print(re.search('^hello$', 'hello'))

# 案例
phone = input('手机号：')

if re.search('^1[3-9]\d{9}$', phone):
    print('手机号格式正确')
else:
    print('手机号格式错误')
