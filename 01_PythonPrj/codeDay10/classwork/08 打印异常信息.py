"""
try:
    可能发生异常的代码
except (异常的类型1, 异常类型2, ...) as 变量名:
    发生异常执行的代码
    print(变量名)
"""
# 打印异常信息
# 单个异常

try:
    num = int(input('输入数字：'))
    result = 1 / num
    print(result)
except ZeroDivisionError as e:
    print(e)   # 打印除了错误描述信息

# 多个异常
try:
    num = int(input('输入数字：'))
    result = 1 / num
    print(result)
except (ZeroDivisionError, ValueError) as e:
    print(e)
