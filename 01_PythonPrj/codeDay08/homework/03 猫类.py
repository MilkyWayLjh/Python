# 新建一个文件，定义一个猫类，创建一个猫对象，调用上面的属性和方法
class Cat:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def __str__(self):
        return 'this is 🐱'

    def eat(self, food='🐟'):
        print(f'{self.name}在恰{food}')

    def catch(self, animal='🐀'):
        print(f'{self.name}在抓{animal}')

cat = Cat('假老练', 2, 'blue')
print(cat)
print(cat.name, cat.age, cat.color)
cat.eat()
cat.catch()

