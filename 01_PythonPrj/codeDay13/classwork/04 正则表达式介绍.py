"""
正则表达式介绍
● 概念：正则就是记录字符串规则的一种字符串
● 作用：字符串匹配
● 特点：
  ○ 可读性比较差
  ○ 通用性强，几乎所有编程语言都支持使用


re模块
    在Python中需要通过正则表达式对字符串进行匹配的时候，可以使用一个 re 模块
● 方法
方法	                                描述	                        返回值
search(pattern,string[, flags])	    在字符串中查找正则匹配的字符串	第一个匹配到的对象或者None
findall(pattern, string[, flags])	列出字符串中模式的所有匹配项	    所有匹配到的字符串列表
match(pattern, string[, flags])     在字符串string的起始位置开始尝试匹配pattern，如果匹配成功返回一个匹配成功后的Match对象；否则返回None
re.sub(pattern, repl, string, count=0, flags=0)     用于替换字符串中的匹配项

匹配到的正则对象: re_obj
    re_obj.group(): 获取匹配到的字符串内容
    re_obj.groups(): 用括号把所有匹配出来的分组加入元组中，没有括号就为空()
group和groups是两个不同的函数。
    一般，re_obj.group(N) 返回第N组括号匹配的字符。
    而re_obj.group() == re_obj.group(0) == 所有匹配的字符，与括号无关，这个是API规定的。

    re_obj.groups() 返回所有括号匹配的字符，以tuple格式。
    re_obj.groups() == (re_obj.group(0), re_obj.group(1), ...)

    ● group() 同 group（0）就是匹配正则表达式整体结果
    ● group(1) 列出第一个括号匹配部分，group(2) 列出第二个括号匹配部分，group(3) 列出第三个括号匹配部分。
    ● groups() 是把所有匹配出来的分组加入元组中

● 匹配模式
匹配模式	            描述
re.I (Ignore)	    使匹配对大小写不敏感，也就是不区分大小写的模式
re.S (Space)	    使 . 这个通配符能够匹配包括换行在内的所有字符，针对多行匹配
"""
import re

# 原字符
match_obj = re.search('hello', '你好hello world hello python')
# 匹配对象.group()  #提取匹配到的字符串
print(match_obj)
print(match_obj.group())
print('==' * 20)

# re.findall(pattern, string[, flag])
# 列出字符串中模式的所有匹配项, 所有匹配到的字符串列表
match_list = re.findall('hello', '你好hello world hello python, hello')
print(match_list)

print('===' * 20)

print(re.search('it\w\w\w', 'Itdogxxxitcat', re.I).group())
list1 = re.findall('it\w\w\w', 'Itdogxxxitcatitabcxxfjdjlkit123', re.I)
print(list1)

print(re.search('it....', 'Itdogxxxitcat\n', re.S).group())

print('===' * 20)

# re.sub(pattern, repl, string, count=0, flags=0)
s = 'day1'
print(re.sub('^day[1-9]$', 'day01', s))  # day01
print(s)    # day1
s = re.sub('^day[1-9]$', 'day01', s)
print(s)    # day1
