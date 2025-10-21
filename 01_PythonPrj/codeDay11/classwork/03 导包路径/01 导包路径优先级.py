"""
python自带包模块：打印出是一个字典{}, 有(built-in)的就是内置模块
    内置包模块
    标准包模块

[
'脚本所在的目录（当前目录）',
'python的标准库（包|模块）',
'第三方库（包|模块）'
]

1. 第一级别:   python内置包模块
   import sys
   print(sys.modules)    # built-in 内置模块
2. 第二级别: `sys.path`列表
   - 当前脚本所在的目录
   - 系统标准模块包目录
   - 第三方包模块目录

目的: 我们在自定义模块或者包的时候,不要和系统的内置或者系统的标准模块包,名字相同
"""

import sys
from pprint import pprint

pprint(sys.modules)


# import random
# print(random.randint(1, 999999))


pprint(sys.path)

