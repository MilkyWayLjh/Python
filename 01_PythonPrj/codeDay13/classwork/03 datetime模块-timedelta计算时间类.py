"""
timedelta(时间单位=1)
"""
# datetime模块下的timedelta类
# 主要做日期的计算
from datetime import datetime, timedelta

datetime_obj = datetime.today()
timedelta_obj = timedelta(weeks=1)

# 7天之前的时间
day7_ago = datetime_obj - timedelta_obj
print(day7_ago)

# 7天之后的时间
day7_after = datetime_obj + timedelta_obj
print(day7_after)


