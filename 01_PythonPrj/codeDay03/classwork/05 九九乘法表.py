# 需求：打印九九乘法表
# 方法一：while
i = 1
while i <= 9:
    j = 1
    while j <= i:
        print(f'{j}x{i}={j*i}', end='\t')
        j += 1
    print()
    i += 1
# 方法二：for
# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print(f'{j}x{i}={j*i}', end='\t')
#     print()
