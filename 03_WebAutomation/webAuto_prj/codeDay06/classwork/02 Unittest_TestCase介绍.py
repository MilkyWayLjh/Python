"""
unittest.main()：
    将一个单元测试模块变为可直接运行的测试脚本，
    main()方法使用TestLoader类来搜索 所有包含在该模块中以test命名开头的测试方法，并自动执行他们。
    执行方法的默认顺序是：根据ASCII码的顺序加载测试用例，数字与字母的顺序为：0-9，A-Z，a-z。
                    所以以A开头的测试用例方法会优先执行，以a开头会后执行。

unittest核心的四个概念：
    TestFixture：一般用于准备及清理工作。
    TestCase：通常是使用断言assert方法检查动作和输入的响应，一般是基于TestCase类扩充。
    TestSuite：多个测试的集合。
    TestRunner：测试执行。
"""
import unittest


class MyTestCase(unittest.TestCase):
    # def test_something(self):
    #     self.assertEqual(True, False)

    def test_login(self):
        print('输入账号')
        print('输入密码')
        print('点击登录')

    def test_register(self):
        print('输入新账号')
        print('输入新密码')
        print('确认密码')
        print('新增')

    def mytest(self):
        print('mytest')


if __name__ == '__main__':
    unittest.main()
    # unittest.main(verbosity=2)


