# 1 打印实心矩形
# n = int(input("输入行列: "))
# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         print("*", end=" ")
#     print()

# 2 打印空心矩形
# n = int(input("输入行列: "))
# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         if i == 1 or j == 1 or i == n or j == n:
#             print("*", end="  ")
#         else:
#             print(" ", end="  ")
#     print()

# 3 打印三角形  列数：1 3 5 7 9 ...
# # 分析：i为行，j为列。j = 2 * i - 1   在range()中的第2个参数就是 2 * i - 1 + 1 = 2 * i
# n = int(input("输入行: "))
# for i in range(1, n + 1):
#     for j in range(1, 2 * i):
#         print('*', end='')
#     print()

# 4 打印左下实心三角形
# n = int(input("输入行列: "))
# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         print("*", end=" ")
#     print()

# 5 打印左下空心三角形
# n = int(input("输入行列: "))
# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         if i == n or i == j or j == 1:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

# 6 打印右下角实心三角形
# n = int(input("输入行列: "))
# for i in range(n + 1):
#     for j in range(0, (n + 1) - i):
#         print(" ", end=" ")
#     for k in range((n + 1) - i, n + 1):
#         print("*", end=" ")
#     print("")

# 7 打印右下角空心三角形
# n = int(input("输入行列: "))
# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         if i == n or j == n or (i + j - 1 == n):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

# 8 打印右上角实心三角形
# n = int(input("输入行列: "))
# for i in range(n):
#     for j in range(0, i):
#         print(" ", end=" ")
#     for k in range(i, n):
#         print("*", end=" ")
#     print("")

# 9 打印右上角空心三角形
# n = int(input("输入行列: "))
# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         if i == 1 or j == n or i == j:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

# 10 打印左上角实心三角形
# n = int(input("输入行列: "))
# for i in range(0, n + 1):
#     for j in range(0, n - i):
#         print("*", end=" ")
#     print()

# 11 打印左上角空心三角形
# n = int(input("输入行列: "))
# for i in range(0, n + 1):
#     for j in range(0, n - i):
#         if (i == 0) or (j == 0) or i + j + 1 == n:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

# 12 打印正等边三角形
# n = int(input("输入行列: "))
# for i in range(n + 1):
#     for j in range(0, (n + 1) - i):
#         print(end=" ")
#     for k in range((n + 1) - i, (n + 1)):
#         print("*", end=" ")
#
#     print("")

# 13 打印倒等边三角形
# n = int(input("输入行列: "))
# for i in range(n):
#     for j in range(0, i):
#         print(end=" ")
#     for k in range(i, n):
#         print("*", end=" ")
#
#     print("")

# 14 打印正等边空心三角形
n = int(input("输入行列: "))
for i in range(1, n * 2):
    if i == n:
        print("*")
        break
    else:
        print(" ", end="")
for j in range(n - 1, 1, -1):
    for i in range(1, n * 2):
        if i == j:
            print("*", end="")
        elif i == n * 2 - j:
            print("*")
            break
        else:
            print(" ", end="")
for i in range(1, n * 2):
    if i % 2 != 0:
        print("*", end="")
    else:
        print(" ", end="")

