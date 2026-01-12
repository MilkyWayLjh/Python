"""
unittest生成自动化测试报告的步骤
1.单独新建一个运行文件--run.py
2.导入unittest
    import unittest
3.导入HTMLTestRunner模块
    from HTMLTestRunnerPlugins import HTMLTestRunner
4.为生成的测试报告定义一个名字
    由于HTMLTestRunner并不是直接生成报告,而是对一个存在的文件写入报告内容,所以:
    (1)要保证报告名字的惟一性,最好使用时间对报告命名
       例如:report_name = datetime.now().strftime('%Y_%m_%d %H_%M_%S') + '_xxx_report.html'
    (2)报告的类型是一个html格式的报告,所以还要指定报告的完整名称及路径(生成在指定的路径当中,例如在reports里面)
      例如:E:\\20220825软件测试精英班\\11.web自动化\\ecshop\\reports\\2022_12_01_12_05_59_result.html
        report_path = path.join(path.dirname(__file__), 'report', report_name)
5.执行用例
    (1)生成测试套件-->使用unittest.defaultTestLoader.discover()
    (2)创建.html格式的报告文件
        with open("测试报告文件路径",'wb') as file
    (3) 将生成的文件对象引入到HTMLTestRunner中来运行测试套件
        [1]生成运行对象
        runner = HTMLTestRunner(stream=file,title='ecshop登录测试报告',description='登录的正确性验证',tester='qlc')
            HTMLTestRunner参数说明:
            stream--> 表示报告内容写入模式
            verbosity=2 -->文件目录等级,一般是默认使用
            title -->报告标题
            description -->报告副标题
            tester --> 测试者
        [2]runner对象调用run方法
            runner.run(discover)

"""
import unittest
from HTMLTestRunnerPlugins import HTMLTestRunner
from os import path
from datetime import datetime

if __name__ == '__main__':
    # 定义一个生成测试报告名字
    """
    1.生成报告的名字不能写成固定名
        如何保证每次运行时生成报告的名字都是唯一的名字呢?
            用时间来对文件命名可以达到名字的唯一性
    """
    # 生成报告的名称
    report_name = datetime.now().strftime('%Y_%m_%d %H_%M_%S') + '_ecshop_report.html'
    # 要指定报告生成的路径
    report_path = path.join(path.dirname(__file__), 'report', report_name)
    # print(report_path)

    """
    2.运行用例
        (1)用unittest.defaultTestLoader来生成测试套件
        (2)用HTMLTestRunner来运行用例
    """
    # 生成一个套件
    discover = unittest.defaultTestLoader.discover('case', pattern='*case.py')
    # 用HTMLTestRunner来运行套件
    with open(report_path, 'wb') as f:
        # stream=sys.stdout, verbosity=2, title=None, description=None, tester=None
        runner = HTMLTestRunner(
            stream=f,   # 写如文件的资源句柄
            verbosity=2,
            title='ecshop登录测试报告',
            description='登录的正确性验证',
            tester='Zeus'
        )
        # runner调用run方法
        runner.run(discover)
