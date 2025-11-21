"""
为什么需要自定义异常类
    系统中的内置异常类，不满足我们的需求，就可以自定义异常类。

三步:
    1.自定义异常类
    2.抛出异常类/类实例
    3.捕获异常
"""
"""
自定义异常类
语法：
class NameError(Exception):
    def __str__(self):
        return '异常描述信息'
"""


class LenError(Exception):  # 自定义异常
    def __str__(self):  # 打印实例时返回描述信息
        return '长度不符合要求'


"""
抛出自定义异常
语法：
    raise NameError
    raise NameError()
    raise NameError('描述信息')
抛出异常 的关键字是 raise
raise 用于向外部抛出异常，后边可以跟一个异常类，或异常类的实例。
"""
# 用户名的长度必须是大于8个，小于24个字符
# 接收用户输入
username = input('>>>用户名：')
try:
    if (len(username) >= 8) and (len(username) <= 24):
        print('用户名可以使用')
    else:
        raise LenError()    # 抛出异常, 抛出错误信息  长度错误类型：长度不符合要求
except LenError as e:   # 捕获异常
    print('捕获异常')
    print(e)
    print(LenError())
