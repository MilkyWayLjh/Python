"""
# 导入单个指定模块
import 模块名
说明：模块名就是没有后缀的文件名字
导入模块的目的：导入模块之后可以使用模块中的资源
资源：变量，函数，类
"""
import module01

print(module01.name)
module01.fn()

print(module01.module02.name)
print(module01.A())
