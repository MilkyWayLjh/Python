# 在python中没有绝对的权限设置，主要是一种约定形式。可以通过特殊手段访问到任何权限的属性和方法

class Person:
    def __init__(self):
        # 受保护权限
        self._name = 'hello'
        # 私有权限
        self.__age = 18

    def __fn(self):
        return self._name


class Staff(Person):
    def get_name(self):
        print(self._name)


staff = Staff()
staff.get_name()

# 受保护权限可以直接访问
# print(staff._name)
person = Person()
print(person._name)

# 私有权限也可以直接访问
# 私有权限：_类名__私有权限名字
print(person._Person__age)
print(person._Person__fn())
