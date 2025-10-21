# 删除字典元素
#   能删单一的元素也能清空字典，清空只需一项操作。
#   显式删除一个字典用del命令，如下实例：
# 1 del 命令方法
dict1 = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}

del dict1['Name']  # 删除键 'Name'
# dict1.clear()  # 清空字典
# del dict1  # 删除字典

print("dict1['Age']: ", dict1['Age'])
print("dict1['Class']: ", dict1['Class'])
print('==' * 20)


# 2 pop(key[,default])    删除字典 key（键）所对应的值，返回被删除的值。
# 参数:
#   key - 要删除的键
#   default - 当键 key 不存在时返回的值
# 返回值:
# 返回被删除的值：
#   如果 key 存在 - 删除字典中对应的元素
#   如果 key 不存在 - 返回设置指定的默认值 default
#   如果 key 不存在且默认值 default 没有指定 - 触发 KeyError 异常
site = {'name': '菜鸟教程', 'alexa': 10000, 'url': 'www.runoob.com'}
element = site.pop('name')
print('删除的元素为:', element)     # 删除的元素为: 菜鸟教程
print('字典为:', site)     # 字典为: {'alexa': 10000, 'url': 'www.runoob.com'}

# 如果删除的键不存在会触发异常：
# site = {'name': '菜鸟教程', 'alexa': 10000, 'url': 'www.runoob.com'}
# element = site.pop('nickname')
# print('删除的元素为:', element)
# print('字典为:', site)
# 报错：
# File "/Users/RUNOOB/runoob-test/test.py", line 5, in <module>
#     element = site.pop('nickname')
# KeyError: 'nickname'

# 可以设置默认值来避免异常：
site = {'name': '菜鸟教程', 'alexa': 10000, 'url': 'www.runoob.com'}
element = site.pop('nickname', '不存在的key')
print('删除的元素为:', element)       # 删除的元素为: 不存在的 key
print('字典为:', site)     # 字典为: {'name': '菜鸟教程', 'alexa': 10000, 'url': 'www.runoob.com'}
print('==' * 20)


# 3 popitem()   返回并删除字典中的最后一对键和值。如果字典已经为空，却调用了此方法，就报出 KeyError 异常。
# 返回值:
#   返回最后插入键值对(key, value 形式)，按照 LIFO（Last In First Out 后进先出法） 顺序规则，即最末尾的键值对。
# 注意：在 Python3.7 之前，popitem() 方法删除并返回任意插入字典的键值对。
site = {'name': '菜鸟教程', 'alexa': 10000, 'url': 'www.runoob.com'}
# ('url': 'www.runoob.com') 最后插入会被删除
result = site.popitem()
print('返回值 = ', result)     # 返回值 =  ('url', 'www.runoob.com')
print('site = ', site)      # site =  {'name': '菜鸟教程', 'alexa': 10000}
# 插入新元素
site['nickname'] = 'Runoob'
print('site = ', site)      # site =  {'name': '菜鸟教程', 'alexa': 10000, 'nickname': 'Runoob'}
# 现在 ('nickname', 'Runoob') 是最后插入的元素
result = site.popitem()
print('返回值 = ', result)     # 返回值 =  ('nickname', 'Runoob')
print('site = ', site)      # site =  {'name': '菜鸟教程', 'alexa': 10000}
print('==' * 20)


# 4 dict.clear() 用于删除字典内所有元素。 该函数没有任何返回值。
d1 = {'Name': 'Zara', 'Age': 7}
print("字典长度 : %d" % len(d1))        # 字典长度 : 2
d1.clear()
print("字典删除后长度 : %d" % len(d1))     # 字典删除后长度 : 0
print(d1)       # {}
