# Python 访问子字符串，可以使用方括号 [] 来截取字符串，字符串的截取的语法格式如下：
#   变量[头下标:尾下标], 索引值以 0 为开始值，-1 为从末尾的开始位置。
# [ : ]	截取字符串中的一部分，遵循 左闭右开 原则，str[0:2] 是不包含第 3 个字符的。

# Python 字符串更新
# 你可以截取字符串的一部分并与其他字段拼接，如下实例：
var1 = 'Hello World!'
print("已更新字符串 : ", var1[:6] + 'Runoob!')    # 已更新字符串 :  Hello Runoob!

# Python转义字符
# 在需要在字符中使用特殊字符时，python 用反斜杠 \ 转义字符。

# \(在行尾时)	续行符
print("line1 \
    ... line2 \
    ... line3")     # line1 line2 line3

# \\	反斜杠符号
print("\\")     # \

# \'	单引号
print('\'')     # '

# \"	双引号
print("\"")     # "

# \a	响铃
print("\a")     # 执行后电脑有响声。

# \b	退格(Backspace)
print("Hello \b World!")       # Hello World!

# \000	空
print("\000")

# \n	换行
print("\n")

# \v	纵向制表符
print("Hello \v World!")    # Hello
#                                 World!

# \t	横向制表符
print("Hello \t World!")    # Hello      World!

# \r	回车，将 \r 后面的内容移到字符串开头，并逐一替换开头部分的字符，直至将 \r 后面的内容完全替换完成。
print("Hello\rWorld!")      # World!
print('google runoob taobao\r123456')   # 123456 runoob taobao

# \f	换页
print("Hello \f World!")
# Hello
#      World!

# \yyy	八进制数，y 代表 0~7 的字符，例如：\012 代表换行。
print("\110\145\154\154\157\40\127\157\162\154\144\41")     # Hello World!
# \xyy	十六进制数，以 \x 开头，y 代表的字符，例如：\x0a 代表换行
print("\x48\x65\x6c\x6c\x6f\x20\x57\x6f\x72\x6c\x64\x21")     # Hello World!

# Python字符串运算符    变量 a 值为字符串 "Hello"，b 变量值为 "Python"：
# +	字符串连接	a + b 输出结果： HelloPython
# *	重复输出字符串	a*2 输出结果：HelloHello
# []	通过索引获取字符串中字符	a[1] 输出结果 e
# [ : ]	截取字符串中的一部分，遵循 左闭右开 原则，str[0:2] 是不包含第 3 个字符的。	a[1:4] 输出结果 ell
# in	成员运算符 - 如果字符串中包含给定的字符返回 True	'H' in a 输出结果 True
# not in	成员运算符 - 如果字符串中不包含给定的字符返回 True	'M' not in a 输出结果 True


# Python 的字符串内建函数、方法
# 查看菜鸟的 字符串 一栏中，很多方法。
