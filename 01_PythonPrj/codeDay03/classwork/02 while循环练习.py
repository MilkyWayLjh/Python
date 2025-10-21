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
# i, result = 1, 0
# while i <= 100:
#     # if i % 2 == 1:    # 奇数
#     if i % 2 == 0:  # 偶数
#         result += i
#     i += 1
# print(result)
# 方法二：
# i, result = 1, 0    # 奇数
# # i, result = 2, 0    # 偶数
# while i <= 100:
#     result += i
#     i += 2
# print(result)

