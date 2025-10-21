# 递归函数：在函数内调用函数(设置临界条件)
# 斐波那契数列：当前项=前两项之和  num(n)=num(n-1)+num(n-2)
def func(num):
    if num == 1 or num == 2:
        return 1
    else:
        return func(num-1) + func(num-2)

print(func(6))


# 使用 yield 实现斐波那契数列：(利用迭代器和生成器)
# import sys
#
#
# def fibonacci(n):  # 生成器函数 - 斐波那契
#     a, b, counter = 0, 1, 0
#     while True:
#         if counter > n:
#             return
#         yield a
#         a, b = b, a + b
#         counter += 1
#
#
# f = fibonacci(10)  # f 是一个迭代器，由生成器返回生成
#
# while True:
#     try:
#         print(next(f), end=" ")
#     except StopIteration:
#         sys.exit()
