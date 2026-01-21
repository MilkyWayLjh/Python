import unittest
from selenium.webdriver.common.by import By
from pageObject.register_page import RegisterPage, sleep
from common.data_operation import DataOperation
from ddt import ddt, data, unpack
from pprint import pprint

# pandas读取异常的注册数据register_error_data.csv
data_operation = DataOperation('register_error_data.csv')
register_error_data = data_operation.common_get_data_to_list()
# pprint(register_error_data)
# pprint(register_error_data[0])    # 单独提取每个反向用例需要的数据
# pprint(register_error_data[1])
# pprint(register_error_data[5])


@ddt
class RegisterTestCase(unittest.TestCase):
    register_error_data = register_error_data

    @classmethod
    def setUpClass(cls) -> None:
        cls.register = RegisterPage()
        cls.register.reg_open_url()

    # 1 用户名为假(长度小于3)，其他为真
    # @data(register_error_data[0])
    @data(*[register_error_data[0]])
    @unpack
    def test_register_01(self, username, email, password, password1, qq,
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
        # 点击立即注册
        self.register.reg_click_register((By.NAME, 'Submit'))
        # 断言验证 ---> 用户名错误提示信息
        info = self.register.reg_get_text_tips((By.ID, 'username_notice'))
        self.assertEqual('- 用户名长度不能少于 3 个字符。', info)

    # 2 用户名为假(已存在)，其他为真
    @data(*[register_error_data[1]])
    @unpack
    def test_register_02(self, username, email, password, password1, qq,
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
        # 显示等待错误提示信息显示
        if self.register.base_find_element((By.ID, 'username_notice')).text == '* 用户名已经存在,请重新输入':
            # 点击立即注册
            self.register.reg_click_register((By.NAME, 'Submit'))
            # 断言
            info = self.register.reg_get_text_tips((By.ID, 'username_notice'))
            self.assertEqual('* 用户名已经存在,请重新输入', info)
    
    # 3 用户名为假(为纯数字)，其他为真
    @data(*[register_error_data[2]])
    @unpack
    def test_register_03(self, username, email, password, password1, qq,
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
        # 断言1
        info = self.register.reg_get_text_tips((By.ID, 'username_notice'))
        self.assertEqual('* 不能为纯数字', info)
        # 点击立即注册
        sleep(2)    # 等待邮箱 可以注册 文本显示
        self.register.reg_click_register((By.NAME, 'Submit'))
        # 获取用户名显示文本
        user_text = self.register.index_username_text()
        # 退出
        self.register.index_logout()
        # 断言2
        self.assertNotEqual(username, user_text)

    # 4 邮箱为假，其他为真
    @data(*[register_error_data[3]])
    @unpack
    def test_register_04(self, username, email, password, password1, qq,
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
        # 点击立即注册
        self.register.reg_click_register((By.NAME, 'Submit'))
        # 断言
        info = self.register.reg_get_text_tips((By.ID, 'email_notice'))
        self.assertEqual('* 邮件地址不合法', info)

    # 5 邮箱为假(已存在)，其他为真
    @data(*[register_error_data[4]])
    @unpack
    def test_register_05(self, username, email, password, password1, qq,
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
        # 显示等待错误提示信息显示
        if self.register.base_find_element((By.ID, 'email_notice')).text == '* 邮箱已存在,请重新输入':
            # 点击立即注册
            self.register.reg_click_register((By.NAME, 'Submit'))
            # 断言
            info = self.register.reg_get_text_tips((By.ID, 'email_notice'))
            self.assertEqual('* 邮箱已存在,请重新输入', info)

    # 6 密码为假(少于6位)，其他为真
    @data(*[register_error_data[5]])
    @unpack
    def test_register_06(self, username, email, password, password1, qq,
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
        # 点击立即注册
        self.register.reg_click_register((By.NAME, 'Submit'))
        # 断言
        info = self.register.base_get_alert_text()
        self.assertEqual('- 登录密码不能少于 6 个字符。', info.rstrip('\n'))    # alert弹窗文本中多了一个\n,需要去除才能比较

    # 7 两次密码不一致，其他为真
    @data(*[register_error_data[6]])
    @unpack
    def test_register_07(self, username, email, password, password1, qq,
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
        # 点击立即注册
        self.register.reg_click_register((By.NAME, 'Submit'))
        # 断言
        info = self.register.base_get_alert_text()
        self.assertEqual('- 两次输入密码不一致', info.rstrip('\n'))

    # 8 手机号为假(长度超过11位)，其他为真
    @data(*[register_error_data[7]])
    @unpack
    def test_register_08(self, username, email, password, password1, qq,
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
        # 点击立即注册
        self.register.reg_click_register((By.NAME, 'Submit'))
        # 获取用户名显示文本
        user_text = self.register.index_username_text()
        # 退出登录
        self.register.index_logout()
        # 断言
        self.assertNotEqual(username, user_text)

    def tearDown(self) -> None:
        # 点击 免费注册 按钮
        self.register.index_register()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.register.quit(2)


if __name__ == '__main__':
    unittest.main()


