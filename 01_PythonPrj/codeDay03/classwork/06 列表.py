# 如何定义列表

# 第一种（常用）
list1 = []  # 空列表
list2 = [1, 12.1, 'hello', True, None, (1, 2), {'key': 'value'}, {1, 2}]
# 说明：
# 列表里面的内容叫做元素
# 列表中的元素可以写任何数据类型
# 列表有序的容器
# 列表中的元素可以重复
# 好处：
# 同时存放多个数据

print(list1)
print(list2)
print('==' * 20)

# 第二种
list3 = list()  # 空列表
list4 = list('hello')
print(list3)
print(list4)

# 索引（下标）
# 列表中数据的序号
# 从左至右：从0开始排序
# 从右至左：从-1开始排序
list5 = ['python', 'mysql', 'git', 'shell', 'linux']
print(list5[0])
print(list5[-1])
print(list5[1:3])
print(list5[-3:-1])
print(list5[::-1])
