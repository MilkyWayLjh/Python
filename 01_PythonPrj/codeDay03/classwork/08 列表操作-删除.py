# 列表删除
# del list[index]   删除指定索引的数据
list1 = [1, 2, 3, 2, 1, 3]
del list1[1]
print(list1)    # [1, 3, 2, 1, 3]
# del list1
# print(list1)  # NameError: name 'list1' is not defined

# list.pop()    删除末尾的数据, 并返回该数据
# list.pop(index)    删除指定索引的数据
list2 = list1.pop()
print(list1, list2)     # [1, 3, 2, 1] 3
list1.pop(-2)
print(list1)    # [1, 3, 1]

# list.remove(obj)    删除第一个出现的指定数据
list1.remove(1)
print(list1)    # [3, 1]

# list.clear()  清空列表
list1.clear()
print(list1)    # []
