# 继承方式

# 单继承 掌握
# 人类
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f'{self.name}吃东西')


# 学生类
class Student(Person):
    def study(self):
        print(f'{self.name}学习')


"""
student = Student('hello', 12)
student.eat()
student.study()
"""


# Pig类
class Pig:
    def sleep(self):
        print(f'{self.name}睡')


# 多继承
# PeiQi 继承 Pig Person
class PeiQi(Person, Pig):
    pass


pei_qi = PeiQi('佩奇', 5)
pei_qi.eat()
pei_qi.sleep()
