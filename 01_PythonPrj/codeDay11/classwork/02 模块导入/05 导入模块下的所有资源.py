"""
# 导入模块下的所有资源
from 模块名 import *
"""

from module01 import *

print(name)
fn()
print(A())  # 因为 module1中__all__没有指定Demo，所以没有被导入

