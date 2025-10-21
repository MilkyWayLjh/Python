"""
配合循环使用的 else
语法：
while 条件:
    循环体
    break
else:
    代码块

else代码块执行机制：
在循环体中没有break执行的情况下，else在循环执行完后执行。
如果有break执行，那么else代码块不执行。
"""

# 没有break
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print('循环结束了')
print('==' * 20)

# 存在break
i = 1
while i < 6:
    if i == 3:
        break
    print(i)
    i += 1
else:
    print('循环结束了')
