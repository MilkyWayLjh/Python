"""
一.python的smtplib模块提供了一种很方便途径来发送电子邮件,它对邮件协议(smtp)协议进行了封装
smtplib模块提供的方法介绍:

1.SMTP_SSL(url,port)
 url:邮箱运营商的服务器地址
 port:服务器端口号

2.login(user,password)
 user:登录邮箱账号
 password:登录邮箱的密码

3.sendmail(from_addr,to_addr,msg)
 from_addr:邮件发送者
 to_addr:字符串列表的,邮箱接收者地址
 msg:发送消息,必须是一个文本对象(使用msg.as_string()转为文本对象)
4.quit()
 关闭邮件服务

二.MIMEText模块用来编写邮件的正文
from email.mime.text import  MIMEText

三.Header模块用来编写邮件的主题
from email.header import Header
"""


import smtplib
#smtp是一个邮件的传输协议它是来控制邮件发送的
from email.mime.text import  MIMEText #用来发送正文的
from email.header import Header #发送邮件标题的

#定义发送邮箱的服务器
url='smtp.qq.com'#qq邮箱的服务器地址 例如新浪邮箱：smtp.sina.com

#定义发送邮箱的帐号及密码
user=""#发送者
password=''#短信的生成的授权码

#收件者
receiver="479270940@qq.com"
#定义多个收件人：receiver=['7766@qq.com','494494@qq.com']

#定义发送的主题(标题)
subject='我们在学习自动发送邮件功能'

#定义发送内容（正文）
msg=MIMEText("这是我们的第一个自动邮件")
print("msg:",msg)



# # #定义发送的标题并且指了编码的格式
# msg['subject']=Header(subject,'utf-8')
# msg["xx"]='ooooo'
# print("msg:",msg)
# #连接发送邮件
# #
# #
#
# smtp=smtplib.SMTP_SSL(url)#连接发送都邮件服务器的，端口号
# #注意****使用SMTP协议时需要保证运行电脑的设备名称中不能有中文
# smtp.login(user,password)#用来登录
# print("aa:",type(msg))
# #由谁发送给谁
# print(type(msg.as_string()))
# smtp.sendmail(user,receiver,msg.as_string())#as_string 转换为字符串 不截尾部空格(防止尾部空格)
#
# smtp.quit()#用于结束我们SMTP的会话

