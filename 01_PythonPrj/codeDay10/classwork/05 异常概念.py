"""
介绍:
    python解释器在执行代码的时候抛出的错误信息
特点:
    1. 显示错误的原因，错误的位置
    2. 阻止代码继续向下执行
异常组成:
    ● Traceback  指出错误的位置
    ● 异常类型: 异常描述信息
异常类型:
    ● 错误类型，就是python中内置的一些类
    ● python中内置了大量的错误类型
    ● 通过这些错误类型就可以捕获错误了
异常捕获:
     是指在程序代码运行过程中,遇到错误, 不让程序代码终止,让其继续运行, 同时可以给使用者一个提示信息
"""
num = int(input('输入数字: '))
result = 1 / num

print(result)   # 1/0  ZeroDivisionError: division by zero

print(111)

