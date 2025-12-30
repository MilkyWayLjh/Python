"""
datetime模块
    datetime 日期时间类
类的方法: datetime.strptime(datetime_str, fmt)   日期字符串 转 日期对象
对象方法: datetime_obj.strftime(fmt)    日期对象转 日期字符串
"""
from datetime import datetime
import time

# 类方法
# 1 datetime.today()	当前时间，localtime。
datetime_obj = datetime.today()
print(datetime_obj)
print(type(datetime_obj))
print('==' * 20)

# 2 datetime.now()	当前的时间。
datetime_obj1 = datetime.now()
print(datetime_obj1)
print('==' * 20)

# 3 datetime.utcnow()	当前格林时间。
print(datetime.utcnow())
print('==' * 20)

# 4 datetime.fromtimestamp()	将时间戳的转换为时间。
timestamp = time.time()
print(datetime.fromtimestamp(timestamp))
print(type(datetime.fromtimestamp(timestamp)))
print('==' * 20)

# 5 datetime.strptime(str,fmt)
# datetime.strptime(str,fmt)	按照fmt的格式解析字符串生成datetime。 字符串时间->对象时间
datetime_str = '2022-10-1 10:10:10'
datetime_obj2 = datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S')
print(datetime_obj2)
print(type(datetime_obj2))
print('==' * 20)


# 对象方法
# 1 datetime.date()	返回一个date对象。
datetime_obj3 = datetime.now()
date_obj = datetime_obj3.date()
print(date_obj)
print(type(date_obj))
print('==' * 20)

# 2 datetime.time()	返回time对象。
datetime_obj4 = datetime.now()
time_obj = datetime_obj4.time()
print(time_obj)
print(type(time_obj))
print('==' * 20)

# 3 datetime.strftime(fmt)
# datetime.strftime(fmt)	按照fmt的格式生成字符串。  对象时间->字符串时间
datetime_obj5 = datetime.now()
datetime_str1 = datetime_obj5.strftime('%Y-%m-%d %H:%M:%S')
print(datetime_str1)
print(type(datetime_str1))
print('==' * 20)

# 将时间转换为时间戳
dt = time.strptime(datetime_str1, '%Y-%m-%d %H:%M:%S')
print(time.mktime(dt))
