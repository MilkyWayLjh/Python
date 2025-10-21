import time


def decorator(fn):
    def inner(*args, **kwargs):
        # 开始时间
        start = time.time()
        result = fn(*args, **kwargs)
        end = time.time()
        print(f'运行时间为：{end - start}')
        return result
    return inner


@decorator
def info():
    for i in range(1000000):
        pass


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


if __name__ == '__main__':
    post()
    comment()
    info()

