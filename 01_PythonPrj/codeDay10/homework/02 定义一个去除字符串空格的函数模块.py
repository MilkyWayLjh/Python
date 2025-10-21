"""
定义一个函数模块:
    可以去除传入的字符串里面的所有空格，返回去除空格之后的字符串
"""


def remove_space(string):
    # return string.replace(' ', '')
    return ''.join(string.split())


s1 = ' how are you? im fine thanks and you? im fine, too '
print(remove_space(s1))
