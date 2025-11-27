def wrapper(fn):
    def inner():
        print('前置功能拓展')
        result = fn()
        print(f'后置功能拓展  {result}')
        return result + 1
    return inner


@wrapper
def demo():
    # print(1 + 1)
    return 1 + 1


demo()
print(demo())    # 调用demo()实际上返回的是装饰器inner函数的返回值，如果inner函数没有显式返回值，默认返回None
