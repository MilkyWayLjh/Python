# 通用装饰器
def decorator(fn):
    def inner(*args, **kwargs):
        print('前置功能拓展')
        result = fn(*args, **kwargs)
        print('后置功能拓展')
        return result
    return inner


@decorator
def demo(a, b, c, d):
    return a * b * c + d


if __name__ == '__main__':
    print(demo(2, 3, c=4, d=5))
