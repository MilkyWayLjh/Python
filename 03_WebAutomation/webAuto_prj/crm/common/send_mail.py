from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib


class SendMail:
    def __init__(self, report_file, sender='1712240212@qq.com', receiver='1712240212@qq.com', subject='ecshop自动化测试报告'):
        """
        该方法用来做初始的设置
        :param report_file: 要发送的报告名称路径
        :return:
        """
        """1.初始化发送人和接收人"""
        self.sender = sender
        self.receiver = receiver

        """2.编辑要发送的邮件内容"""
        with open(report_file, 'rb') as file:
            self.mail_body = file.read()
            # print(self.mail_body)

        """3.定义发送人,接收人,邮件主题"""
        self.msg = MIMEMultipart()
        self.msg["from"] = sender
        self.msg["to"] = receiver
        self.msg["subject"] = subject

        """4.将要发送的邮件信息以附件的形式定义发送"""
        self.att = MIMEText(self.mail_body, "base64", "utf-8")
        self.att["Content-Type"] = "application/octet-stream"
        self.att["Content-Disposition"] = 'attachment; filename="test_report.html"'
        self.msg.attach(self.att)

    def common_send_mail(self, smtp_server="smtp.qq.com"):
        """发送邮件的方法"""
        smtp = smtplib.SMTP_SSL(smtp_server)
        smtp.login(self.sender, 'ndjyxjzddhfjcjdb')   # 邮箱授权码
        smtp.sendmail(self.sender, self.receiver, self.msg.as_string())
        smtp.quit()

