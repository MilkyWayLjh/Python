"""
2.网吧年龄验证
需求：
1. 定义两个变量，分别记录年龄和是否携带身份证
2. 如果满18岁，并且带有身份证，运行进入网吧上网。
"""

age = int(input('input your age: '))
id_card = int(input('input your id_card status(1/0): '))
if age >= 18 and id_card:
    print('上网happy吧!')
else:
    print('我们网吧是正规的，可以去隔壁的黑网吧!')
