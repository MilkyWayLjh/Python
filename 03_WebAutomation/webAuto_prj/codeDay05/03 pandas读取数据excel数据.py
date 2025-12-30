""""
 pandas:是专门用于数据管理的一个工具,它实际上集成一个固定的模块xlrd
 语法:
     1.文件读取对象 = pandas.read_excel("路径")-->读取excel文件,获取的是一个类对象
        内容中有索引号,每一行数据
     2.文件读取对象.head(n):
        获取指前n行的数据
     3.文件读取对象.loc[index].values
        获取某一行的数据
     4.文件读取对象.loc[n1,n2].values
        获取第n1,n2行的数据
     5.文件读取对象.values.tolist()
        将文件中所有的内容转为列表输出
     6.文件读取对象.loc[index].to_dict()
        将某一行的数据转为字典输出
        在结果for循环来遍历转为字典
     7.文件读取对象.shape #获取文件行数和列数
     8.文件读取对象.index.values #获取文件的索引范围
     9.文件读取对象.columns #获取列名
"""

import pandas

path1 = "./data/pandas_1.xls"
path2 = "./data/pandas_2.xlsx"

# 生成了一个读取结果对象
table = pandas.read_excel(path1)
print(table)
print(type(table))

# head获取指定行数的内容,默认时前2行
print(table.head(2))
# head获取指定行数的内容,默认时前5行
print(table.head())

# 获取指定的某一行,使用索引获取,索引是从0开始
print(table.loc[6].values)

# 指定获取某个两行的数据
print(table.loc[4:7].values)  # 获取某一个范围内的数据

print(table.loc[[i for i in range(2, 7)]].values)  # 列表推导式来获取某一个范围内的数据
# print(table.loc[[4,7]])

print(table.loc[[2, 3, 4, 5, 6]].values)
#
# #将文件内容转为列表
# print(table.values.tolist())
#
# #将文件中数据转为字典
#
# print(table.loc[1].to_dict())
#
for i in range(len(table.values.tolist())):
    print(table.loc[i].to_dict())
#

print(table.shape)  # 获取文件行数和列数
print(table.index.values)  # 获取文件的索引范围
print(table.index)
print(table.columns)  # 获取列名

