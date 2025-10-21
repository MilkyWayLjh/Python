def single_decorator(cls):
    obj = None

    def inner(*args, **kwargs):
        # print('前置拓展功能')
        nonlocal obj
        if not obj:
            obj = cls(*args, **kwargs)
        # print('后置拓展功能')
        return obj
    return inner


# 装饰器的本质 Fn = decorator(Fn)，装饰器返回类本身，还是之前的类，只是在返回之前增加了额外的功能
@single_decorator
class Fn:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'{self.x} + {self.y} = {self.x + self.y}'


# f1 = Fn()
# f2 = Fn()
# print(f1)
# print(f2)

f3 = Fn(1, 2)
print(f3, id(f3))
f4 = Fn(2, 3)
print(f4, id(f4))   # 还是1, 2 只能创建一个对象
