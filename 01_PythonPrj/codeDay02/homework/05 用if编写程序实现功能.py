"""
5.使用if，编写程序，实现以下功能：
    从键盘获取用户名、密码
    如果用户名和密码都正确（预先设定一个用户名和密码），那么就显示“欢迎进入xxx的世界”，否则提示密码或者用户名错误
"""
username = input('输入用户名: ')
password = input('输入密码: ')
usr = '李四'
pwd = '123'
if username == usr and password == pwd:
    print('欢迎进入我的世界!')
else:
    print('用户名或密码错误!')
