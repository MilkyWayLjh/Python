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
    # 创建加载器
    loader = unittest.TestLoader()

    # TODO loader.loadTestsFromTestCase()       通过测试类加载
    # 所有加载器方法返回的都是测试套件对象
    suite1 = loader.loadTestsFromTestCase(Demo1TestCase)
    suite2 = loader.loadTestsFromTestCase(Demo2TestCase)

    suite = unittest.TestSuite()
    # 单个
    """
    suite.addTest(suite1)
    suite.addTest(suite2)
    """

    # 批量
    suite.addTests([suite1, suite2])

    # 执行
    # 执行器
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
