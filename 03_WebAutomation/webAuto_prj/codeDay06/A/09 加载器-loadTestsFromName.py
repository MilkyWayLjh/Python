import unittest

# 创建加载器
loader = unittest.TestLoader()

# loader.loadTestsFromName()   通过测试模块名|类名|方法名加载
# TODO 通过模块名加载
"""
suite1 = loader.loadTestsFromName('case.demo1_testcase')
suite2 = loader.loadTestsFromName('case.demo2_testcase')
suite1.addTest(suite2)
"""
# TODO 通过类名加载
suite1 = loader.loadTestsFromName('case.demo1_testcase.Demo1TestCase')

# TODO 通过方法名加载
suite2 = loader.loadTestsFromName('case.demo2_testcase.Demo2TestCase.test_a')
suite1.addTest(suite2)

# 执行
runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite1)
