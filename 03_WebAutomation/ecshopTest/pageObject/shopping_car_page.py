from base.base import *
from common.common_login import CommonLogin


class ShoppingCarPage(CommonLogin):
    # 购物车增加操作：
    def add_shopcart(self):
        # 定位一个商品
        self.base_click((By.LINK_TEXT, "立即购买"))
        # 定位立即购买，加入商品到购物车
        self.base_click((By.CSS_SELECTOR, '#ECS_FORMBUY>ul>li.padd>table>tbody>tr>td.td1>a>img'))

    def continue_shop(self):
        # 定位继续购物按钮点击
        self.base_click((By.XPATH, '/html/body/div[6]/div[1]/table/tbody/tr/td[1]/a/img'))

    # 购物车查看操作
    def check_shopcart(self):
        # 定位购物车按钮点击，查看购物车
        self.base_click((By.XPATH, '//*[@id="ECS_CARTINFO"]/a'))

    # 购物车修改操作
    def modify_shopcart(self, num=3):
        # 定位购物车商品购买数量清空并修改
        self.base_clear((By.XPATH, '/html/body/div[6]/div[1]/form/table[1]/tbody/tr[2]/td[5]/input'))
        self.base_send_keys((By.XPATH, '/html/body/div[6]/div[1]/form/table[1]/tbody/tr[2]/td[5]/input'), num)
        # 定位更新购物车按钮点击
        self.base_click((By.XPATH, '//*[@id="formCart"]/table[2]/tbody/tr/td[2]/input[2]'))

    # 购物车删除操作
    def delete_goods(self):
        # 定位购物车删除按钮点击
        self.base_click((By.LINK_TEXT, '删除'))
        # 切换到弹窗点击确认
        self.base_get_alert_text()

    def clear_shopcart(self):
        # 定位清空购物车按钮点击
        self.base_click((By.XPATH, '//*[@id="formCart"]/table[2]/tbody/tr/td[2]/input[1]'))
