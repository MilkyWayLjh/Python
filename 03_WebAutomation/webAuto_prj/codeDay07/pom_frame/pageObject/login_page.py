"""
需要将页面的每个对象,封闭成独立的代码块
比如要将输入框,点击按纽,复选框都进行要封装
要进行封装就需要使用Base层相关的行为

"""
from codeDay06.pom_frame.common.base import Base, sleep


class LoginPage(Base):
    def login_page_open_url(self, url):
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


if __name__ == '__main__':
    login = LoginPage()
    login.login_page_open_url('http://127.0.0.1:8080/ecshop/user.php')

    login.login_page_input_username(('name', 'username'), 'Zeus')
    sleep(1)
    login.login_page_input_password(('name', 'password'), '123456')
    sleep(1)
    login.login_page_click_checkbox(('name', 'remember'))
    sleep(1)
    login.login_page_click_login(('name', 'submit'))

    login.login_page_close(2)


