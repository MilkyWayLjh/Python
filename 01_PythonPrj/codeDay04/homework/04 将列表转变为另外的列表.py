"""
假设有一个列表 names = [[“张飞”,”刘备”,”关羽”],[“曹操”,”典韦”,”司马懿”]],
如何将names这个列表通过代码转变得到如下列表 li=[“张飞”,”刘备”,”关羽”,“曹操”,”典韦”,”司马懿”]
"""
# 方法一：
names = [['张飞', '刘备', '关羽'], ['曹操', '典韦', '司马懿']]
li = []
for item1 in names:
    for item2 in item1:
        # print(item2)
        li.append(item2)
print(li)

# 方法二：
names = [['张飞', '刘备', '关羽'], ['曹操', '典韦', '司马懿']]
li1, li2 = names[0], names[1]
# print(li1 + li2)
li1.extend(li2)
print(li1)
