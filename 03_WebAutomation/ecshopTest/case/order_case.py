import unittest
from pageObject.generate_order_page import *


class OrderTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        # 打开登录浏览器
        cls.order = OrderPage()
        cls.order.login('Zeus', '123456')

    def setUp(self) -> None:
        # 点击首页
        self.order.home_page((By.XPATH, "//div[@class='m_left']/ul/li[1]/a"))
        # 点击配件
        self.order.fittings((By.LINK_TEXT, "配件"))
        # 默认浏览第一个商品
        self.order.goods((By.LINK_TEXT, "立即购买"))
        # 购买
        self.order.buy((By.XPATH, "//td[@class='td1']/a/img"))
        # 结算
        self.order.settle((By.XPATH, "/html/body/div[6]/div[1]/table/tbody/tr/td[2]/a/img"))

    # test01 已支付订单
    def test_01_order_paid(self):
        # TODO 可能自动化有bug，有时候会让你选择地址配送，有时候连地址选择的页面都没有，直接进入支付详情页面，所以在这可以做一个判断
        page_element = self.order.base_find_element(
            (By.CSS_SELECTOR, '#theForm>div>table>tbody>tr:nth-child(5)>td>input.bnt_blue_2')
        )
        if page_element:
            # 默认选择第一个地址配送(由于测的是订单模块，所以默认是存在收货地址的)
            self.order.base_click((By.CSS_SELECTOR, '#theForm>div>table>tbody>tr:nth-child(5)>td>input.bnt_blue_2'))

        # 判断对应支付方式是否被选中
        if not self.order.base_find_element(
                (By.XPATH, '//*[@id="paymentTable"]/tbody/tr[2]/td[1]/input')
        ).is_selected():
            self.order.payment_method((By.XPATH, '//*[@id="paymentTable"]/tbody/tr[2]/td[1]/input'))
        # 提交订单
        self.order.submit((By.XPATH, "/html/body/div[6]/form/div[15]/div[2]/input[1]"))
        # 断言
        text = self.order.base_get_text((By.XPATH, '/html/body/div[6]/div/table/tbody/tr[1]/td/strong[2]'))
        self.assertEqual('余额支付', text)
        # 进入用户中心查看生成的订单
        self.order.user_center_click()
        self.order.my_order()

    # test02 未支付订单
    def test_02_order_unpaid(self):
        # 原理同上
        page_element = self.order.base_find_element(
            (By.CSS_SELECTOR, '#theForm>div>table>tbody>tr:nth-child(5)>td>input.bnt_blue_2')
        )
        if page_element:
            self.order.base_click((By.CSS_SELECTOR, '#theForm>div>table>tbody>tr:nth-child(5)>td>input.bnt_blue_2'))

        # 选择支付方式
        if not self.order.base_find_element(
                (By.XPATH, '//*[@id="paymentTable"]/tbody/tr[3]/td[1]/input')
        ).is_selected():
            self.order.payment_method((By.XPATH, '//*[@id="paymentTable"]/tbody/tr[3]/td[1]/input'))
        # 提交订单
        self.order.submit((By.XPATH, "/html/body/div[6]/form/div[15]/div[2]/input[1]"))
        # 断言
        text = self.order.base_get_text((By.XPATH, '/html/body/div[6]/div/table/tbody/tr[1]/td/strong[2]'))
        self.assertEqual('银行汇款/转帐', text)
        # 获取订单编号
        # text_num = self.order.base_get_text((By.XPATH, '/html/body/div[6]/div/h6/font'))
        # print(text_num)
        # 进入用户中心查看生成的订单
        self.order.user_center_click()
        self.order.my_order()

    @classmethod
    def tearDownClass(cls) -> None:
        # 退出关闭浏览器
        cls.order.quit(3)


if __name__ == '__main__':
    unittest.main()


