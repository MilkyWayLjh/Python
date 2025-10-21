# 类成员：类属性和类方法
"""
类属性和类方法属于整个类，可以通过类名访问，也可以对象访问
"""


class Person:
    # 类属性
    country = '中国'


# 在类外部访问类属性
# 通过类名访问类属性
# 语法：类名.类属性名
print(Person.country)
p1 = Person()
print(p1.country)

# 修改
Person.country = 'China'
print(Person.country)

# 对象并不能修改类的属性，只是自己设置了一个相同的对象属性
p1.country = 'C'
print(p1.country)
print(Person.country)

"""
注意事项：千万不要将实例属性和类属性使用相同的名字
    1.类属性和实例属性重名时，相同名称的实例属性将屏蔽掉类属性
    2.通过实例对象是不能修改一个类属性的，想当于绑定了一个新的实例属性
"""


class Person1:
    country = '中国'

    # 类方法
    @classmethod    # 装饰器
    def get_country(cls):
        print(cls.country)

    @classmethod    # 装饰器
    def set_country(cls):
        cls.country = 'China'


# print(Person1)
Person1.get_country()
Person1.set_country()
Person1.get_country()
# 通过实例访问
print('------')
Person1().get_country()
