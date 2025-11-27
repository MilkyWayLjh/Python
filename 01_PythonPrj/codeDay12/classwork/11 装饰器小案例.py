import time


def check(fn):
    def inner(*args, **kwargs):
        print('登录验证')
        result = fn(*args, **kwargs)
        return result
    return inner


# 发帖
@check
def post():
    # 登录验证
    print('发帖')


# 评论
@check
def comment():
    # 登录验证
    print('评论')


def decorator(fn):
    def inner(*args, **kwargs):
        start = time.time()     # 增加前置开始时间记录
        result = fn(*args, **kwargs)    # 运行被装饰的函数
        end = time.time()   # 添加后置结束时间记录
        print(f'运行时间为：{end - start}')   # 计算运行时间
        return result
    return inner


@decorator
def info():
    for i in range(10000):
        if i % 2 == 0:
            print(i)


if __name__ == '__main__':
    info()
    post()
    comment()
