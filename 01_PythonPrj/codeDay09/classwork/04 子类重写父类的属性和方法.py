# 子类和父类的属性方法名相同的时候,就是重写
# 定义商品类
class Goods:
    def __init__(self):
        self.name = '商品'

    def __str__(self):
        return self.name

    def fn(self):
        print('商品类')


# 定义手机类
class Phone(Goods):
    # 重写init方法
    def __init__(self):
        # super(Phone, self).__init__()
        super().__init__()  # python3中可以省略
        self.name = '手机'

    def fn(self):
        print('手机')


# 调用
p1 = Phone()
print(p1.name)
p1.fn()
