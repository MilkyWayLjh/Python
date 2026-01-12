"""
fixture:夹具  （类夹具）
    1.一个类只运行类夹具一次,与类中方法的个数无关(setUp与tearDown运行的次数与类中方法个数有关)
    2.类夹具的名称:setUpClass,tearDownClass
    3.类夹具的形参是cls关键字
    4.类夹具需要用到装饰器@classmethod
"""
import unittest


class MyTestCase(unittest.TestCase):
    # 必须使用@classmethod装饰器，所有test运行前执行一次。
    @classmethod
    def setUpClass(cls) -> None:
        print('类的前夹具')

    # 必须使用@classmethod装饰器，所有test运行完后执行一次。
    @classmethod
    def tearDownClass(cls) -> None:
        print('类的后夹具')

    # 前夹具  每个测试方法运行前执行
    def setUp(self) -> None:
        print('打开浏览器')

    # 后夹具  每个测试方法运行完后执行
    def tearDown(self) -> None:
        print('关闭浏览器\n======')

    def test_login(self):
        print('输入账号')
        print('输入密码')
        print('点击登录')

    def test_register(self):
        print('输入新账号')
        print('输入新密码')
        print('确认密码')
        print('新增')


if __name__ == '__main__':
    unittest.main()
