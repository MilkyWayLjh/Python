import keyword
print(keyword.kwlist)

"""
Python3 的六个标准数据类型中：
    不可变数据（3 个）：Number（数字）、String（字符串）、Tuple（元组）；
    可变数据（3 个）：List（列表）、Dictionary（字典）、Set（集合）。
"""

# Python3 支持 int、float、complex（复数）、bool
a, b, c, d = 20, 5.5, 4 + 3j, True
print(type(a), type(b), type(c), type(d))
# <class 'int'> <class 'float'> <class 'complex'> <class 'bool'>

# 此外还可以用 isinstance 来判断：
e = 111
print(isinstance(e, int))  # True
"""
isinstance 和 type 的区别在于：
    type()不会认为子类是一种父类类型。
    isinstance()会认为子类是一种父类类型。
"""
# 注意：Python3 中，bool 是 int 的子类，True 和 False 可以和数字相加， True==1、False==0 会返回 True，但可以通过 is 来判断类型。
print(type(e + True) is int)
print('===' * 30)


# List（列表）
list = ['abcd', 786, 2.23, 'runoob', 70.2]
tinylist = [123, 'runoob']

print(list)  # 输出完整列表 => 打印结果为：['abcd', 786, 2.23, 'runoob', 70.2]
print(list[0])  # 输出列表第一个元素  => 打印结果为：abcd
print(list[1:3])  # 从第二个开始输出到第三个元素 => 打印结果为：[786, 2.23]
print(list[2:])  # 输出从第三个元素开始的所有元素    => 打印结果为：[2.23, 'runoob', 70.2]
print(tinylist * 2)  # 输出两次列表 => 打印结果为：[123, 'runoob', 123, 'runoob']
print(list + tinylist)  # 连接列表  => 打印结果为：['abcd', 786, 2.23, 'runoob', 70.2, 123, 'runoob']

# Python 列表截取可以接收第三个参数，参数作用是截取的步长，
# 以下实例在索引 1 到索引 4 的位置并设置为步长为 2（间隔一个位置）来截取字符串：
print(list[1:4:2])
print('===' * 30)


# Tuple（元组）
tuple = ('abcd', 786, 2.23, 'runoob', 70.2)
tinytuple = (123, 'runoob')
print(tuple)  # 输出完整元组
print(tuple[0])  # 输出元组的第一个元素
print(tuple[1:3])  # 输出从第二个元素开始到第三个元素
print(tuple[2:])  # 输出从第三个元素开始的所有元素
print(tinytuple * 2)  # 输出两次元组
print(tuple + tinytuple)  # 连接元组

tup = (1, 2, 3, 4, 5, 6)
print(tup[0])  # 1
# tup[0] = 11     # 修改元组元素的操作是非法的

# 构造包含 0 个或 1 个元素的元组比较特殊，所以有一些额外的语法规则：
tup1 = ()  # 空元组
tup2 = (20,)  # 一个元素，需要在元素后添加逗号
print(tup1, tup2)

# string、list 和 tuple 都属于 sequence（序列）。
# 注意：
#     1、与字符串一样，元组的元素不能修改。
#     2、元组也可以被索引和切片，方法一样。
#     3、注意构造包含 0 或 1 个元素的元组的特殊语法规则。
#     4、元组也可以使用+操作符进行拼接。
print('===' * 30)


# Dictionary（字典）
# 字典（dictionary）是Python中另一个非常有用的内置数据类型。
# 列表是有序的对象集合，字典是无序的对象集合。两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。
# 字典是一种映射类型，字典用 { } 标识，它是一个无序的 键(key) : 值(value) 的集合。
# 键(key)必须使用不可变类型。
# 在同一个字典中，键(key)必须是唯一的。
dict = {}
dict[1] = "1 - 菜鸟教程"
dict['two'] = "2 - 菜鸟工具"
tinydict = {'name': 'runoob', 'code': 1, 'site': 'www.runoob.com'}

print(dict)       # 输出完整的字典
print(dict[1])       # 输出键为 1 的值
print(dict['two'])           # 输出键为 'two' 的值
print(tinydict)          # 输出完整的字典
print(tinydict.keys())   # 输出所有键
print(tinydict.values())    # 输出所有值

# 构造函数 dict() 可以直接从键值对序列中构建字典如下：
# dict1 = dict([('Runoob', 1), ('Google', 2), ('Taobao', 3)])
# print(dict1)
# dict2 = {x: x**2 for x in (2, 4, 6)}
# print(dict2)
# dict3 = dict(Runoob=1, Google=2, Taobao=3)
# print(dict3)

# {x: x**2 for x in (2, 4, 6)} 该代码使用的是字典推导式.
# 另外，字典类型也有一些内置的函数，例如 clear()、keys()、values() 等。
# 注意：
# 1、字典是一种映射类型，它的元素是键值对。是无序的对象集合,通过键值对来存取.
# 2、字典的关键字必须为不可变类型，且不能重复。
# 3、创建空字典使用 { }。
print('===' * 30)


# Set（集合）
# 集合（set）是由一个或数个形态各异的大小整体组成的，构成集合的事物或对象称作元素或是成员。
# 基本功能是进行成员关系测试和删除重复元素。
# 可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。
# 创建格式：
#     set = {value01,value02,...}
#     或者
#     set(value)
sites = {'Google', 'Taobao', 'Runoob', 'Facebook', 'Zhihu', 'Baidu'}
print(sites)   # 输出集合，重复的元素被自动去掉

# 成员测试
if 'Runoob' in sites:
    print('Runoob 在集合中')
else:
    print('Runoob 不在集合中')

# set可以进行集合运算
a = set('abracadabra')
b = set('alacazam')
print(a)
print(a - b)     # a 和 b 的差集
print(a | b)     # a 和 b 的并集
print(a & b)     # a 和 b 的交集
print(a ^ b)     # a 和 b 中不同时存在的元素
# 元组不能 + 拼接
print('===' * 30)
