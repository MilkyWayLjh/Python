import unittest
from pageObject.order_management_page import *


class ManagementTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        # 打开浏览器
        cls.order = OrderManagePage()
        # 先登录前台
        cls.order.common_user_login('Zeus', '123456')

    def setUp(self) -> None:
        # 点击用户中心
        self.order.base_click((By.LINK_TEXT, '用户中心'))
        # 点击我的订单
        self.order.base_click((By.LINK_TEXT, '我的订单'))

    # test1 查看前后台最新生成的订单
    def test_01_view_order(self):
        # 获取前台最新一条订单编号
        order_id = self.order.base_get_text(
            (By.XPATH, '/html/body/div[6]/div[2]/div/div/div/table/tbody/tr[1]/td[1]/a')
        )
        # 登录后台
        self.order.common_admin_login('admin', 'admin123456')
        # 切换到左侧导航栏框架
        self.order.change_frame('menu-frame')
        # 点击订单管理
        self.order.manage((By.XPATH, '//*[@id="menu-ul"]/li[4]'))
        # 点击订单列表
        self.order.order_list((By.XPATH, '//*[@id="sub-menu-02_order_list"]/a'))
        # 退出导航栏框架
        self.order.sign_out_frame()
        # 进入订单查询的框架
        self.order.change_frame('main-frame')
        # 获取后台最新一条订单编号
        order_id2 = self.order.base_get_text((By.ID, 'order_0'))
        # 点击查看订单详情
        if order_id2:
            sleep(1)
            self.order.view_order((By.XPATH, '//*[@id="listDiv"]/table[1]/tbody/tr[3]/td[7]/a'))
            sleep(2)
            self.order.base_scroll()
        # 断言 前后台同一账号的订单编号是否一致
        self.assertEqual(order_id, order_id2)

    # test2 后台输入前台最新订单编号搜索
    def test_02_view_order(self):
        # 获取前台最新一条订单编号
        order_id = self.order.base_get_text(
            (By.XPATH, '/html/body/div[6]/div[2]/div/div/div/table/tbody/tr[1]/td[1]/a')
        )
        # 直接进入后台(因为第一条用例执行后会有登录记录)
        self.order.base_open_url('http://localhost:8080/ecshop/admin/')
        # 切换到左侧导航栏框架
        self.order.change_frame('menu-frame')
        # 点击订单管理
        self.order.manage((By.XPATH, '//*[@id="menu-ul"]/li[4]'))
        # 点击订单列表
        self.order.order_list((By.XPATH, '//*[@id="sub-menu-02_order_list"]/a'))
        # 退出导航栏框架
        self.order.sign_out_frame()
        # 进入订单查询的框架
        self.order.change_frame('main-frame')
        # 输入订单号
        self.order.order_num((By.XPATH, '//*[@id="order_sn"]'), order_id)
        # 点击搜索
        self.order.search_button((By.XPATH, '/html/body/div[3]/form/input[3]'))
        # 获取存在的订单项
        order_item = self.order.base_get_text((By.CSS_SELECTOR, '#listDiv>table:nth-child(1)>tbody>tr:nth-child(3)'))
        # 点击查看订单详情
        # if order_item:
        #     sleep(2)
        #     self.order.view_order((By.XPATH, '//*[@id="listDiv"]/table[1]/tbody/tr[3]/td[7]/a'))
        # 断言 前台同一账号的订单编号 在后台是否存在搜索结果
        self.assertTrue(order_item)

    def tearDown(self) -> None:
        self.order.driver.get('http://127.0.0.1:8080/ecshop/user.php')

    @classmethod
    def tearDownClass(cls) -> None:
        # 退出关闭浏览器
        cls.order.quit(2)


if __name__ == '__main__':
    unittest.main()
