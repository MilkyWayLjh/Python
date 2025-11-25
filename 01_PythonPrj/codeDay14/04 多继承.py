# 子类重写父类的属性和方法
# 子类调用父类的属性和方法
class A:
    def info(self):
        super(A, self).info()  # C.info()
        print('a')


class C:
    def info(self):
        print('c')


# 按继承父类的传参顺序，优先查找A
class B(A, C):
    def info(self):
        super().info()  # super(B, self).info()  # A.info()
        print('b')


# MRO查找原则
print(B.__mro__)    # (<class '__main__.B'>, <class '__main__.A'>, <class '__main__.C'>, <class 'object'>)

b = B()
b.info()    # c a b
