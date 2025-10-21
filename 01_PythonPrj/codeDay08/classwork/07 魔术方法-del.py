"""
● __del__  （析构函数）
触发机制：当对象被销毁时执行这个方法 del obj, 当脚本执行完毕以后，所有的数据都会自动销毁
作用：在对象被销毁时可以做一些销毁之后的收尾工作
"""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'我是{self.name}, 我有{self.age}岁了'

    def __del__(self):
        print('对象被销毁，__del__方法执行')


p = Person('李同学', 22)
print(p)
# del p     # 使用del销毁对象时会触发__del__方法并打印. 如果不使用del，那么会在程序执行完之后自动销毁，并在最后执行__del__方法并打印
print('the code last line')
