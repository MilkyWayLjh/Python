name = 'hello'


def fn():
    for i in name:
        print(i, end=' ')
    print()


class A:
    @staticmethod
    def prt():
        print(name)

    def __str__(self):
        return name

# 魔术变量 __all__
# 指定当前模块在import * 时，可以被导入的资源
# 注意：列表中写的是资源的字符串名称
__all__ = ['name', 'fn']

