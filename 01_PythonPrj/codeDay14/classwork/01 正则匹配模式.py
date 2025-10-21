# 匹配模式	        描述
# re.I (Ignore)	    使匹配对大小写不敏感，也就是不区分大小写的模式
# re.S (Space)	    使 . 这个通配符能够匹配包括换行在内的所有字符，针对多行匹配
import re

# re.I
print(re.search('Hello', 'hello world hello python'))
list1 = re.findall('Hello', 'hello world hello python', re.I)
print(list1)

# re.S
print(re.search('hello.world', 'hello\nworld', re.S).group())

