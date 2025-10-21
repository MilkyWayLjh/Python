# 返回多个值：return后面多个值之间用逗号分割，返回的多个值是元组类型


def fn1():
    return 1, 2, 3


def fn2():
    print('111')


data = fn1()
print(data)  # (1, 2, 3)

# 拆包
a, b, c = fn1()
print(a, b, c)
