"""
装饰器概念
● 说明：
    就是给已有函数增加额外功能的函数，它本质上就是一个闭包函数。
    装饰器就是一个特殊的闭包
● 特点：
    1.不修改已有函数的源代码
    2.不修改已有函数的调用方式
    3.给已有函数增加额外的功能
"""


def wrapper(fn):
    def inner():
        print('前置功能拓展')
        fn()
        print('后置功能拓展')
    return inner


def fn1():
    print('this is fn1')


def fn2():
    print('this is fn2')


# wrapper(fn1)()
fn1 = wrapper(fn1)
fn1()
print('---'*3)
fn2 = wrapper(fn2)
fn2()
