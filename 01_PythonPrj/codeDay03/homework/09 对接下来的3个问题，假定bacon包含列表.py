"""
对接下来的3个问题，假定bacon包含列表[3.14, 'cat', 11, 'cat', True]
1) bacon.index('cat')求值为多少？
2) bacon.append(99)让bacon中的列表值变成什么样？
3) bacon.remove('cat')让bacon中的列表值变成什么样？
"""

bacon = [3.14, 'cat', 11, 'cat', True]

# 1) bacon.index('cat')求值为多少？
"""
list.index(元素)的用法为查询列表中第一次出现的元素的下标
在bacon列表中'cat'的下标分别为1,3   第一次出现的下标为1
所以bacon.index('cat')输出为1
"""
print(bacon.index('cat'))   # 结果为 1

# 2) bacon.append(99)让bacon中的列表值变成什么样？
"""
list.append(元素)的用法为,将元素添加到列表的末尾
所以bacon.append(99)输出的结果为[3.14, 'cat', 11, 'cat', True, 99]
"""
bacon.append(99)
print(bacon)    # 结果为[3.14, 'cat', 11, 'cat', True, 99]

# 3) bacon.remove('cat')让bacon中的列表值变成什么样？
"""
list.remove(元素)的用法为,将列表中第一次出现的元素移除
所以bacon.remove('cat')输出的结果为[3.14, 11, 'cat', True, 99]
"""
bacon.remove('cat')
print(bacon)    # 结果为[3.14, 11, 'cat', True, 99]
