"""
下面的程序执行结果是：
x = 1
def change(a):
    global x
    x += 1
    print(x)
change(x)
"""
x = 1


def change(a):
    global x    # 将x声明为全局变量以便可以进一步修改
    x += 1     # x = x + 1  即 1 + 1 = 2
    print(x)    # 打印 2
change(x)   # 传入x = 1

# 程序执行结果为：2
