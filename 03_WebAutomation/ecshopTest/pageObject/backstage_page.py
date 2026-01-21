from base.base import *
from common.common_login import CommonLogin


class GoodsAddPage(CommonLogin):
    def admin_login(self, username, password):
        self.common_admin_login(username=username, password=password)

    # 输入商品信息商品
    def goods_send_keys(self, locator, content):
        # 先清空
        self.base_clear(locator=locator)
        self.base_send_keys(locator, content=content)

    # 商品管理-添加新商品
    def goods_click(self, locator):
        self.base_click(locator=locator)

    # 清空价格
    def price_clear(self, locator):
        self.base_clear(locator=locator)

    # 选择单选框
    def check_box(self, locator):
        self.base_click(locator=locator)

    # 下拉菜单
    def select(self, locator, method, values):
        self.base_get_select(locator=locator, method=method, values=values)

    # 滚动到底部
    def scroll(self):
        self.base_scroll()


if __name__ == '__main__':
    goods = GoodsAddPage()
    goods.admin_login('admin', 'admin123456')
    goods.driver.switch_to.frame('menu-frame')
    goods.goods_click((By.CSS_SELECTOR, '#main-div>div>ul>li:nth-of-type(2)'))
    goods.goods_click((By.LINK_TEXT, "添加新商品"))
    goods.driver.switch_to.default_content()  # 切换回父frame
    goods.driver.switch_to.frame('main-frame')
    goods.goods_click((By.ID, 'general-tab'))

    goods.goods_send_keys((By.NAME, 'goods_name'), 'test')
    # 商品分类
    goods.select((By.NAME, 'cat_id'), 2, '19')
    # 本店售价
    goods.goods_send_keys((By.XPATH, '//*[@id="general-table"]/tbody/tr[7]/td[2]/input[1]'), '99')
    goods.goods_click((By.XPATH, '//*[@id="tabbody-div"]/form/div/input[2]'))
