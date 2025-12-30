import unittest
from case import demo1_testcase

# 创建加载器
loader = unittest.TestLoader()

# loader.loadTestsFromModule()                     通过测试模块
# TODO 通过模块加载
suite = loader.loadTestsFromModule(demo1_testcase)

# 执行
runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)
