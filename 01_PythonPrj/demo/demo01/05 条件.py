"""
age = int(input("请输入你家修勾的年龄: "))
if age <= 0:
    print("你是在逗我吧!")
elif age == 1:
    print("相当于 14 岁的人。")
elif age == 2:
    print("相当于 22 岁的人。")
else:
    human = 22 + (age - 2) * 5
    print("对应人类年龄: ", human)

# 退出提示
input("点击 enter 键退出 =>")
"""

# if条件，代码冗余单一
# sports = input('你喜欢篮球、足球还是乒乓球(b/f/p), 或者都不喜欢(n)？ => ')
# if sports == 'b':
#     print('我也喜欢篮球！')
# elif sports == 'f':
#     print('我也喜欢足球！')
# elif sports == 'p':
#     print('我也喜欢乒乓球！')
# else:
#     print('那你喜欢啥啊？')

# 优化代码（优雅）
sports = input('你喜欢篮球、足球还是乒乓球(b/f/p), 或者都不喜欢(n)？ => ')
ball = {
    'b': '我也喜欢篮球！',
    'f': '我也喜欢足球！',
    'p': '我也喜欢乒乓球！'
}
if sports in ball.keys():
    print(ball[sports])
# elif sports not in ball.keys():
else:
    print('那你喜欢啥啊？')
