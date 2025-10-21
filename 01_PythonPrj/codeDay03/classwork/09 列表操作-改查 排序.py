# 修改
# list[index] = obj
list1 = [1, 2, 3, 1, 2, 3, 1, 2, 3]
list1[1] = 4
print(list1)    # [1, 4, 3, 1, 2, 3, 1, 2, 3]


# 查询
# 变量 = list[index]
l1 = list1
l2 = list1[2]
print(l1, l2)   # [1, 4, 3, 1, 2, 3, 1, 2, 3] 3

# list.index(obj)   查询第一次数据出现的索引
print(list1.index(3))   # 2

# list.count(obj)   统计某个元素在列表中出现的次数
print(list1.count(1))   # 3

# len(list)     列表元素个数/长度
print(len(list1))   # 9
print(len('hello'))  # 5


# 排序
# list.sort()     列表升序
list1.sort()
print(list1)    # [1, 1, 1, 2, 2, 3, 3, 3, 4]

# list.sort(reverse=True)   列表降序
list1.sort(reverse=True)
print(list1)    # [4, 3, 3, 3, 2, 2, 1, 1, 1]

# list.reverse()    列表逆序 反转
list1.reverse()
print(list1)    # [1, 1, 1, 2, 2, 3, 3, 3, 4]
