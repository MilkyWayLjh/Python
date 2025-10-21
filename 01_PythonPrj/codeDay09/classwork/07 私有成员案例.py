class Person:
    def __init__(self, name, age):
        # 私有属性
        self.name = name
        self.__age = age

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if 1 <= age <= 120:
            self.__age = age
        else:
            print('年龄不合法')


p1 = Person('hello', 19)
# p1 = Person('hello', -19)
print(p1.name)
print(p1.get_age())

# 修改年龄
p1.set_age(-29)
print(p1.get_age())
# p1.__age = 29
# print(p1.__age)
#
# # 修改年龄
# p1.__age = -29
# print(p1.__age)

print(dir(Person))  # name 和 __age 都是在 init 方法中通过 self 定义的实例属性，只有在创建具体实例时才会存在，Person 类本身作为类对象，并不包含这些实例属性
print(dir(p1))
