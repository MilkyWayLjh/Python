import unittest
from selenium.webdriver.common.by import By
from pageObject.login_page import LoginPage
from common.data_operation import DataOperation
from ddt import ddt, data, unpack

# 使用pandas来读取数据
data_operation = DataOperation('login_data.csv')
login_data = data_operation.common_get_data_to_list()


@ddt
class LoginTestCase(unittest.TestCase):
    login_data = login_data

    @classmethod
    def setUpClass(cls) -> None:
        cls.login = LoginPage()
        cls.login.login_page_open_url('http://127.0.0.1:8080/ecshop/user.php')

    def setUp(self) -> None:
        self.login.index_login()

    # 不记住信息进行登录
    @data(*login_data)
    @unpack
    def test_login_01(self, username, password):
        # 输入账号
        self.login.login_page_input_username(('name', 'username'), username)
        # 输入密码
        self.login.login_page_input_password(('name', 'password'), password)
        # 点击登录按纽
        self.login.login_page_click_login(('name', 'submit'))
        # 断言
        try:
            user_text = self.login.base_get_text(('class name', 'f4_b'))
            self.assertEqual(username, user_text, msg='信息匹配失败')
        except Exception as e:
            print(e)
            print(f'{username}, {password}, 该条数据登录失败')

    # 记住信息进行登录
    @data(*login_data)
    @unpack
    def test_login_02(self, username, password):
        # self.login.driver.implicitly_wait(5)
        # 输入账号
        self.login.login_page_input_username(('name', 'username'), username)
        # 输入密码
        self.login.login_page_input_password(('name', 'password'), password)
        # 点击记住登录
        self.login.login_page_click_checkbox(('name', 'remember'))
        # 点击登录按纽
        self.login.login_page_click_login(('name', 'submit'))
        # 断言
        try:
            user_text = self.login.base_get_text(('class name', 'f4_b'))
            self.assertEqual(username, user_text, msg='信息匹配失败')
        except Exception as e:
            print(e)
            print(f'{username}, {password}, 该条数据登录失败')

    def tearDown(self) -> None:
        if not self.login.base_find_element((By.LINK_TEXT, '免费注册')):
            self.login.index_logout()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.login.quit(1)


if __name__ == '__main__':
    unittest.main()


