import os, time, random

print(os.my_os)     # AttributeError: module 'os' has no attribute 'my_os'  报错，说明属于第一级别

print(time.my_time)     # AttributeError: module 'time' has no attribute 'my_time'  报错，说明属于第一级别

print(random.my_random)     # this is myrandom  没报错，说明属于第二级别。当前目录中的random优先级比系统标准模块包目录高一级


