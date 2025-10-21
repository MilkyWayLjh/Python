def fn1():
    result = 1 / 0


def fn2():
    fn1()


def fn3():
    try:
        fn2()
    except ZeroDivisionError as e:
        print(e)

fn3()

