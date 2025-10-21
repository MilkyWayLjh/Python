"""
__new__方法
python 内置的魔术方法
    作用：创建类的实例并且返回。负责创建类的实例对象
    触发：创建类的实例的时候。在对象创建时首先被调用
    new方法不能随便写，必要要返回类的实例。
"""
"""
详解：
    新创建一个对象的时候，python解释器自动调用类上的__new__()。
    该方法至少要有一个参数cls，代表需要实例化的类，由python解释器自动传入，并且必须返回通过该类新实例化出来的实例对象
    （还记得我们初始化方法__init__()第一个参数self代表的是该类的实例对象，而这个实例正是__new__()返回给它的）。

    我们自己定义的所有的类都可以追溯到基类object上，所以通过类创建对象的时候都会成功自动到基类上的__new__()，从而得到创建好的对象

__new__方法注意事项:
    1.__new__至少要有一个参数cls，代表要实例化的类，此参数在实例化时由Python解释器自动提供。
    2.__new__必须要有返回值，返回实例化出来的实例，这点在自己实现__new__时要特别注意，一般return 父类 __new__出来的实例
    3.__init__有一个参数self，就是这个__new__返回的实例,__init__在__new__的基础上可以完成一些其它初始化的动作，__init__不需要返回值
    4.如果创建对象时传递了自定义参数，且重写了__new__方法，则__new__也必须"预留"该形参,用不用都无所谓,否则__init__()方法将无法获取到该参数
"""


# class Person(object): # 继承自object类
class Person:
    def __new__(cls, name, *args, **kwargs):
        # 返回父类的new方法
        # return object.__new__(cls, *args, **kwargs)
        print(super().__new__(cls, *args, **kwargs))
        return super().__new__(cls, *args, **kwargs)

    def __init__(self, name):
        print(self, name)


p1 = Person('Zeus')
# print(p1)

# p2 = Person()
# print(p2)
