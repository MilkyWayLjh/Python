from base.base import *


class CommonLogin(Base):
    # 用户前台登录
    def common_user_login(self, username, password):
        # 打开前台登录页
        self.base_open_url('http://127.0.0.1:8080/ecshop/user.php')
        # 输入用户名
        self.base_send_keys(('name', 'username'), username)
        # 输入密码
        self.base_send_keys(('name', 'password'), password)
        # 点击登录按钮
        self.base_click(('name', 'submit'))

    # 管理员后台登录
    def common_admin_login(self, username, password):
        # 打开后台登录页
        self.base_open_url('http://localhost:8080/ecshop/admin/')
        # x掉弹窗
        self.base_click((By.CSS_SELECTOR, '.panel-cross span'))
        # 点击ecshop登录方式
        self.base_click((By.ID, 'cloudLogin'))
        # 输入用户名
        self.base_send_keys(('name', 'username'), username)
        # 输入密码
        self.base_send_keys(('name', 'password'), password)
        # 点击登录按钮
        self.base_click(('class name', 'btn-a'))


if __name__ == '__main__':
    common_login = CommonLogin()
    # common_login.common_user_login('Zeus', 123456)
    common_login.common_admin_login('admin', 'admin123456')

    common_login.quit(2)
