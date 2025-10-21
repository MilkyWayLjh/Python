# 函数注释（函数说明文档）

# def fn():
#     """
#     函数注释
#     """

# help(fn)  # 查看函数的说明文档


def result(a, b):
    """
    求两个数的鸡
    :param a: 数字1
    :param b: 数字2
    :return: 数字1和数字2的乘积
    """
    return a * b


print(result(2, 4))

help(result)

help(print)
