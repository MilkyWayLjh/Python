"""
from 包[.包.n] import *
说明：
    上面的import *需要在包的init文件中指定可以导入的模块。
"""
from package01 import *
from package01.module01 import *

print(module01.name)
module01.fn()
module01.A().prt()
print(module01.A())

fn()
# module01.fn()

# print(module02.name)
