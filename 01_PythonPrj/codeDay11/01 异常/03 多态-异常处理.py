"""
通过一个接口，传入不同的对象，调用相同的方法，产生不同的结果
多态实现：
1. 子类继承父类
2. 子类重写父类的方法
3. 调用这个方法
"""


# 动物类
class Animal:
    def call(self):
        print('动物叫')


# 狗类
class Dog(Animal):
    def call(self):
        try:
            1 / 0
        except NameError:
            print('dog')
        print('旺旺叫')


# 猫类
class Cat(Animal):
    def call(self):
        try:
            print(hello)
        except ZeroDivisionError:
            pass
        print('喵喵叫')


# 人类
class Person(Animal):
    pass


# 普通调用方法
"""
dog = Dog()
cat = Cat()

dog.call()
cat.call()
"""


# 定义一个统一的接口(函数)来调用这个方法
# 类型 obj
def do_call(obj):
    """
    处理多态的执行结果
    :param obj: 类的实例
    :return:
    """
    try:
        obj.call()
    except Exception as e:
        print(e)


do_call(Dog())
do_call(Cat())
do_call(Person())
