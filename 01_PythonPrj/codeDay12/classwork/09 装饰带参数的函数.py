def wrapper(fn):
    def inner(*args, **kwargs):
        print('前置功能拓展')
        result = fn(*args, **kwargs)
        print('后置功能拓展')
        return result
    return inner


@wrapper
def demo(a, b):
    return a + b


print(demo(1, 1))
print(demo(2, 2))
