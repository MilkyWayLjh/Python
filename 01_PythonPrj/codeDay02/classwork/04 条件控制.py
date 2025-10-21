# age1 = input('your age is: ')
# age2 = input('his age is: ')

# 单分支语句
# if age1 == age2:
#     print('you are same!')

# 双分支语句
# if age1 == age2:
#     print('you are old!')
# else:
#     print('you are not same!')

"""
需求：
1.定义两个变量，分别记录年龄和是否携带身份证。
2.如果满18岁，并且带有身份证，运行进入网吧上网。
3.如果不满足条件，提示 “我们网吧是正规的，可以去隔壁的黑网吧！”
"""
"""
age = int(input('input your age: '))
id_card = int(input('input your id_card status(1/0): '))
if age >= 18 and id_card:
    print('上网happy吧!')
else:
    print('我们网吧是正规的，可以去隔壁的黑网吧!')
"""

# 多分支语句
"""
需求：
1.输入一个成绩。
2.判断并且提示成绩的等级（A、B、C、D、E）。
"""
score = int(input('input your score: '))
# if score >= 90 and score <= 100:
if 90 <= score <= 100:
    print('A')
elif score >= 80:
    print('B')
elif score >= 70:
    print('C')
elif score >= 60:
    print('D')
# elif score < 60 and score >= 0:
elif 0 <= score < 60:
    print('E')
else:
    print('你的成绩无效！')
