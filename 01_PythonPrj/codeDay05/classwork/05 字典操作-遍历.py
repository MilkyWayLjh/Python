"""
for 临时变量 in 可迭代对象:
    临时变量
说明：
    字典如果没有指明操作的是key还是value，默认使用的是key
"""

info = {'name': 'fine', 'age': 18}
# 1 key
# 第一种
for key in info.keys():
    print(key)
print('--' * 20)
# 第二种
for key in info:
    print(key)  # 字典如果没有指明操作的是key还是value，默认使用的是key
print('==' * 20)

# 2 value
for value in info.values():
    print(value)
print('==' * 20)

# 3 items
for item in info.items():
    print(item)
print('==' * 20)

# 4 key, value
# 拆包
for key, value in info.items():
    print(key, value)

print('==' * 20)

# TODO 拓展，3种方式将2个列表组成字典
li1 = ['a', 'b', 'c']   # 作为key
li2 = [1, 2, 3]   # 作为values
# 1 使用zip函数，遍历
dic1 = {}
# for i in range(len(li1)):
#     dic1[li1[i]] = li2[i]
for key, value in zip(li1, li2):
    dic1[key] = value
print(dic1)
# 2 使用zip函数，字典推导式
dic2 = {key: value for key, value in zip(li1, li2)}
print(dic2)
# 3 使用zip函数, dict()构造函数
dic3 = dict(zip(li1, li2))
print(dic3)


# TODO 拓展
'''
zip()的含义和用法:
1. 基本概念
zip() 是Python内置函数，用于将多个可迭代对象（如列表、元组等）"压缩"在一起，创建一个迭代器，该迭代器将每个可迭代对象中的元素按位置配对。
'''
# 2. 基本语法: zip(iterable1, iterable2, ...)
# 3. 基本用法示例,最简单的配对
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
result = zip(list1, list2)
print(list(result))  # [(1, 'a'), (2, 'b'), (3, 'c')]
# 创建字典
keys = ['name', 'age', 'city']
values = ['Alice', 25, 'Beijing']
dic = dict(zip(keys, values))
print(dic)  # {'name': 'Alice', 'age': 25, 'city': 'Beijing'}

# 4. 重要特性
# 处理不同长度的序列
list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c']
result = zip(list1, list2)
print(list(result))  # [(1, 'a'), (2, 'b'), (3, 'c')]  zip会以最短的序列为准
# 解压缩操作
pairs = [(1, 'a'), (2, 'b'), (3, 'c')]
numbers, letters = zip(*pairs)
print(numbers)  # (1, 2, 3)
print(letters)  # ('a', 'b', 'c')

# 5. 常见应用场景
# 矩阵转置
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transposed = list(zip(*matrix))
print(transposed)  # [(1, 4, 7), (2, 5, 8), (3, 6, 9)]

# 并行遍历
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
cities = ['Beijing', 'Shanghai', 'Guangzhou']

for name, age, city in zip(names, ages, cities):
    print(f"{name}, {age}, {city}")

# 6. Python 2 vs Python 3 的区别
# 在Python 2中，zip()函数返回的是一个元组列表，如[(1, 'a'), (2, 'b'), (3, 'c')]。
zip([1, 2], ['a', 'b'])  # [(1, 'a'), (2, 'b')]
# 在Python 3中，zip()函数返回的是一个迭代器，如<zip object at 0x7f9d9d9d9d9d>。
zip([1, 2], ['a', 'b'])  # <zip object at 0x7f9d9d9d9d9d>
list(zip([1, 2], ['a', 'b']))  # [(1, 'a'), (2, 'b')]

# 7. 实际应用示例
li1 = ['name', 'age', 'city']
li2 = ['Tom', 23, 'Shanghai']
dic3 = dict(zip(li1, li2))
print(dic3)  # {'name': 'Tom', 'age': 23, 'city': 'Shanghai'}
"""
这个过程相当于：
    zip(li1, li2) 生成配对: [('name', 'Tom'), ('age', 23), ('city', 'Shanghai')]
    dict() 将这些键值对转换为字典
zip() 是一个非常实用的函数，特别适合需要同时处理多个序列的场景。
"""
