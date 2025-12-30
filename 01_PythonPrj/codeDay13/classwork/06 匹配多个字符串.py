"""
匹配多个字符
代码	        功能
*	        匹配前一个字符出现0次或者无限次 {0,}
+	        匹配前一个字符出现1次或者无限次 {1,}
?	        匹配前一个字符出现1次或者0次 {0,1}
{m}	        匹配前一个字符出现m次
{m,n}	    匹配前一个字符出现从m到n次
{m,}	    匹配前一个字符至少出现m次
注意: 大括号里面不能有空格
"""
import re

# 1   * 匹配前一个字符出现0次或者无限次  {0,}
print(re.search('a*go', 'go'))
print(re.search('a*go', 'ago'))
print(re.search('a*go', 'aago'))
print(re.search('a*go', 'aaago'))
print('===' * 20)

# 2   + 匹配前一个字符出现1次或者无限次  {1,}
print(re.search('\w+go', '_go'))
print(re.search('\d+go', '098898go'))
print(re.search('\s+go', ' \n\tgo'))
print(re.search('\S+go', '===go'))
print(re.search('[a-z]+go', 'fsdgo'))
print('===' * 20)

# 3   ? 匹配前一个字符出现1次或者0次 {0,1}
print(re.search('a?go', 'go'))
print(re.search('a?go', 'ago'))
print(re.search('a?go', 'aago'))
print(re.search('a?go', 'aaago'))
print('===' * 20)

# 4   {m} 匹配前一个字符出现m次
print(re.search('a{2}go', 'ago'))
print(re.search('\w{3}go', '1a_go'))
print(re.search('\s{2}go', ' \ngo'))
print(re.search('\S{3}go', 'aa=!go'))
print('===' * 20)

# 5   {m,n} 匹配前一个字符出现从m到n次
print(re.search('a{1,3}go', 'ago'))
print(re.search('a{1,3}go', 'aago'))
print(re.search('a{1,3}go', 'aaago'))
print('===' * 20)

# 6   {m,} 匹配前一个字符至少出现m次
print(re.search('a{1,}go', 'ago'))
print(re.search('a{1,}go', 'aago'))
print(re.search('a{1,}go', 'aaago'))
print('===' * 20)
