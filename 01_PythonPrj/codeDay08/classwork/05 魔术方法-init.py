"""
python类中内置的具有特殊功能的方法
魔术方法不需要我们手动调用
在对类的实例进行一些操作的时候会触发魔术方法的执行
魔术方法的命名方式: __名字__

● __init__   （构造函数）[掌握]
对象属性初始化方法
触发机制:对象创建以后,自动执行这个方法. 即当创建对象以后，init自动执行。。在__new__创建对象后自动调
作用: 用来初始化对象的属性。负责初始化已创建的实例对象
说明：以后对象属性的初始化，都在init方法中设置
"""


# 定义类
class Person:
    def __init__(self, name, age):
        print('_____init_____')
        self.name = name
        self.age = age


# 创建对象
p1 = Person('张老师', 2)  # 人的实例
print(p1.name)
print(p1.age)

p2 = Person(name='李同学', age=1)
print(p2.name)
print(p2.age)
