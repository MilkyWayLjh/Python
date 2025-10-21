"""
定义:
    通过继承，子类可以拥有父类的资源(属性和方法).子类可以拥有自己的资源.
继承解决的问题:
    共性提取
B类继承A类:
    A类叫做  父类, 基类, 超类
    B类叫做  子类, 派生类

#  B类继承A类
class A:
    pass

class B(A):
    pass
"""


# 员工类
class Staff:
    def __init__(self, name, age, num):
        self.name = name
        self.age = age
        self.num = num
        self.type = '人类'

    def fn(self):
        print('它是员工')


# 讲师类
class Teacher(Staff):
    sex = '男'
    type = '人'

    def fn(self):
        print('它是讲师')


t = Teacher('鹿人', '22', '001')
print(t.name, t.age, t.num, t.sex, t.type)  # 鹿人 22 001 男 人类
t.fn()
