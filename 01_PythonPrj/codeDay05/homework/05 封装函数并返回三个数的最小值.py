# 封装函数,实现返回三个数的最小值

# def _min(m, n, p):
#     return min(m, n, p)
#
# print(_min(3, 6, 9))

_a, _b, _c = input('请输入三个数(以空格隔开): ').split()
a, b, c = int(_a), int(_b), int(_c)


def _min(m, n, p):
    if m < n:
        i = m
    else:
        i = n
    if p < i:
        print(f'最小值是: {p}')
    else:
        print(f'最小值是: {i}')

_min(a, b, c)
