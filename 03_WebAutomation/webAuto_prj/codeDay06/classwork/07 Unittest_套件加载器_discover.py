"""
unittest.defaultTestLoader.discover(start_dir=dir,pattern='*.py')
start_dir: 查找运行文件目录
pattern: 指定格式的.py运行,
    test*.py表示将当前目录下所有test开头.py文件进行执行
    *.py表示对当前目录下所有的.py进行执行

defaultTestLoader = TestLoader()
defaultTestLoader是TestLoader类的实例化对象
"""
import unittest

if __name__ == '__main__':
    # 形成更大的套件，自定义路径和匹配项
    discover = unittest.defaultTestLoader.discover('case', pattern='*.py')
    # 运行套件
    runner = unittest.TextTestRunner()
    runner.run(discover)


"""
# 创建加载器
loader = unittest.TestLoader()

# loader.discover(start_dir, pattern='*_testcase')   通过目录路径加载
# 通过目录路径加载
suite = loader.discover('case', pattern='*_testcase.py')

# 执行
runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)
"""
