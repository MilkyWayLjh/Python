# 列表增加
# list.insert(index, obj) 将对象插入列表
list1 = [1, 2, 3]
list1.insert(0, 'hello')
print(list1)    # ['hello', 1, 2, 3]
list1.insert(-1, 'world')
print(list1)    # ['hello', 1, 2, 'world', 3]

# list.append(obj)    在列表末尾添加新的对象
list1.append('你好')
print(list1)    # ['hello', 1, 2, 'world', 3, '你好']

# list.extend(seq)    在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
list1.extend(['god', 'me'])
print(list1)    # ['hello', 1, 2, 'world', 3, '你好', 'god', 'me']
list1.extend('god')
print(list1)    # ['hello', 1, 2, 'world', 3, '你好', 'god', 'me', 'g', 'o', 'd']

# list.copy 列表的浅复制
list2 = list1.copy()
print(list2)    # ['hello', 1, 2, 'world', 3, '你好', 'god', 'me', 'g', 'o', 'd']
