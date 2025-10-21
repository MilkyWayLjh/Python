"""
1.可以是任意文件类型。2.大文件复制。
大文件的问题:
    read函数: 一次性的读取文件中的所有数据到内存中, 如果超出了内存容量会产生什么问题呢?  电脑就会卡死了,因为内存全部被占用了.
解决方案:
    1.所有文件都是二进制组成的,包含文本文件.   我们读取文件中的二进制
    2.一次读取1k的内容,然后写入文件, 读取多次.
注意事项:
    1.所有文件都是二进制文件(包含文本文件)
    2.二进制文件不需要指定编码,  只有文本文件需要指定编码
    3.二进制文件没有行的概念,所有不能够按行读取,所以在read中指定按指定的字节读取.
"""
import os

file = input('录入文件名: ')
# filename = (file.split('/'))[-1:-2:-1]
# print(filename[0])
# filename = (file.split('/'))[-1]
# print(filename)
print(os.path.split(file))
filename = os.path.split(file)[-1]
print(filename)

f = open(file, 'rb')
new_f = open('resource/' + filename[0], 'ab')
while True:
    content = f.read(1024)
    # print(content)
    new_f.write(content)
    if not content:
        break
f.close()
new_f.close()
