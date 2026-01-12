"""
unittest生成自动化测试报告的步骤
1.单独新建一个运行文件--run.py
2.导入HTMLTestRunner模块
    from HTMLTestRunnerPlugins import HTMLTestRunner
3.导入unittest
    import unittest
3.为生成的测试报告定义一个名字
    由于HTMLTestRunner并不是直接生成报告,而是对一个存在的文件写入报告内容,所以:
    (1)要保证报告名字的惟一性,最好使用时间对报告命名
       例如:report_name =time.strftime("%Y_%m_%d_%H_%M_%S")
    (2)报告的类型是一个html格式的报告,所以还要指定报告的完整名称及路径(生成在指定的路径当中,例如在reports里面)
      例如:E:\20220825软件测试精英班\11.web自动化\ecshop\reports\2022_12_01_12_05_59_result.html
4.执行用例
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
import os
import time
from Common.send_mail import Send_Mail
if __name__ == '__main__':
    #定义一个生成测试报告名字
    """
    1.生成报告的名字不能写成固定名
        如何保证每次运行时生成报告的名字都是唯一的名字呢?
            用时间来对文件命名可以达到名字的唯一性
    
    """
    # print(time.strftime("%Y_%m_%d_%H_%M_%S",time.localtime(time.time())))
    #生成报告的名称
    report_name =time.strftime("%Y_%m_%d_%H_%M_%S")+"_result.html"
    #要指定报告生成的路径
    current_dir = path.dirname(__file__)
    report_dir = path.join(current_dir, 'reports')
    report_file_name = path.join(report_dir, report_name)
    print(report_file_name)

    """
    2.运行用例
        (1)用unittest.defaultTestLoader来生成测试套件
        (2)用HTMLTestRunner来运行用例
    
    """
    #生成一个套件
    discover = unittest.defaultTestLoader.discover('./Case', pattern='test*.py')
    #用HTMLTestRunner来运行套件

    with open(report_file_name,'wb') as file:  #创建一个.html格式的报告文件

        #加.html文件引入到HTMLTestRunner中,并定义相关的属性,由此可以生成一个运行对象
        runner = HTMLTestRunner(stream=file,title='ecshop登录测试报告',description='登录的正确性验证',tester='qlc')

        #runner调用run方法
        runner.run(discover)
    """3.指定选取最新的测试报告以邮件的形式发送"""
    report_flie=path.join(report_dir,os.listdir(report_dir)[-1])

    send = Send_Mail(report_file=report_flie)
    send.common_send_mail()



