"""
匿名函数：
lambda表达式

语法：
lambda x, y:表达式
特点：
    lambda会把表达式执行结果返回
"""


# 需求：求2个数的和
def sum1(x, y):
    return x + y


print((lambda x, y: x + y)(1, 2))

sum2 = lambda x, y: x + y
print(sum2(1, 2))

print((lambda: 1 + 1)())


def fn(a, b, operator):
    """
    计算器
    @param a: 数字1
    @param b: 数字2
    @param operator: 计算操作的函数
    @return: 返回计算的结果
    """
    return operator(a, b)


def add(x, y):
    return x + y


def sub(x, y):
    return x - y


print(fn(2, 1, add))
print(fn(2, 1, sub))

print(fn(2, 1, lambda x, y: x + y))
fn(2, 1, lambda x, y: x - y)
fn(2, 1, lambda x, y: x * y)
fn(2, 1, lambda x, y: x / y)
print(fn(2, 1, lambda x, y: x // y))
