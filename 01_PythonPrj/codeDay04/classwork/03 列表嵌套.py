li1 = [
    ['python', 'mysql', 'linux', 'git', 'shell'],
    ['apple', 'peer', 'lemon']
]
# 需求：打印嵌套列表中的每个元素

# for循环
# for i in li1:
#     for j in i:
#         print(j)

# while循环
i = 0
while i < len(li1):
    j = 0
    # print(li1[i])
    while j < len(li1[i]):
        print(li1[i][j])
        j += 1
    i += 1


"""
假设有一个列表 names = [[“张飞”,”刘备”,”关羽”],[“曹操”,”典韦”,”司马懿”]],
如何将names这个列表通过代码转变得到如下列表 li=[“张飞”,”刘备”,”关羽”,“曹操”,”典韦”,”司马懿”]
"""
# 方法一：
# for循环
names = [['张飞', '刘备', '关羽'], ['曹操', '典韦', '司马懿']]
li = []
for item1 in names:
    for item2 in item1:
        # print(item2)
        li.append(item2)
print(li)
# while循环
names = [['张飞', '刘备', '关羽'], ['曹操', '典韦', '司马懿']]
li = []
i = 0
while i < len(names):
    j = 0
    while j < len(names[i]):
        li.append(names[i][j])
        j += 1
    i += 1
print(li)

# 方法二：
names = [['张飞', '刘备', '关羽'], ['曹操', '典韦', '司马懿']]
# li1, li2 = names[0], names[1]
li1, li2 = names    # 列表解包
# print(li1 + li2)
li1.extend(li2)
print(li1)
