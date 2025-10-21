"""
求解1-100中能被3整除的所有数字的和
"""
i = 1
Sum = 0
while i <= 100:
    if i % 3 == 0:
        print(i, end=' ')
        Sum += i
    i += 1
print(f'\n它们的和为: {Sum}')

