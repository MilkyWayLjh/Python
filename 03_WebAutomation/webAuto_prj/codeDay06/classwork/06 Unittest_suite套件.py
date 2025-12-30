"""
生成套件语法
1.套件对象 = unittest.TestSuite()
2.套件对象.addTest(模块名.类名("方法名"))

生成运行套件对象
1.运行对象 = unittest.TextTestRunner()
2.运行对象.run(套件对象)

运行结果说明:
1.运行结果中"."表示一条成功的用例
2.运行结果中"E"表示一条用例异常
3.F表示一条用例断言失败
4.S表示一条用例执行跳过
5.suite.addTest()可以改变用例默认的执行顺序，先添加，先执行

总结:使用suite与TestRunner来运行用例与unittest运行的区别
1.unittest.main()无法改变用例的执行顺序
2.unittest.main()它是将所有以test开对的方法进行执行,不能达到指定执行的效果
3.unittest.main()默认情况下不能跨文件执行用例

"""
import unittest


class Demo1TestCase(unittest.TestCase):
    def test_1(self):
        print('test1')

    def test_2(self):
        print('test2')


class Demo2TestCase(unittest.TestCase):
    def test_a(self):
        print('testa')

    def test_b(self):
        print('testb')


if __name__ == '__main__':
    # 创建一个测试套件对象
    suite = unittest.TestSuite()

    # suite.addTest：单个收集测试用例方法
    """
    # 在unittest框架中以test开头的方法就是一条用例
    suite.addTest(Demo1TestCase('test_2'))
    suite.addTest(Demo1TestCase('test_1'))
    suite.addTest(Demo2TestCase('test_b'))
    suite.addTest(Demo2TestCase('test_a'))
    """

    # suite.addTests：批量收集测试用例方法
    tests = [
        Demo1TestCase('test_2'),
        Demo1TestCase('test_1'),
        Demo2TestCase('test_b'),
        Demo2TestCase('test_a')
    ]

    suite.addTests(tests)

    # 创建执行器，生成一个运行对象
    # 执行器只会执行套件收集的用例
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)

    # unittest.TextTestRunner().run(suite)

