"""
f.read([n])
    1. 不写参数，一次性读取所有内容
    2. 写参数
        2.1 如果是普通模式，n就是字符个数
        2.2 如果是二进制模式,n就是字节个数
f.readline()
    读取一行
f.readlines()
    一次性读取所有行，返回列表类型
"""
# f.read([n])
# 打开文件-普通模式
"""
f = open('resource/test05.txt', 'r', encoding='utf8')
print(f.read(3))
print(f.read(3).encode())   # str转二进制
f.close()
"""
# 打开文件-二进制模式
"""
f = open('resource/demo1.txt', 'br')
content = f.read(7)
# 二进制类型转化为str
print(content)
# print(content.decode())
f.close()
"""

# f.readline() 按行读取内容
"""
f = open('resource/demo1.txt', 'r', encoding='utf8')
# print(f.readline())
# print(f.readline())
# print(f.readline())
f.close()
"""

# f.readlines() 一次性读取所有行，返回列表。列表中每个元素就是一行
"""
f = open('resource/test05.txt', 'r', encoding='utf8')
content_list = f.readlines()
print(content_list)
f.close()
"""

# 迭代遍历
f = open('resource/test03.txt', 'r', encoding='utf8')
print(f)
for line in f:
    print(line, end='')
f.close()

print('\n--------------')

# 或者 readlines()
f = open('resource/test03.txt', 'r', encoding='utf8')
content1 = f.readlines()
print(content1)
for line in content1:
    print(line, end='')
f.close()

print('\n--------------')

# 死循环 readline()
f = open('resource/test03.txt', 'r', encoding='utf8')
while True:
    content = f.readline()
    # 如果读到的是空字符串，那么就退出循环
    if not content:
        break
    print(content, end='')
f.close()
