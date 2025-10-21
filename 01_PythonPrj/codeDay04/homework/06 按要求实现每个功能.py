"""
写代码，有如下变量，请按照要求实现每个功能
   name = "  posekakaka  "
a. 移除name 变量对应的值两边的空格，并输出移除后的内容
   name = "posekakaka"
b. 判断name 变量对应的值是否以 "po" 开头，并输出结果
c. 判断name 变量对应的值是否以 "a" 结尾，并输出结果
d. 将name 变量对应的值中的 “k” 替换为 “c”，并输出结果
e. 将name 变量对应的值根据 “k” 分割，并输出结果。
f. 请问，上一题 e 分割之后得到值是什么类型（可选）
"""
name = ' posekakaka '
# a
n1 = name.strip()
print(n1)   # posekakaka

# b
n2 = n1.startswith('po')
print(n2)   # True

# c
n3 = n1.endswith('a')
print(n3)   # True

# d
n4 = n1.replace('k', 'c')
print(n4)   # posecacaca

# e
name = 'posekakaka'
print(name.split('k'))  # ['pose', 'a', 'a', 'a']

# f
# 上一题分割后得到一个列表['pose', 'a', 'a', 'a']，所以是列表类型
print(type(name.split('k')))    # <class 'list'>
