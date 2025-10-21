"""
使用while，完成以下图形的输出
*
**
***
****
*****
"""
i = 1
while i <= 5:
    j = 1
    while j <= i:
        print('*', end='  ')
        j += 1
    print()
    i += 1

