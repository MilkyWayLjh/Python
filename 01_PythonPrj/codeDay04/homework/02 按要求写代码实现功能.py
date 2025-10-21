"""
写代码，有如下列表，请按要求实现每个功能 li = ['ethan', 'zoran', 'jim']
   a. 计算列表长度并输出
   b. 列表中追加元素 “lucy”，并输出添加后的列表
   c. 请在列表的第 1 个位置插入元素 “Tony”，并输出添加后的列表
   d. 请修改列表第 2 个位置的元素为 “Kelly”，并输出修改后的列表
   e. 请删除列表中的元素 “ethan”，并输出修改后的列表
   f. 请删除列表中的第 2 个元素，并输出删除的元素的值和删除元素后的列表
"""

li = ['ethan', 'zoran', 'jim']
# a
print(len(li))      # 3

# b
li.append('lucy')
print(li)       # ['ethan', 'zoran', 'jim', 'lucy']

# c
li.insert(0, 'Tony')
print(li)       # ['Tony', 'ethan', 'zoran', 'jim', 'lucy']

# d
li[1] = 'Kelly'
print(li)       # ['Tony', 'Kelly', 'zoran', 'jim', 'lucy']

# e
li = ['ethan', 'zoran', 'jim']
li.remove('ethan')
print(li)       # ['zoran', 'jim']

# f
li = ['ethan', 'zoran', 'jim']
li1 = li.pop(1)
print(li1, li)      # zoran ['ethan', 'jim']




