# 1 dict[key]
# 根据key查询对应的值，key不存在则抛出错误
info = {'name': 'fine', 'age': 18}
# 存在
print(info['name'])
# 不存在 则会报错
# print(info['addr'])
print('==' * 20)


# 2 dict.get(key[, default])        函数返回指定键的值。
# 根据key查询对应值，key不存在，返回default的值，default默认是None
# 返回值：
#   返回指定键的值，如果键不在字典中返回默认值 None 或者设置的默认值。
info = {'name': 'fine', 'age': 18}
# 存在
print(info.get('name'))
# 不存在
print(info.get('addr'))
print(info.get('addr', '成都'))
print('==' * 20)


# 3 str(dict)   # 输出字典，可以打印的字符串表示。
d = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
print(str(d))  # "{'Name': 'Runoob', 'Class': 'First', 'Age': 7}"
print('==' * 20)


# 4 len(dict) 计算字典元素个数，即键的总数。
# 通用方法：str，list，tuple，dict
print(len(info))
print('==' * 20)


# 5 dict.items()    以列表返回视图对象，是一个可遍历的key/value 对。
# dict.keys()、dict.values() 和 dict.items()
#   返回的都是视图对象（ view objects），提供了字典实体的动态视图，这就意味着字典改变，视图也会跟着变化。
#   视图对象不是列表，不支持索引，可以使用 list() 来转换为列表。
#   我们不能对视图对象进行任何的修改，因为字典的视图对象都是只读的。
d1 = {'Name': 'Runoob', 'Age': 7}
print("Value : %s" % d1.items())    # Value : dict_items([('Age', 7), ('Name', 'Runoob')])
print('==' * 20)


# 6 dict.keys()     返回一个视图对象。(键)
# 7 dict.values()       返回一个视图对象。(值)
dishes = {'eggs': 2, 'sausage': 1, 'bacon': 1, 'spam': 500}
keys = dishes.keys()
values = dishes.values()
print(keys, values)

# 迭代
n = 0
for val in values:
    n += val
print(n)    # 504

# keys 和 values 以相同顺序（插入顺序）进行迭代
print(list(keys))     # 使用 list() 转换为列表
# ['eggs', 'sausage', 'bacon', 'spam']
print(list(values))
# [2, 1, 1, 500]

# 视图对象是动态的，受字典变化的影响，以下删除了字典的 key，视图对象转为列表后也跟着变化
del dishes['eggs']
del dishes['sausage']
print(list(keys))     # ['bacon', 'spam']
print(list(values))     # [1, 500]
# 相同两个 dict.values() 比较返回都是 False
d = {'a': 1}
print(d.values() == d.values())     # False
print('==' * 20)

# 8 key in dict
# Python 字典 in 操作符用于判断键是否存在于字典中，如果键在字典 dict 里返回 true，否则返回 false。
# 而 not in 操作符刚好相反，如果键在字典 dict 里返回 false，否则返回 true。

thisdict = {'Name': 'Runoob', 'Age': 7}
# 检测键 Age 是否存在
if 'Age' in thisdict:
    print("键 Age 存在")
else:
    print("键 Age 不存在")
# 检测键 Sex 是否存在
if 'Sex' in thisdict:
    print("键 Sex 存在")
else:
    print("键 Sex 不存在")

# not in
# 检测键 Age 是否存在
if 'Age' not in thisdict:
    print("键 Age 不存在")
else:
    print("键 Age 存在")

# ==>
#   键 Age 存在
#   键 Sex 不存在
#   键 Age 存在
