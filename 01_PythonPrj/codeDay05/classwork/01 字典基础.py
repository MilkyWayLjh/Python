"""
字典是另一种可变容器模型，且可存储任意类型对象。
字典的每个键值 key=>value 对用冒号 : 分割，每个对之间用逗号(,)分割，整个字典包括在花括号 {} 中
结构：
{key1:value1, key2:value2, ...}
key:不可变数据类型，一般都用字符串。键必须是唯一的，但值则不必。键必须是不可变的，如字符串，数字，元组。
value: 任何数据类型都可以。值可以取任何数据类型。
Why:
[xx, xx, xx, xx, xx]
[xx, xx, xx, xx, xx]
[[18, 18, xx, xx, xx], [xx, xx, xx, xx], [xx, xx, xx, xx]]
[
 {'name':'good', 'age':18, 'addr':'成都', 'number':18},
 {'name':'good', 'age':18, 'addr':'成都', 'number':18},
 {'name':'good', 'age':18, 'addr':'成都', 'number':18}
]
特点：
key是唯一的
key：value形式的数据结构
"""

# 创建空字典
# 使用大括号 {} 来创建空字典
emptyDict = {}
# 打印字典
print(emptyDict)
# 查看字典的数量
print("Length:", len(emptyDict))
# 查看类型
print(type(emptyDict))


# 构造函数 dict() 可以直接从键值对序列中构建字典如下：
dict0 = dict()
print(dict0)

dict1 = dict([('Runoob', 1), ('Google', 2), ('Taobao', 3)])
print(dict1)
# 创建字典：字典推导式
dict2 = {x: x**2 for x in (2, 4, 6)}
print(dict2)

dict3 = dict(Runoob=1, Google=2, Taobao=3)
print(dict3)
print(str(dict3))
print(dict3.items())    # dict_items([('Runoob', 1), ('Google', 2), ('Taobao', 3)])
# print(dict3.items()[0])     # 返回的是视图对象，不支持索引操作，直接使用[0]会抛出TypeError
print(dict3.keys())     # dict_keys(['Runoob', 'Google', 'Taobao'])
print(dict3.values())   # dict_values([1, 2, 3])
print(len(dict3.values()))
for key, value in dict3.items():
    print(key, value)
for key in dict3.keys():
    print(key)
for value in dict3.values():
    print(value)

# 字典值可以是任何的 python 对象，既可以是标准的对象，也可以是用户定义的，但键不行。
# 两个重要的点需要记住：
# 1）不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住，如下实例：
tinydict = {'Name': 'Runoob', 'Age': 7, 'Name': '小菜鸟'}
print("tinydict['Name']: ", tinydict['Name'])         # tinydict['Name']:  小菜鸟

# 2）键必须不可变，所以可以用数字，字符串或元组充当，而用列表就不行，如下实例：
tinydict = {'Name': 'Runoob', 1: 7}
print(tinydict[1])  # 7
# tinydict = {['Name']: 'Runoob', 'Age': 7}
# print("tinydict['Name']: ", tinydict[['Name']])       # 报错，key为列表
