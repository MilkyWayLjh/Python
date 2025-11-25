# 列表推导式
"""
说明：快速生成列表的表达式
特点：生成列表语法简洁，效率高。
变量 = [生成元素的表达式 控制元素生成个数的表达式]
常用方式:
    变量 = [表达式 for 变量 in 列表]
"""
# 需求1：列表中生成1-10的元素
li1 = [i for i in range(1, 11)]
print(li1)

# 需求2：生成1-10奇数列表
li2 = [i for i in range(1, 11, 2)]
print(li2)
li2 = [i for i in range(1, 11) if i % 2 != 0]
print(li2)

# 需求3：['hello', 'hello', ...]
li3 = ['hello' for i in range(10)]
print(li3)

li4 = ['hello' + str(i) for i in range(10)]
print(li4)

li5 = [i ** 2 for i in range(10)]
print(li5)
print('==' * 20)

# 需求4：[(1, 1), (1, 2), (2, 1), (2, 2)]
# 传统
li6 = []
for i in range(1, 3):
    for j in range(1, 3):
        li6.append((i, j))
print(li6)
print('--' * 20)

# 列表推导式
li7 = [(i, j) for i in range(1, 3) for j in range(1, 3)]
print(li7)
print('--' * 20)
'''
字典推导式
'''
listdemo = ['Google', 'Runoob', 'Taobao']
# 将列表中各字符串值为键，各字符串的长度为值，组成键值对
newdict = {key: len(key) for key in listdemo}
print(newdict)

dic = {x: x**2 for x in (2, 4, 6)}
print(dic)
