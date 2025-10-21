# 新建一个文件，定义一个狗类，创建一个狗对象，调用上面的属性和方法
class Dog:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def __str__(self):
        return 'this is 🐶'

    def eat(self, food='💩'):
        print(f'{self.name}在恰{food}')

    def chase(self, person):
        print(f'{self.name}在追{person}')

dog = Dog('莽哥', 2, 'yellow')
print(dog)
print(dog.name, dog.age, dog.color)
dog.eat()
dog.chase('小偷')

