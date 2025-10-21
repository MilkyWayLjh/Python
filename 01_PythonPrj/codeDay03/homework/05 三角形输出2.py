"""
使用while，找规律输出
*
***
*****
*******
*********
"""
# 分析：i为行，j为列。j = 2 * i - 1
i = 1
while i <= 5:
    j = 1
    while j <= 2 * i - 1:
        print('*', end='')
        j += 1
    print()
    i += 1

