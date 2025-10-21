"""
● type  查看数据类型
● dir  查看对象上所有属性和方法
● isinstance  查看对象是否属于某个类. True|False

"""
# type  查看对象的类型
print(type(123))    # <class 'int'>


# dir  查看对象上所有方法和属性
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f'{self.name}吃脑子🧠')


p = Person('僵尸', '1000')
p.eat()
print(dir(Person))
print(dir(p))

# isinstance(变量, 类名)  判断一个变量是否是我们需要的指定的类型
age = p.age     # age: <class 'str'>
print(isinstance(age, int))     # False
