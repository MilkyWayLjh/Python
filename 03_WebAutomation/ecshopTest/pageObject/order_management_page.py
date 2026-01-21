from base.base import *
from common.common_login import CommonLogin


class OrderManagePage(CommonLogin):
    # 登录
    def login(self, username, password):
        self.common_admin_login(username, password)

    # 切换框架
    def change_frame(self, content):
        self.driver.switch_to.frame(content)

    # 退出框架到最外层
    def sign_out_frame(self):
        self.driver.switch_to.default_content()

    # 定位订单管理
    def manage(self, locator):
        self.base_click(locator)

    # 定位订单列表
    def order_list(self, locator):
        self.base_click(locator)

    # 定位订单号的输入框
    def order_num(self, locator, content):
        self.base_send_keys(locator, content)

    # 定位搜索按钮
    def search_button(self, locator):
        self.base_click(locator)

    # 定位查看
    def view_order(self, locator):
        self.base_click(locator)


if __name__ == '__main__':

    order = OrderManagePage()
    # 登录
    order.login('admin', 'admin123')
    # 切换到左侧导航栏框架
    order.change_frame('menu-frame')
    # 点击订单管理
    order.manage((By.XPATH, '//*[@id="menu-ul"]/li[4]'))
    # 点击订单列表
    order.order_list((By.XPATH, '//*[@id="sub-menu-02_order_list"]/a'))
    # 退出导航栏框架
    order.sign_out_frame()
    # 进入订单查询的框架
    order.change_frame('main-frame')
    # 输入订单号
    order.order_num((By.XPATH, '//*[@id="order_sn"]'), '2022120583107')
    # 点击搜索
    order.search_button((By.XPATH, '/html/body/div[3]/form/input[3]'))
    # 点击查看
    order.view_order((By.XPATH, '//*[@id="listDiv"]/table[1]/tbody/tr[3]/td[7]/a'))
