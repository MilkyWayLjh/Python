"""
跳过用例执行的使用场景:
    当环境不稳定，或者某些页面暂时无法测试时可以选择将相应的测试用例跳过执行
注意:
    unittest.skip执行时间是早于所有以test开头的方法，也是早于setup
    所以skip如果有使用变量,必须要让变量在运行此类之前先生成
"""
import unittest

gender = input('性别【男|女】：')


class DemoTestCase(unittest.TestCase):
    @unittest.skip(reason='无条件跳过')
    def test01(self):
        print('test01')

    # 条件成立跳过
    @unittest.skipIf(gender == '男', reason='男生跳过测试')
    def test02(self):
        print('test02')

    # 条件不成立跳过
    @unittest.skipUnless(gender == '男', reason='不是男跳过测试')
    def test03(self):
        print('test03')

    @unittest.expectedFailure
    def test04(self):
        self.assertEqual(1, 1, msg='断言1等于1')

    @unittest.expectedFailure
    def test05(self):
        self.assertEqual(1, 2, msg='断言1等于2')


if __name__ == '__main__':
    unittest.main(verbosity=2)
