"""
while 条件语句:
    条件成立,重复执行这里的代码块
else
    条件不成立,执行这里的代码块
"""
# 没有break的情况
# i = 1
# while i <= 3:
#     print(i)
#     i += 1
# else:
#     print('else执行了')

# 有break的情况
# i = 1
# while i <= 3:
#     if i == 2:
#         # i += 1
#         # continue
#         break
#     print(i)
#     i += 1
# else:
#     print('else执行')

# 猜数字游戏：
# import random
# num = random.randint(0, 10)
# # print(num)
# count = 0
# while True:
#     num1 = int(input('输入一个整数进行猜测: '))
#     count += 1
#     if num1 == num:
#         print(f'猜对了，有奖励噢! 你总共猜了{count}次!')
#         break
#     elif num1 < num:
#         print('猜小了，再试一次！')
#     else:
#         print('猜大了，再试一次！')


# 需求1：打印出1-100的值
# 方法一：
# i = 1
# while i <= 100:
#     print(i)
#     i += 1
# 方法二：
# for i in range(1, 101):
#     print(i)

# 需求2：1-100的和
# 方法一：
# i, result = 1, 0
# while i <= 100:
#     result += i
#     i += 1
# else:
#     print(result)
# 方法二：
# result = 0
# for i in range(101):
#     result += i
# print(result)

# 需求3：1-100 奇数/偶数 和
# 方法一：
# i, result = 1, 0    # 奇数
# # i, result = 2, 0    # 偶数
# while i <= 100:
#     result += i
#     i += 2
# print(result)
# 方法二：
# i, result = 1, 0
# while i <= 100:
#     # if i % 2 == 1:    # 奇数
#     if i % 2 == 0:  # 偶数
#         result += i
#     i += 1
# print(result)

# 需求4：你女朋友要求你是说100遍 “我爱你！”，但是说到60遍就不想听了
# i = 1
# while i <= 100:
#     print(f'第{i}遍我爱你！')
#     if i == 60:
#         break
#     i += 1
# print('我已经说完啦~')

# 需求5：你女朋友要求你是说100遍“我爱你！”，但是觉得第44遍不吉利，要求跳过44遍。
# i = 1
# while i <= 100:
#     if i == 44:
#         print('这一遍我不说哦~')
#         i += 1
#         continue
#     print(f'第{i}遍我爱你！')
#     i += 1
# print('我已经说完啦~')

# 需求6：死循环
# while True:
#     print('只要不断电，爱你到永远！')


# while循环嵌套
"""
while 条件表达式1:
    满足条件的循环体...
    while 条件表达是2:
        满足条件的循环体...
"""
# 需求7：打印九九乘法表
# 方法一：while
# i = 1
# while i <= 9:
#     j = 1
#     while j <= i:
#         print(f'{j}x{i}={j*i}', end='\t')
#         j += 1
#     print()
#     i += 1
# 方法二：for
# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print(f'{j}x{i}={j*i}', end='\t')
#     print()

# 需求8：打印三角形
# i = 1
# while i <= 5:
#     j = 1
#     while j <= i:
#         print('*', end='  ')
#         j += 1
#     print()
#     i += 1

# 需求8：打印三角形 1 3 5 7 9
# 分析：i为行，j为列。j = 2 * i - 1
# 方法一：while循环
# i = 1
# while i <= 5:
#     j = 1
#     while j <= 2 * i - 1:
#         print('*', end='')
#         j += 1
#     print()
#     i += 1
# for循环：
# for i in range(1, 6):
#     for j in range(1, 2 * i - 1):
#         print('*', end='')
#     print()

# 方法二：if判断--列
# i = 1
# while i <= 9:
#     a = 1
#     while a <= i:
#         if i % 2 == 1:
#             print('*', end=' ')
#         a += 1
#     if i % 2 == 1:
#         print()
#     i += 1

# 方法三：累加2 --列
# i = 1
# while i <= 9:
#     a = 1
#     while a <= i:
#         print('*', end=' ')
#         a += 1
#     print()
#     i += 2

# 需求9：打印正方形
# i = 1
# while i <= 5:
#     j = 1
#     while j <= 5:
#         print('*', end='  ')
#         j += 1
#     print()
#     i += 1

# 需求10：找出任意一个正整数的约数及其总个数。
# num = int(input('输入一个正整数以查找其约数: '))
# i = 1
# result = 0
# print(f'{num}的约数为:')
# while i <= num:
#     if num % i == 0:
#         print(i, end=' ')
#         result += 1
#     i += 1
# print(f'总个数为: {result}')
# if result == 2:
#     print(f'{num} 是一个质数')
# else:
#     print(f'{num} 是一个合数')


