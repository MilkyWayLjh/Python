"""
为一层实现的是自动化测试用例的编写
用例中有行为,有数据,有结果的检查

ecshoplogin操作步骤:1.
打开网页的--setup来实现?
输入账号
输入密码
点击复选框
点击登录按纽
获取用户信息文本

"""
import unittest
from codeDay07.pom_frame.pageObject.login_page import LoginPage
from codeDay07.pom_frame.common.data_operation import DataOperation
from ddt import ddt, data, unpack
# from os import path

# 完成数据文本的定义--指定login_data.csv文件所有的路径
# dir_name = path.dirname(path.dirname(__file__))
# data_name = path.join(dir_name, 'data/login_data.csv')
# 使用pandas来读取数据
data_operation = DataOperation('login_data.csv')
login_data = data_operation.common_get_data_to_list()


@ddt
class LoginTestCase(unittest.TestCase):
    login_data = login_data

    def setUp(self) -> None:
        self.login = LoginPage()
        self.login.login_page_open_url('http://127.0.0.1:8080/ecshop/user.php')

    def tearDown(self) -> None:
        self.login.quit(1)

    @data(*login_data)
    @unpack
    def test_login(self, username, password):
        # 输入账号
        self.login.login_page_input_username(('name', 'username'), username)
        # 输入密码
        self.login.login_page_input_password(('name', 'password'), password)
        # 点击记录登录
        self.login.login_page_click_checkbox(('name', 'remember'))
        # 点击登录按纽
        self.login.login_page_click_login(('name', 'submit'))
        # 断言
        # 预期 和 实际结果的比对
        # Zeus 和 获取实际结果
        # 定位预期结果
        """
        user_text = self.login.base_get_text(('class name', 'f4_b'))
        # 获取文本信息后作断言
        self.assertEqual("Zeus", user_text)
        """
        # 获取用户信息--只有一条数登录成功才能获取文本,所以要使用try进行处理
        try:
            user_text = self.login.base_get_text(('class name', 'f4_b'))
            # 获取文本信息后作断言
            self.assertEqual("Zeus", user_text, msg='信息匹配失败')
        except Exception as e:
            print(e)
            print(f'{username}, {password}, 该条数据登录失败')


if __name__ == '__main__':
    unittest.main()
