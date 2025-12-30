"""
fixture:夹具  （方法夹具）
    1.setUp和tearDown命名必须固定
    2.setUp称为前夹具,tearDown为后夹具
    3.setUp和tearDown可以不需要同时存在
    4.setUp和tearDown会包裹类中每一个以test开头的方法
"""
import unittest


class MyTestCase(unittest.TestCase):
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
    unittest.main()     # 它是运行当前文件中所有以test开头的方法


