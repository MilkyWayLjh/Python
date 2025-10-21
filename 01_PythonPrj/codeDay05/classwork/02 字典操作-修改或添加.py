# 向字典添加新内容的方法是增加新的键/值对，修改或删除已有键/值
# 普通修改
# {key: value}
# 通过key可以获取key对应的value
info = {'name': 'fine', 'age': 18}
# 语法（获取）：dict[key] 得到这个key对应的value
"""
print(info['name'])
print(info['age'])
"""
# 1 语法（修改）： dict[key]=new value
# key存在：就是修改
info['name'] = 'hello'
info['age'] = 28
print(info)

# key不存在，新增
info['addr'] = '成都'
print(info)
print('==' * 20)

# 2 dict.setdefault(key, default_value)
# key存在不设置新值，不存在才设置，并返回。如果键不存在于字典中，将会添加键并将值设为default
info = {'name': 'fine', 'age': 18}
print(info.setdefault('name', 'good'))      # fine
print(info.setdefault('addr', '源码'))
print(info)
print('==' * 20)

# 3 dict.update(dict2)
# 将字典2合并到字典1，如果key相同，后面的会覆盖前面的。(把字典dict2的键/值对更新到dict里)
info1 = {'name': 'fine', 'age': 18}
info2 = {'name': 'good', 'age': 19, 'addr': '成都'}
info1.update(info2)
print(info1)
print('==' * 20)

# 4 dict.fromkeys(seq [, value])
# 用于创建一个新字典，以序列 seq 中元素做字典的键，value 为字典所有键对应的初始值。
# 参数:
#   seq -- 字典键值列表。
#   value -- 可选参数, 设置键序列（seq）对应的值，默认为 None。
# 返回值:
#   该方法返回一个新字典。
seq = ('name', 'age', 'sex')
dict1 = dict.fromkeys(seq)
print("新的字典为 : %s" % str(dict1))    # 新的字典为 : {'age': None, 'name': None, 'sex': None}
dict1 = dict.fromkeys(seq, 10)
print("新的字典为 : %s" % str(dict1))    # 新的字典为 : {'age': 10, 'name': 10, 'sex': 10}
value = (1, 2, 3)
dict1 = dict.fromkeys(seq, value)
print("新的字典为 : %s" % str(dict1))    # {'name': (1, 2, 3), 'age': (1, 2, 3), 'sex': (1, 2, 3)}
print('==' * 20)

# 5 dict.copy()     返回一个字典的浅复制
dict1 = {'Name': 'Runoob', 'Age': 7, 'Class': [1]}
dict2 = dict1.copy()
print("新复制的字典为 : ", dict2)      # 新复制的字典为 :  {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
dict1['Class'][0] = 2
print(dict1, dict2)

# 直接赋值和 copy 的区别：
dict1 = {'user': 'runoob', 'num': [1, 2, 3]}
dict2 = dict1  # 浅拷贝: 引用对象
dict3 = dict1.copy()  # 浅拷贝：深拷贝父对象（一级目录），子对象（二级目录）不拷贝，子对象是引用
#   修改 data 数据
dict1['user'] = 'root'
dict1['num'].remove(1)
#   输出结果
print(dict1)    # {'user': 'root', 'num': [2, 3]}
print(dict2)    # {'user': 'root', 'num': [2, 3]}
print(dict3)    # {'user': 'runoob', 'num': [2, 3]}

# 实例中 dict2 其实是 dict1 的引用（别名），所以输出结果都是一致的，
# dict3 父对象进行了深拷贝，不会随dict1 修改而修改，子对象是浅拷贝所以随 dict1 的修改而修改。
