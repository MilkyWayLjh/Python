"""
# 第一种
try:
    可能发生异常的代码
except (异常的类型1, 异常类型2, ...):
    捕获异常执行的代码

# 第二种
try:
    可能发生异常的代码
except 异常类型1:
    发生异常1,执行的代码
except 异常类型2:
    发生异常2,执行的代码
except ...:
    pass
"""
# 第一种方式
try:
    # 接收用户输入
    num = int(input('>>>请输入数字：'))
    result = 1 / num
    print(result)
except (ZeroDivisionError, ValueError):
    print('输入的数字不合法!')

# 第二种方式
try:
    num = int(input('>>>输入数字：'))
    result = 1 / num
    print(result)
except ZeroDivisionError:
    print('输入的数字不能是0!')
except ValueError:
    print('输入的不能是非数字!')


