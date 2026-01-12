"""
Untitest简介：
    unittest是Python自带的一个单元测试框架，unittest又被称为PyUnit，是由Java的JUnit衍生而来，基本结构是类似的。
对于单元测试，需要设置预先条件，对比预期结果和实际结果。

为什么要使用unittest：
    当我们写的自动化用例越来越多时，我们就需要考虑用例编写的规范与组织，以便于后期的维护，而unittest正是这样一款工具。

1.先导入unittest模块
2.编写一个类,此类必须继承unittest.TestCase-->表示在使用unittest框架
3.unittest框架中方法的命名要求
    类中的方法必须是test*开头

"""
import unittest


class MyTestCase(unittest.TestCase):
    def test02(self):
        print('test02')

    def test01(self):
        print('test01')

    def testA(self):
        print('testA')

    def testa(self):
        print('testa')

    # 不以test开头，不运行，没有实例化
    def mytest(self):
        print('mytest')
