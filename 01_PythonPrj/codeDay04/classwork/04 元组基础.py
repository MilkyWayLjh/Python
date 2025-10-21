# 元组结构 tuple
# 简单方式（常用）
t1 = ()
t2 = ('a', 1, 1.1, True, [1, 2], ('hello', 'good'))
print(type(t1))
print(type(t2))
t3 = ("hello")
t3_1 = ('hello',)
# 注意：只有一个元素的情况下，后面必须要有逗号，否则就是一个普通数据
print(t3, type(t3))     # <class 'str'>
print(t3_1, type(t3_1))   # <class 'tuple'>
print('==' * 20)

# 函数方式
t4 = tuple('hello')
print(t4)
t5 = tuple(['python', 'mysql', 'linux'])
print(t5)
l1 = list(t5)
print(l1)
print('--' * 20)

# 下标使用
print(t2[1])

# 切片使用
print(t2[:3])

# 元组特点
"""
1. 元组中可以放任何数据类型
2. 元组也是有序的，可以通过下标获取元素
3. 通过切片获取新的子元组，和列表相同
4. 元组不可以修改(和列表的区别)    除了不能够修改里面的元素外，其他的操作和列表一样。
"""

# t2 = ('a', 1, 1.1, True, [1, 2], ('hello', 'good'))
# t2[0] = 'good'   # 元组不能修改
# print(t2)
print('--' * 20)
t2[-2][0] = 100  # 但如果元组内包含可变对象（如列表），则可以通过索引修改该可变对象的内容
print(t2)

# 删除元组
# 元组中的元素值是不允许删除的，但我们可以使用del语句来删除整个元组
tup = ('Google', 'Runoob', 1997, 2000)

print(tup)
del tup
print("删除后的元组 tup : ")
# print(tup)         # 'tup' is not defined

# 关于元组是不可变的
# 所谓元组的不可变指的是元组所指向的内存中的内容不可变
tup = ('r', 'u', 'n', 'o', 'o', 'b')
# tup[0] = 'g'     # 不支持修改元素

# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: 'tuple' object does not support item assignment
id(tup)     # 查看内存地址    4440687904
tup = (1, 2, 3)
id(tup)     # 内存地址不一样了  4441088800
