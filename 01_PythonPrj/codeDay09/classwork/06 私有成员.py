"""
私有成员：具有私有权限的属性和方法
私有权限：只能在类的内部访问，也就是说 子类不能继承父类中的私有方法和私有属性
    原理了解:
        通过函数dir(类名)查看所有可以访问的方法,python解析器将私有方法的名称偷偷的的修改成了(_类名__方法名),
        所有我们通过原来的方法名去访问肯定是访问不到的

# 语法：
私有属性: __attr = value
私有方法: __fn()
"""


class Person:
    __age = 22

    def __init__(self):
        # 私有属性
        self.__name = 'hello'

    def get_info(self):
        print(self.__name)
        print(self.__age)
        self.__fn()

    @staticmethod
    def __fn():
        print('fn')


p1 = Person()
p1.get_info()


# 在类的外部访问私有属性 - 不能
# print(p1.__name)
# p1.__fn()
# print(Person.__age)
print(dir(Person))
# 通过 _类名__方法名 或 _类名__属性名 强行访问
print(p1._Person__name)
p1._Person__fn()
print(Person._Person__age)


# 在派生类中
class Student(Person):
    def get_info(self):
        print(self.__name)  # 调用不到
        self.__fn()  # 调用不到


# 在派生类中访问私有属性 - 不能
s1 = Student()
# s1.get_info()     # AttributeError: 'Student' object has no attribute '_Student__name'
print(dir(Student))
s1._Person__fn()
