"""
遍历：
依次获取列表（可迭代对象）中的数据
可以遍历：字符串，列表，元组，字典
"""
list1 = ['python', 'mysql', 'linux', 'git']

# while循环遍历
i = 0
while i < len(list1):
    print(list1[i])
    i += 1
print('==' * 20)

# for循环遍历
"""
语法：
for 临时变量 in 可迭代对象（列表）:
    print(临时变量)
"""
for item in list1:
    print(item)

# 俩种遍历方式的特点：
"""
while可以控制想要遍历的元素
for循环一次性遍历对象中的所有元素
"""
print('--' * 20)
# 遍历字符串
str1 = 'hello'
for char in str1:
    print(char)
