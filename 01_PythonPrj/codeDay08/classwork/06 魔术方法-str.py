"""
● __str__
触发机制: 当对象被print打印的时候,触发str方法执行
使用注意: str方法必须返回字符串类型
作用: 默认print打印对象,输出的是对象的地址.通过str方法可以返回自定义的一个字符串。
    打印对象的时候，不是返回对象的内存地址，而是返回对象的标识信息
"""


# 定义类
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'我叫{self.name}, 我有{self.age}岁了'


# 创建对象
p1 = Person('张老师', 20)
print(p1)  # 触发魔术方法str执行

p2 = Person('李同学', 18)
print(p2)  # 触发魔术方法str执行
