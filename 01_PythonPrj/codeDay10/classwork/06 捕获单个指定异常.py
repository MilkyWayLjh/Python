"""
try:
    可能发生异常的代码
except 异常的类型:
    捕获到异常后执行的代码

"""
try:
    num = int(input('输入数字: '))
    result = 1 / num    # 分别输入 1、0、hello
except ZeroDivisionError:   # 如果类型指定错误，会抛出异常，也就不会执行下面的代码块
    print('0不能被除!')

print('Hello Zeus!')


