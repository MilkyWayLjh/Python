# 输入: var_name = input()
# name = input('input your name: ')
# age = input('input your age: ')
# address = input('input your address: ')
# print('你的姓名为：' + name, '你的年龄为：' + age, '你的地址是：' + address)

a, b = input('输入姓名和成绩(以空格隔开)：').split()
# a, b = input('输入姓名和成绩(以逗号隔开)：').split(',')
print(a + ': ' + b)
"""
理解：
输入name, score
'name score'.split() => list => ['name', 'score']
a, b = ['name', 'score']       列表拆包
"""

m = input('请输入第一个数字：')
n = input('请输入第二个数字：')
print(m + n)    # input输入的是字符串，所以相加结果是字符串拼接
print(int(m) + int(n))  # 转换为数字相加
