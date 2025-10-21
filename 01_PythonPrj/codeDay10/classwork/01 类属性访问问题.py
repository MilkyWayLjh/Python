"""
类属性，可以通过类访问，也可以通过对象访问
对象属性和对象方法, 只能通过对象/实例去访问, 强行用类名去访问对象属性会报错, 用类名去访问对象方法需要手动传入对象self->Person()
"""


class Person:
    # 类属性
    country = '中国'
    __country = 'China'

    def __init__(self):
        self.q = 'q'

    @classmethod
    def set_country(cls, name):
        if name == 'China':
            cls.__country = name
        elif name == '中国':
            cls.__country = name
        else:
            print('Fail')
        print(cls.__country)

    def get_country(self):
        print(self.country)
        print(self.__country)

    def fn(self):
        print(f'{self.country}~')


p1 = Person()
p1.get_country()
p1.set_country('中国')
p1.get_country()

Person.fn(Person())
# print(Person.q)     # AttributeError: type object 'Person' has no attribute 'q'
