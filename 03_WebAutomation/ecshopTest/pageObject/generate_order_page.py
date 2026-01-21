from pageObject.goods_fitting_page import *


class OrderPage(GoodsFittingPage):
    # 登录
    def login(self, username, password):
        self.common_user_login(username, password)

    # 定位首页
    def home_page(self, locator):
        self.index_url(locator)

    # 点击用户中心
    def user_center_click(self):
        self.base_click((By.LINK_TEXT, '用户中心'))

    # 定位配件
    def fittings(self, locator):
        self.goods_fittings_click(locator)

    # 定位立即购买浏览商品
    def goods(self, locator):
        self.goods_click(locator)

    # 定位立即购买下单
    def buy(self, locator):
        self.goods_click(locator)

    # 定位结算
    def settle(self, locator):
        self.base_click(locator)

    # 定位支付方式
    def payment_method(self, locator):
        self.base_click(locator)

    # 定位提交订单
    def submit(self, locator):
        self.base_click(locator)

    # 定位我的订单
    def my_order(self):
        self.base_click((By.LINK_TEXT, '我的订单'))

    # 获取最新一条订单的编号
    def read_order_id(self):
        return self.base_get_text((By.XPATH, '/html/body/div[6]/div[2]/div/div/div/table/tbody/tr[1]/td[1]/a'))


if __name__ == '__main__':

    order = OrderPage()
    order.login('Thorns', 'admin123')

    # 点击首页
    order.home_page((By.XPATH, "//div[@class='m_left']/ul/li[1]/a"))

    # 点击配件10
    order.fittings((By.LINK_TEXT, "配件"))
    # 默认浏览第一个商品
    order.goods((By.LINK_TEXT, "立即购买"))

    # 购买
    order.buy((By.XPATH, "//td[@class='td1']/a/img"))
    # 结算
    order.settle((By.XPATH, "/html/body/div[6]/div[1]/table/tbody/tr/td[2]/a/img"))

    # 选择支付方式(不选择支付方式默认是余额支付就是已支付的订单， 选择银行汇款/转帐支付就是未支付订单)
    # order.payment_method((By.XPATH, '//*[@id="paymentTable"]/tbody/tr[3]/td[1]/input'))
    # 提交订单
    # order.submit((By.XPATH, "/html/body/div[6]/form/div[15]/div[2]/input[1]"))
    # 进入用户中心查看生成的订单
    # order.user_center_click()
    # order.my_order()








