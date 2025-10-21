# 子类调用父类的同名方法
"""
如果要重写构造函数，必须在构造函数中使用 super() 方法实现继承，并且还要传递必要的参数
在函数中定义的其它属性，一定要在 super() 之后定义

super() 函数是用于调用父类(超类)的一个方法。
    super() 是用来解决多重继承问题的，直接用类名调用父类方法在使用单继承的时候没问题，
        但是如果使用多继承，会涉及到查找顺序（MRO）、重复调用（钻石继承）等种种问题。
    MRO 就是类的方法解析顺序表, 其实也就是继承父类方法时的顺序表。
语法: super(type[, object-or-type])
参数:
    type -- 当前子类
    object-or-type -- 类，一般是 self
    Python3 可以使用直接使用 super().xxx 代替 super(Class, self).xxx
"""


# 定义商品类
class Goods:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def fn(self):
        print('this is Goods')


# 定义手机类
class Phone(Goods):
    # phone的对象属性: name price(单价) capacity(容量) size(尺寸)
    def __init__(self, name, price, capacity, size):
        # 子类调用父类的方法
        super().__init__(name, price)   # name price
        self.capacity = capacity
        self.size = size

    def fn(self):
        # super(Phone, self).fn()   # 用子类对象调用父类已被覆盖的方法(类内部)
        super().fn()
        print('this is Phone')


p1 = Phone('Huawei', 1999, '100G', '7')
print(p1.name)
print(p1.price)
print(p1.capacity)
print(p1.size)
p1.fn()
super(Phone, p1).fn()  # 用子类对象调用父类已被覆盖的方法(类外部)
