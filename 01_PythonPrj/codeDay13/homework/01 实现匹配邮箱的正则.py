# 实现匹配邮箱的正则
import re


# reg = '^[A-Za-z0-9_-]+@[A-Za-z0-9_-]+(\.[A-Za-z0-9_-]+)+$'
reg = '^\w{3,20}@[A-Za-z0-9]+(\.[A-Za-z]{2,5}){1,3}$'
email = input('>>>输入邮箱：')
if re.search(reg, email):
    print('邮箱格式正确!')
else:
    print('邮箱格式错误!')
