from crm.base.base import *


class Login(Base):
    def login(self):
        # 打开前台登录页
        self.base_open_url('http://172.16.20.203:8080/crm/')
        # 输入用户名
        self.base_send_keys(('name', 'userNum'), 'admin')
        # 输入密码
        self.base_send_keys(('name', 'userPw'), '123456')
        # 点击登录按钮
        self.base_click(('id', 'in1'))


if __name__ == '__main__':
    login = Login()
    login.login()

    login.quit(2)


