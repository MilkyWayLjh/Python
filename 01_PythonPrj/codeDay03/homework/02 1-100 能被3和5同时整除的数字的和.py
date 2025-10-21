"""
求解1-100 能被3和5同时整除的数字的和
"""
i = 1
Sum = 0
while i <= 100:
    if i % 3 == 0 and i % 5 == 0:
        print(i, end=' ')
        Sum += i
    i += 1
print(f'\n它们的和为: {Sum}')

