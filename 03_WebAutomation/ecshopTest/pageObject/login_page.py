from base.base import Base, sleep
from pageObject.index_page import IndexPage


class LoginPage(IndexPage):
    def login_page_open_url(self, url='http://127.0.0.1:8080/ecshop/user.php'):
        self.base_open_url(url)

    # 用户名
    def login_page_input_username(self, locator, content):
        self.base_send_keys(locator, content)

    # 密码
    def login_page_input_password(self, locator, content):
        self.base_send_keys(locator, content)

    # 保存登录信息
    def login_page_click_checkbox(self, locator):
        self.base_click(locator)

    # 点击登录
    def login_page_click_login(self, locator):
        self.base_click(locator)

    # 关闭当前窗口
    def login_page_close(self, seconds=0):
        # super().close(seconds)
        self.close(seconds)

    # def logout(self):
    #     super().index_logout()


if __name__ == '__main__':
    login = LoginPage()
    login.login_page_open_url()

    login.login_page_input_username(('name', 'username'), 'Zeus1')
    sleep(1)
    login.login_page_input_password(('name', 'password'), '123456')
    sleep(1)
    login.login_page_click_checkbox(('name', 'remember'))
    sleep(1)
    login.login_page_click_login(('name', 'submit'))

    # login.login_page_close(2)

    # login.super().index_logout()
    # login.logout()
    login.index_logout()


