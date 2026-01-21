import unittest
from selenium.webdriver.common.by import By
from pageObject.register_page import RegisterPage
from common.data_operation import DataOperation
from ddt import ddt, data, unpack

# pandas读取正确的注册数据register_data.csv
data_operation = DataOperation('register_data.csv')
register_data = data_operation.common_get_data_to_list()
# print(register_data)


@ddt
class RegisterTestCase(unittest.TestCase):
    register_data = register_data

    @classmethod
    def setUpClass(cls) -> None:
        cls.register = RegisterPage()
        cls.register.reg_open_url()

    @data(*register_data)
    @unpack
    def test_register(self, username, email, password, password1, qq,
                      work_phone, home_phone, mobile_phone, question_index, answer):
        # 输入用户名
        self.register.reg_username_ipt((By.ID, 'username'), username)
        # 输入email
        self.register.reg_email_ipt((By.ID, 'email'), email)
        # 输入密码
        self.register.reg_password_ipt((By.NAME, 'password'), password)
        # 输入确认密码
        self.register.reg_password1_ipt((By.NAME, 'confirm_password'), password1)
        # 输入QQ
        self.register.reg_qq_ipt((By.NAME, 'extend_field2'), qq)
        # 输入办公电话
        self.register.reg_work_phone_ipt((By.NAME, 'extend_field3'), work_phone)
        # 输入家庭电话
        self.register.reg_home_phone_ipt((By.NAME, 'extend_field4'), home_phone)
        # 输入手机
        self.register.reg_mobile_phone_ipt((By.NAME, 'extend_field5'), mobile_phone)
        # 选择密码提示问题
        self.register.reg_pwd_question_select((By.NAME, 'sel_question'), question_index)
        # 输入密码问题答案
        self.register.reg_pwd_answer_ipt((By.NAME, 'passwd_answer'), answer)
        # 点击接收用户协议  默认是勾选中的，所以不用再勾选
        # self.register.reg_click_agreement((By.NAME, 'agreement'))
        # 第一步断言验证 ---> 密码和确认密码是否相同
        self.assertEqual(password, password1, msg='两次密码不相同')
        # 点击立即注册
        self.register.reg_click_register((By.NAME, 'Submit'))
        # 第二步断言验证 ---> 注册成功后会自动登录，左上角的用户名和注册输入的用户名是否相同
        user_text = self.register.index_username_text()
        self.assertEqual(username, user_text)

    def tearDown(self) -> None:
        # 注册成功后退出登录
        self.register.index_logout()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.register.quit(2)


if __name__ == '__main__':
    unittest.main()
