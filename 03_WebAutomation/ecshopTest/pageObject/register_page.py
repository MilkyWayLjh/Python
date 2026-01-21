from pageObject.index_page import *


class RegisterPage(IndexPage):
    def reg_open_url(self, url='http://localhost:8080/ecshop/user.php?act=register'):
        self.base_open_url(url)

    # 用户名
    def reg_username_ipt(self, locator, content):
        self.base_send_keys(locator, content)

    # email
    def reg_email_ipt(self, locator, content):
        self.base_send_keys(locator, content)

    # 密码
    def reg_password_ipt(self, locator, content):
        self.base_send_keys(locator, content)

    # 确认密码
    def reg_password1_ipt(self, locator, content):
        self.base_send_keys(locator, content)

    # QQ
    def reg_qq_ipt(self, locator, content):
        self.base_send_keys(locator, content)

    # 办公电话
    def reg_work_phone_ipt(self, locator, content):
        self.base_send_keys(locator, content)

    # 家庭电话
    def reg_home_phone_ipt(self, locator, content):
        self.base_send_keys(locator, content)

    # 手机
    def reg_mobile_phone_ipt(self, locator, content):
        self.base_send_keys(locator, content)

    # 密码提示问题
    def reg_pwd_question_select(self, locator, values):
        self.base_get_select(locator, 1, values)

    # 密码问题答案
    def reg_pwd_answer_ipt(self, locator, content):
        self.base_send_keys(locator, content)

    # 点击接收用户协议
    def reg_click_agreement(self, locator):
        self.base_click(locator)

    # 点击立即注册
    def reg_click_register(self, locator):
        self.base_click(locator)

    # 获取错误提示信息
    def reg_get_text_tips(self, locator):
        return self.base_get_text(locator)


if __name__ == '__main__':
    register = RegisterPage()
    register.reg_open_url()

    sleep(1)
    register.reg_username_ipt((By.ID, 'username'), '12')
    sleep(1)
    register.reg_pwd_question_select((By.NAME, 'sel_question'), 3)
    sleep(1)
    print(register.reg_get_text_tips((By.ID, 'username_notice')))
    sleep(1)
    register.reg_click_agreement((By.NAME, 'agreement'))
    # 用户协议默认是勾选中的
    sleep(1)
    register.reg_click_agreement((By.NAME, 'agreement'))

    register.quit(2)



