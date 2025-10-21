"""
在类的内部操作对象属性，本质就是在对象方法中操作对象属性，在self上来操作对象属性
"""


# 定义类
class Person:
    name = '李同学'

    def set_age(self):
        # 设置属性
        self.age = '22'

    def get_age(self):
        print(self.age)

    def update_age(self):
        self.age = '23'

    def del_age(self):
        del self.age


p1 = Person()
print(p1.name)
# 调用对象方法
p1.set_age()  # 设置
p1.get_age()  # 获取
p1.update_age()  # 修改
p1.get_age()  # 获取
# p1.del_age()  # 删除
print(p1.age)
