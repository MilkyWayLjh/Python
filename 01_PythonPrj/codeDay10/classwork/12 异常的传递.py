# 函数嵌套
# 函数嵌套异常传递
def fn1():
    result = 1 / 0


def fn2():
    fn1()


def fn3():
    try:
        fn2()
    except ZeroDivisionError:
    # except ValueError:
        print('函数运行有问题')

fn3()


# try嵌套
# 异常只要没有被捕获就一直向外传递，如果最后没有捕获到，就抛出错误信息到终端
try:
    try:
        num = int(input('数字：'))
        result = 1 / num
        print(result)
    except ValueError:
        print('输入的数字不能是字符')
except ZeroDivisionError:
    print('传入的数字不能是0')


