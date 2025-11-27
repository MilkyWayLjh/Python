# 定义装饰器
def wrapper(fn):
    def inner():
        print('前置功能拓展')
        fn()
        print('后置功能拓展')
    return inner


# 装饰器的语法糖形式
# 语法：在被装饰函数上添加@装饰器的名称
# wrapper装饰器对demo1函数进行装饰
@wrapper    # @wrapper => demo = wrapper(demo)
def demo():
    print('this is demo')


# demo = wrapper(demo)
# demo()
demo()
