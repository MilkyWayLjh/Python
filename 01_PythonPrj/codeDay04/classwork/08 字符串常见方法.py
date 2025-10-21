# 字符串常用方法

# 1 去除俩边空格 strip()
str1 = ' hello '
print(str1)
# str.strip()  # 去除俩边空格
print(str1.strip())
# str.lstrip() # left去除左边空格
print(str1.lstrip())
# str.rstrip() # right去除右边空格
print(str1.rstrip())
print('==' * 20)

# 2 字符串分割 split()
# 字符串转列表
str2 = 'hello world'
# str.split() 按照空格分割字符串为列表
print(str2.split())     # ['hello', 'world']
print(''.join(str2.split()))    # helloworld
print(' '.join(str2.split()))    # hello world
# str.split(分割符) 按照分割符来分割字符串为列表
str3 = 'python,mysql,linux,git'
print(str3.split('n'))  # ['pytho', ',mysql,li', 'ux,git']
print(str3.split(','))
# str.split(分割符, 分割次数) 从左按照指定分隔符分割,分割指定的次数,返回一个列表
print(str3.split(',', 2))
# str.rsplit(分割符, 分割次数) 从右按照指定分隔符分割,分割指定的次数,返回一个列表
print(str3.rsplit(',', 2))
print('==' * 20)


# 3 字符串拼接 join()
# str.join(列表)    列表转字符串
list1 = ['python', 'mysql', 'linux']
print('|'.join(list1))
print(','.join(list1))
print(''.join(list1))
print(' '.join(list1))
print('+'.join(list1))
print('==' * 20)

# 4 字符串替换 replace()
# str.replace(原内容, 新内容)  # 返回替换之后的新字符串
str1 = 'hello world'
print(str1.replace('world', 'python'))
print('==' * 20)


# 5 str.index(char)
# str.index(str, beg=0, end=len(string)) 方法检测字符串中是否包含子字符串 str，
# 如果指定 beg（开始） 和 end（结束） 范围，则检查是否包含在指定范围内，如果str不在 string中会报一个异常。
str1 = "Runoob example....wow!!!"
str2 = "exam"
print(str1.index(str2))
print(str1.index(str2, 5))
# print(str1.index(str2, 10))      # 出现异常信息
print('==' * 20)


# 6 str.find(str, beg=0, end=len(string))
# 检测字符串中是否包含子字符串 str ，如果指定 beg（开始） 和 end（结束） 范围，则检查是否包含在指定范围内，
# 如果指定范围内如果包含指定索引值，返回的是索引值在字符串中的起始位置。如果不包含索引值，返回-1。
str1 = "Runoob example....wow!!!"
str2 = "exam"
print(str1.find(str2))      # 7
print(str1.find(str2, 5))       # 7
print(str1.find(str2, 10))      # -1
print('==' * 20)


# 7 变量格式化输出 str.format()
# f格式化, %格式化
name, age, address = 'hello', 11, '成都'
str2 = '姓名：{}, 年龄：{}, 地址：{}'.format(name, age, address)
str3 = '地址：{2}, 姓名：{0}, 年龄：{1}'.format(name, age, address)
str4 = '地址：{c}, 姓名：{a}, 年龄：{b}'.format(a='apple', b=18, c='南城')
print(str2)
print(str3)
print(str4)
print('==' * 20)


# 8 大小写转化  upper() lower()
str1 = 'hello python'
# 字符串转化为大写
str2 = str1.upper()
print(str2)
# 字符串转化为小写
print(str2.lower())
# 单词首字母大写  str.title()
print(str1.title())
# 判断字符串大小写 isupper() islower() istitle()
if str1.isupper():
    print('大写')
elif str1.islower():
    print('小写')
elif str1.istitle():
    print('首字母大写')
else:
    print('其他')
print('==' * 20)


# 9 判断字符串开头或者结尾 startswith()  endswith()
# 判断开始
str1 = 'hello python'
print(str1.startswith('he'))
print(str1.startswith('le'))
# 判断结尾
print(str1.endswith('on'))
print(str1.endswith('of'))
# 举例：判断文件是不是.txt的后缀文件
print(str1.endswith('.txt'))
print('==' * 20)


# 10 判断“数据类型”的方法 isdigit() isalpha() isalnum()     返回的是 True/False
str1 = '11'
str2 = 'aa'
str3 = 'aa11'
# 判断字符串由数字组成
print(str1.isdigit())
print(str2.isdigit())
print(str3.isdigit())
print('--' * 20)
# 判断字符串由字母组成
print(str1.isalpha())
print(str2.isalpha())
print(str3.isalpha())
print('--' * 20)
# 判断字符串由字母数字组成,包括一个就行.  至少有一个字符并且所有字符都是字母或数字
print(str1.isalnum())
print(str2.isalnum())
print(str3.isalnum())
print('--' * 20)
