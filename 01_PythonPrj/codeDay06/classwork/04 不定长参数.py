"""
不定长参数(万能参数)：
    可以传入任意多个参数
不定长参数类型：
    位置不定长: 可以接收任意多个位置参数，会以元组类型将所有位置参数打包在args变量中
    关键字不定长：可以接收任意多个关键字参数，会以字典类型将所有关键字参数打包在kwargs变量中
"""


# 位置不定长参数
def fn1(*args):
    print(args)  # tuple


fn1(1, 'a', 'b', 'hello', 'xxx')


# 关键字不定长参数
def fn2(**kwargs):
    print(kwargs)


fn2(a=1, b=2, c='hello')


# 混合使用
def fn3(*args, **kwargs):
    print(args)
    print(kwargs)


fn3(1, 2, 3, a=1, b=2, c=3)


# 必填参数 > 默认参数 > 位置不定长参数 > 关键字不定长参数
def fn4(a, b, name='hello', *args, **kwargs):
    print(a, b)
    print(name)
    print(args)
    print(kwargs)


fn4(1, 2, '3', 4, c=6)      # 当 默认参数 > 位置不定长参数 的时候，默认参数可以按照 位置 来传递


# 必填参数 > 位置不定长参数 > 默认参数 > 关键字不定长参数
def fn5(a, b, *args, name='hello', **kwargs):
    print(a, b)
    print(name)
    print(args)
    print(kwargs)


fn5(1, 2, 3, name='4', c=6)     # 当 位置不定长参数 > 默认参数 的时候，默认参数需要按照 关键字 来传递
