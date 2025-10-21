# 没有break的情况
# i = 1
# while i <= 3:
#     print(i)
#     i += 1
# else:
#     print('else执行了')

# break终止结束循环
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

# continue跳出本次循环，继续下一次循环
# i = 1
# while i <= 3:
#     if i == 2:
#         i += 1
#         continue
#     print(i)
#     i += 1
# else:
#     print('else执行')

# 需求4：你女朋友要求你是说100遍 “我爱你！”，但是说到60遍就不想听了
# i = 1
# while i <= 100:
#     print(f'第{i}遍我爱你！')
#     if i == 60:
#         break
#     i += 1
# print('我已经说完啦~')

# 需求5：你女朋友要求你是说100遍“我爱你！”，但是觉得第44遍不吉利，要求跳过44遍。
i = 1
while i <= 100:
    if i == 44:
        print('这一遍我不说哦~')
        i += 1
        continue
    print(f'第{i}遍我爱你！')
    i += 1
print('我已经说完啦~')
