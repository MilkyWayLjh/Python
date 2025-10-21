import copy

# 以下代码没有拷贝，只是拷贝了列表的地址
"""
list1 = [1, 2, 3]
list2 = list1
"""
# 注意：拷贝针对的是可变数据类型
# 浅拷贝
# 只拷贝最外层对象
# 语法：copy.copy(要拷贝的数据)  # 返回拷贝的结果
# 可变数据类型
list1 = [1, 2, 3, ['a', 'b']]
list2 = copy.copy(list1)
print(f'list1:{id(list1)}, list1[3]:{id(list1[3])}')
print(f'list2:{id(list2)}, list2[3]:{id(list2[3])}')
print('--' * 20)

# 不可变数据类型
str1 = 'hello'
str2 = copy.copy(str1)
print(f'str1:{id(str1)}')
print(f'str2:{id(str2)}')
print('==' * 20)

# 深拷贝
# 拷贝对象的所有层级
# 语法：copy.deepcopy(要拷贝的数据)  返回拷贝结果
# 可变数据类型
list1 = [1, 2, 3, ['a', 'b']]
list2 = copy.deepcopy(list1)
print(f'list1:{id(list1)}, list1[3]:{id(list1[3])}')
print(f'list2:{id(list2)}, list2[3]:{id(list2[3])}')
print('--' * 20)

# 不可变数据类型
str1 = 'hello'
str2 = copy.deepcopy(str1)
print(f'str1:{id(str1)}')
print(f'str2:{id(str2)}')
