import unittest
from HTMLTestRunnerPlugins import HTMLTestRunner
from datetime import datetime
from os import path
import os
from common.send_mail import SendMail

if __name__ == '__main__':
    # 生成报告的名称
    report_name = datetime.now().strftime('%Y_%m_%d %H_%M_%S') + '_ecshop_test_report.html'
    # 要指定报告生成的路径
    report_path = path.join(path.dirname(__file__), 'report', report_name)
    # print(report_path)

    # 运行用例
    # 生成一个套件
    discover = unittest.defaultTestLoader.discover('case', pattern='*case.py')
    # 用HTMLTestRunner来运行套件
    with open(report_path, 'wb') as f:
        runner = HTMLTestRunner(
            stream=f,
            verbosity=2,
            title='ecshop测试报告',
            description='用例通过性验证',
            tester='Group4'
        )
        # runner调用run方法
        runner.run(discover)

    # 指定选取最新的测试报告以邮件的形式发送
    report_dir = path.join(path.dirname(__file__), 'report')
    report_file = path.join(report_dir, os.listdir(report_dir)[-1])
    send_mail = SendMail(report_file=report_file)
    send_mail.common_send_mail()


