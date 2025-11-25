"""
闭包概念
● 概念
    在函数嵌套的前提下，内部函数使用了外部函数的变量，并且外部函数返回了内部函数，我们把这个使用外部函数变量的内部函数称为闭包。
● 闭包构成
    1. 在函数嵌套(函数里面再定义函数)的前提下
    2. 内部函数使用了外部函数的变量(还包括外部函数的参数)  如果要修改需要使用 nonlocal 关键字
    3. 外部函数返回了内部函数

nonlocal关键字用来在函数或其他作用域中使用并修改外层(非全局)变量（逐层到外面作用域找，直到全局作用域之前的局部作用域）。
意义：nonlocal使用能够弥补global和闭包的两个问题。
对于global，只能使用全局变量，对于嵌套函数中的内层函数而言，无法通过global使用外层函数，通过nonlocal就可以，当然直接读取也可以（闭包）。
对于闭包，内层函数可以读取外层函数的变量，但是如果在内部函数中尝试进行修改外部变量，且外部变量为不可变类型，则需要在变量前加nonlocal，如果变量为可变类型，则不需要添加nonlocal。

使用总结：
1、局部作用域改变全局变量用global， global同时还可以定义新的全局变量
2、内层函数改变外层函数变量用nonlocal， nonlocal不能定义新的外层函数变量，只能改变已有的外层函数变量
3、同时nonlocal不能改变全局变量
"""


def f():
    print(123)


def wrapper(var):
    var()
    num = 1

    def inner():
        # nonlocal num
        # num += 1
        print(num)

    return inner


def wrapper1(num):
    def inner():
        return num

    return inner


wrapper(f)
wrapper(f)()

print(wrapper1(1))
print('---')
print(wrapper1(1)())

fn = wrapper1(10)   # wrapper1(10) = inner
print('---')
print(fn())
