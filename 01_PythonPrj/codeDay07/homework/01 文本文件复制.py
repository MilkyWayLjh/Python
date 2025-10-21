"""
需求：
    1.根据录入文件名,复制出来一个新的文件,新的文件名为: 原文件名-副本.原文件后缀
分析:
    1.一行一行读取原文件中的数据
    2.从原文件中读取出文件名和后缀。通过.来取出文件名中前面和后面的内容.
    3.一行一行写入目标文件(读取到文件内容时)
"""
import os

file = input('录入文件名: ')
filename, extension = os.path.splitext(file)
# print(filename, extension)
f = open(file, 'r', encoding='utf-8')
new_f = open(filename + '-副本' + extension, 'a', encoding='utf-8')
for line in f:
    # print(line)
    new_f.write(line)
f.close()
new_f.close()
