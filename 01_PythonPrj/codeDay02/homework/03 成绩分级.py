"""
3.成绩分级
需求：
1. 输入一个成绩。
2. 判断判断并且提示成绩的等级（A、B、C、D、E）。
如果考试分数大于等于90等级为A，如果考试成绩大于等于80等级为B，如果考试成绩大于等于70等级为C，
如果考试成绩大于等于60等级为D，如果考试成绩低于60等级为E。
"""
score = int(input('input your score: '))
# if score >= 90 and score <= 100:
if 90 <= score <= 100:
    print('A')
elif 80 <= score < 90:
    print('B')
elif 70 <= score < 80:
    print('C')
elif 60 <= score < 70:
    print('D')
elif 0 <= score < 60:
    print('E')
else:
    print('你的成绩无效！')
