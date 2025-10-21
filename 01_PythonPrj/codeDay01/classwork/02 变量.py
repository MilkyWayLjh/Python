# 变量：
#   python运行时在电脑上开辟一个 内存空间，该内存空间用来存储数据的内存地址。
#   变量就是给该存储的数据起一个名字或贴一个标签，需要使用该数据时就将变量拿去使用。便于数据的使用和修改。
# 语法: 变量名 = 变量值
name = 'i_kun'
print(name * 6)
print('===' * 6)

# 标识符：
# 1. 以字母 数字 下划线组成，不能以数字开头
# 2. 区分大小写
# 3. 不能使用python关键字

# 命名格式
# 下划线
hello_world = 123
# 驼峰式
#   大驼峰式
HelloWorld = 111
#   小驼峰式
helloWorld = 111

# python的关键字
import keyword
print(keyword.kwlist)

# 修改变量
name = 'zhang_san'
print(name)
# 删除变量
del name
# print(name)


# 变量赋值
a, b, c = 1, 2, 3
print(a, b, c)

d = e = f = 5
print(f, e, d)

# 交换变量值
m = 10
n = 100

m, n = n, m
print(m, n)

# p = m
# m = n
# n = p
# print(m, n)
