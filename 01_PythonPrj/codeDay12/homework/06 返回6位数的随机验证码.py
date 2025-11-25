# 封装一个函数, 返回6位数的随机验证码
import random


def random_verification_code():
    return '%06d' % random.randint(0, 999999)


if __name__ == '__main__':
    print(random_verification_code())
