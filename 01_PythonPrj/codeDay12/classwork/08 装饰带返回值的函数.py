def wrapper(fn):
    def inner():
        print('前置功能拓展')
        result = fn()
        print('后置功能拓展')
        return result
    return inner


@wrapper
def demo():
    return 1 + 1

print(demo())


