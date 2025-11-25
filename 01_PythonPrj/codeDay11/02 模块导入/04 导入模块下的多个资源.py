"""
# 导入模块下的指定资源
from 模块名 import 资源名1 [as 别名], 资源名2, ...
"""
# 导入了module01下的name和fn资源
from module01 import name, fn
from module02 import name as m2_name

print(name)
fn()

print(m2_name)

