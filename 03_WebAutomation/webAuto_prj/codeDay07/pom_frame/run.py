"""
该文件是专用于测试用例运行的文件
该文件是直接放置在项目名称目录下
"""
import unittest

if __name__ == '__main__':
    # 生成discover对象--指定某行某个目录中的文件
    discover = unittest.defaultTestLoader.discover('case', pattern='*case.py')
    # 运行
    runner = unittest.TextTestRunner()
    runner.run(discover)
