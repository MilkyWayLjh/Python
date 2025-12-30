"""
代码	    功能
.	    匹配任意1个字符（除了\n）
[ ]	    匹配[ ]中列举的字符[0-9][a-z][A-Z][\u4e00-\u9fa5]
\d	    匹配数字，即0-9
\D	    匹配非数字，即不是数字
\s	    匹配空白，即 空格，tab键, \n
\S	    匹配非空白
\w	    匹配非特殊字符，即a-z、A-Z、0-9、_、汉字
\W	    匹配特殊字符，即非字母、非数字、非汉字、非下划线
"""
import re

# 原字符：匹配原生字符
# 元字符：具有特殊含义的字符

# 原字符
print(re.search('a', 'bag').group())
print(re.search('c', 'bag'))  # 匹配不到
print('===' * 20)

# .	匹配任意1个字符（除了\n）
print(re.search('.he', 'jfk-helsj'))
print(re.search('.ls', 'jfkdh=lsj'))
print(re.search('.kd', 'j kdhelsj'))
print(re.search('.helj', 'jfkdhelsj'))  # 匹配不到
print(re.search('.he', 'jfk\nhelsj'))  # 匹配不到
print('===' * 20)

# [ ]	匹配[ ]中列举的一个字符[0-9][a-z][A-Z][\u4e00-\u9fa5] (汉字)
print(re.search('[abcd]go', 'fdskljcgokl'))
print(re.search('[abcd]go', 'fdskljagokl'))
print(re.search('[abcd]go', 'fdskljdgokl'))
print(re.search('[abcd]go', 'fdskljbgokl'))
print(re.search('[abcd]go', 'fdskljegokl'))  # 匹配不到
print(re.search('[0-9]go', 'fdsklj6gokl'))
print(re.search('[a-z]go', 'fdskljbgokl'))
print(re.search('[A-Z]go', 'fdskljFgokl'))
print(re.search('[\u4e00-\u9fa5]go', 'fdsklj好gokl'))
print(re.search('.go', 'fdsklj𰻞gokl'))
print('===' * 20)

# \d	匹配数字，即0-9   [0-9]
print(re.search('\dgo', '1go'))
print(re.search('\dgo', '6go'))
print(re.search('\dgo', '-go'))  # 匹配不到
print('===' * 20)

# \D	匹配非数字，即不是数字
print(re.search('\Dgo', '1go'))  # 匹配不到
print(re.search('\Dgo', '6go'))  # 匹配不到
print(re.search('\Dgo', '-go'))
print('===' * 20)

# \s	匹配空白，即 空格，tab键, \n
print(re.search('\sgo', 'ab go'))
print(re.search('\sgo', 'ab go'))
print(re.search('\sgo', 'ab\ngo'))
str1 = '''
go
'''
print(re.search('\sgo', str1))
print('===' * 20)

# \S	匹配非空白
print(re.search('\Sgo', 'ab go'))   # None
print(re.search('\Sgo', 'ab go'))   # None
print(re.search('\Sgo', 'ab\ngo'))  # None
str1 = '''
    go
'''
print(re.search('\Sgo', str1))  # None
print('===' * 20)

# \w	匹配非特殊字符，即a-z、A-Z、0-9、_、汉字  [a-zA-Z0-9_\u4e00-\u9fa5]
print(re.search('\wgo', '1go'))
print(re.search('\wgo', 'ago'))
print(re.search('\wgo', 'Bgo'))
print(re.search('\wgo', '_go'))
print(re.search('\wgo', '号go'))
print(re.search('\wgo', '-go'))  # 匹配不到
print('===' * 20)

# \W	匹配特殊字符，即非字母、非数字、非汉字、非下划线
print(re.search('\Wgo', 'ago'))  # 匹配不到
print(re.search('\Wgo', '1go'))  # 匹配不到
print(re.search('\Wgo', '号go'))  # 匹配不到
print(re.search('\Wgo', '_go'))  # 匹配不到
print(re.search('\Wgo', '&go'))
print(re.search('\Wgo', '~go'))
print(re.search('\Wgo', '@go'))
print(re.search('\Wgo', '$go'))
print(re.search('\Wgo', '^go'))
print('===' * 20)
