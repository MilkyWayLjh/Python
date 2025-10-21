"""
单例类:
    在程序中,有的情况下,我们只需要某个类只有一个实例就可以完成所有的功能,没有必要通过该类创建多个对象从而浪费内存空间,这样的类称为单例类。
单例模式：
    一个类只能创建一个对象 (创建对象的内存地址相同 只有一个)

实现单例模式:
·保证通过类只能创建出一个对象：
    1.重写__new__()方法，自定义创建对象，保证只创建一次对象：只有当没有创建过对象才创建，如果已经创建就直接返回创建过的对象
    2.使用一个私有的类属性保存创建好的对象，设置为私有的可以保护类属性不被修改
·保证对象只初始化化一次
    1.既然只能创建一个对象，那么初始也只能初始化一次
    2.使用一个私有的类属性 __has_init 是否已经初始化
    3.在初始化方法__init__()中判断是否已经初始化过，如果没有才进行初始化
"""

"""
class Singleton:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super().__new__(cls, *args, **kwargs)
        return cls.__instance

s1 = Singleton()
print(s1)
s2 = Singleton()
print(s2)
"""


# 完整代码：
# 单例
# class Singleton(object):
class Singleton:
    # 保存创建好的对象
    __instance = None
    # 是否已经初始化
    __has_init = False

    # 自定义创建对象
    def __new__(cls, name, age, *args, **kwargs):
        # 没有创建对象才创建
        if not cls.__instance:
            cls.__instance = super().__new__(cls, *args, **kwargs)
        return cls.__instance

    # 初始化属性
    def __init__(self, name, age):
        if not self.__has_init:
            # 没有初始化才初始化
            self.name = name
            self.age = age
            self.__has_init = True

    def __str__(self):
        return "我的名字为%s,今年%d" % (self.name, self.age)

# 创建两次对象
s1 = Singleton('亚索', 22)
s2 = Singleton('永恩', 23)
print(s1)
print(s2)   # 第二个对象创建失败
# 我的名字为亚索,今年22
# 我的名字为亚索,今年22


