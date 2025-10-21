# while循环嵌套
"""
while 条件表达式1:
    满足条件的循环体...
    while 条件表达式2:
        满足条件的循环体...
"""
# 需求：打印正方形
# i = 1
# while i <= 5:
#     j = 1
#     while j <= 5:
#         print('*', end='  ')
#         j += 1
#     print()
#     i += 1

# 需求：打印三角形
# i = 1
# while i <= 5:
#     j = 1
#     while j <= i:
#         print('*', end='  ')
#         j += 1
#     print()
#     i += 1

# 需求：打印三角形 1 3 5 7 9
# 分析：i为行，j为列。j = 2 * i - 1
# 方法一：
i = 1
while i <= 5:
    j = 1
    while j <= 2 * i - 1:
        print('*', end='')
        j += 1
    print()
    i += 1
# 方法二：
# for i in range(1, 6):
#     for j in range(1, 2 * i - 1):
#         print('*', end='')
#     print()
