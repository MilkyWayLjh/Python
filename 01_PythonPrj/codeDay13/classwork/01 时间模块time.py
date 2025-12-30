"""
time模块
    time.time()  掌握  生成时间戳
单位:秒
    从1970年1月1日0时0分0秒到当前的秒数

    time.sleep()  掌握  程序休眠
"""
import time     # 内置模块 第一优先级 [掌握]

print(time.time())
time.sleep(1)

# 1 time.time()     # 返回一个距19700101000000的秒数，是浮点数。
print(time.time())

# 2 time.gmtime([seconds])	# 将秒数转化为年月日时分秒，以UTC时间为标准。返回struct_time对象
print(time.gmtime(100))      # tm_wday = 3 表示星期四 0 1 2 3 4 5 6
struct_time = time.gmtime()  # 当前的UTC时间   UTC时间和中国时间差8小时
print(struct_time)

# 3 time.localtime([seconds])	将秒数转化为年月日时分秒，以当地时间为标准。返回struct_time对象
struct_time = time.localtime(80)
struct_time1 = time.localtime()
print(struct_time1)

# 4 time.ctime([seconds])	返回年月日时分秒的字符串。
print(time.ctime(100), time.ctime(), type(time.ctime()))

# 5 time.asctime(tuple)     从struct_time返回年月日时分秒字符串。
struct_time2 = time.localtime()
print(time.asctime(struct_time2))

# 6 time.mktime(tuple)	将struct_time转换为秒数。
struct_time3 = time.localtime()
print(time.mktime(struct_time3))

# 7 time.strftime(fmt,t)	按照fmt格式将struct_time显示成字符串。  日期对象转日期字符串
struct_time4 = time.localtime()
print(time.strftime('%Y-%m-%d %H:%M:%S', struct_time4))
# 年份时间格式化
# %y:2位的年 %Y:4位的年 %m:月,%d:日
# %H:时 %M:分 %S:秒

# 8 time.strptime(str,fmt)	将年月日时分秒的字符串按照fmt解析成struct_time结构。日期字符串转时间对象
time_str = time.strftime('%Y-%m-%d %H:%M:%S', struct_time4)
print(time.strptime(time_str, '%Y-%m-%d %H:%M:%S'))
