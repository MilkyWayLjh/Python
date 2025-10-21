# 内置函数
# 1 len(data) 获取容器内容长度
# str， list， tuple， set， dict
print(len('abc'))
print(len([1, 2]))
print(len((1, 2)))
print(len({1, 2}))
print(len({'a': 1, 'b': 2}))
print('==' * 20)

# 2 del 变量 对于元素可以删除可变类型的元素

# 3 max()
# ASCII对比
print(max([1, 2, 3]))

# 4 min()
print(min([1, 2, 3]))

print('==' * 20)


# 运算符
# 1    + str list tuple
#   str
str1 = 'hello'
str2 = 'world'
print(str1 + str2)

#   list
print([1, 2] + ['a', 'b'])

#   tuple
print((1, 2) + ('a', 'b'))
print('==' * 20)

# 2 *   str list tuple
# 注意：只能和正整数相乘
print('abc' * 2)
print([1, 2] * 2)
print((1, 2) * 2)
print('==' * 20)

# 3     in语句
# 元素是否存在，在True， 不在False
# 数据：str list tuple dict
# 语法：item in 容器数据
str1 = 'hello'
print('he' in str1)     # True

list1 = ['python', 'msyql']
print('python' in list1)    # True

tuple1 = ('python', 'msyql')
dict1 = {'name': 'hello', 'age': 18}
print('hello' in dict1)   # False
print('hello' in dict1.values())     # True
print('name' in dict1)  # True
print('name' in dict1.keys())   # True

# 4     not in 语句 不在True， 在False
print('hello' not in dict1.values())     # False


# 5     is 语句
# 判断两个变量是否指向同一个对象，比较内存地址
a = [1, 2]
b = [1, 2]
print(id(a), id(b))     # 2776673922560 2776673680448
print(a is b)  # False
