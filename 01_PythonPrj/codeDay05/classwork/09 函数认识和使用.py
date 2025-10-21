"""
系统函数
print()   输出内容
len()     获取容器长度
min()     获取容器中最小值
max()     获取容器中最大值

函数
带名字的代码块，封装了一个特定的功能。

自定义函数
自己编写的函数
"""
# 变量
a = "AAAAAAAAAAAAAAAAAAAAAAAAA"

# for j in range(3):
#     for i in range(3):
#         print(a)

for i in range(300):
    print(a)
print(111111)

for i in range(300):
    print(a)
print(22222)

for i in range(300):
    print(a)
print(33333)


# 定义
"""
def 函数名():
    代码块(函数体)

代码块：封装这个函数的功能
"""
a = "AAAAAAAAAAAAAAAAAAAAAAAAA"


# 函数定义
def print_a():
    for j in range(5):
        print(a)


# 调用
"""
函数名()
"""
print_a()
print(111)
print_a()
print(222)
print_a()

# 说明：
"""
1. 函数名要符合标识符的命名规范
2. 函数在定义的时候，函数体里面的代码不会执行
3. 函数体中的代码，只有在函数调用的时候才会执行
4. 定义好的函数可以多次被调用
5. 函数需先定义再调用。Python是按顺序执行的，如果在函数定义之前调用函数，会引发NameError错误。
"""
# 特点：
"""
一次定义多次使用
"""
# 作用：
"""
1. 减少冗余代码
2. 提高代码的可维护性
"""
