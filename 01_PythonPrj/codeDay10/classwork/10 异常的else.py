"""
else表示的是如果没有异常要执行的代码。
try:
    可能发生异常的代码
except Exception as result:
    发生异常执行的代码
else:
    没有异常的时候执行的代码
"""
try:
    num = int(input('>>>数字：'))
    result = 1 / num
except Exception as e:
    print('捕获到异常了~')
    print(e)
else:
    print(f'没有异常，1 ➗ {num} = {result}')
