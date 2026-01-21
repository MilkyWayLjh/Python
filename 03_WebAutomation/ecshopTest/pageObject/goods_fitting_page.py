from base.base import *
from common.common_login import CommonLogin


class GoodsFittingPage(CommonLogin):
    def user_login(self, username, password):
        self.common_user_login(username=username, password=password)

    # 首页
    def index_url(self, locator):
        self.base_click(locator=locator)

    # 商品分类侧边栏→配件
    def goods_fittings_click(self, locator):
        self.base_click(locator=locator)

    # 数码时尚
    def fittings_fashion(self, locator):
        self.base_click(locator=locator)

    # 保护壳
    def fittings_protection(self, locator):
        self.base_click(locator=locator)

    # 排序
    # 上架时间
    def fittings_uptime(self, locator):
        self.base_click(locator=locator)

    # 价格
    def fittings_price(self, locator):
        self.base_click(locator=locator)

    # 更新时间
    def fittings_downtime(self, locator):
        self.base_click(locator=locator)

    # 点击商品立即购买同时也是浏览
    def goods_click(self, locator):
        self.base_click(locator=locator)

    # 浏览
    def browse(self):
        # 点击首页
        self.base_click((By.LINK_TEXT, "首页"))
        # 浏览配件分类
        self.base_click((By.LINK_TEXT, "配件"))
        # sleep(2)
        # # 上架时间排序
        # self.base_click((By.CSS_SELECTOR, 'form[name="listform"]>a>img'))
        # sleep(2)
        # # 价格排序
        # self.base_click((By.CSS_SELECTOR, 'form[name="listform"]>a:nth-of-type(2)>img'))
        # sleep(2)
        # # 更新时间排序
        # self.base_click((By.CSS_SELECTOR, 'form[name="listform"]>a:nth-of-type(3)>img'))
        # sleep(2)
        # # 浏览第一个商品
        # self.base_click((By.LINK_TEXT, "立即购买"))
        # sleep(2)

    def goods_list(self):
        goods_locator = (By.CSS_SELECTOR, '.cat-box>.cat1>a')
        # 通过定位获取类目元素(列表)
        a_elements = self.base_find_element(goods_locator)
        # 返回类目元素的href属性值
        return [a_element.get_attribute('href') for a_element in a_elements]


if __name__ == '__main__':
    gp = GoodsFittingPage()
    # gp.user_open_url("http://localhost:8080/ecshop/index.php")
    # 点击配件
    gp.goods_fittings_click((By.LINK_TEXT, "配件"))
    sleep(3)
    # 上架时间排序
    gp.fittings_uptime((By.CSS_SELECTOR, 'form[name="listform"]>a>img'))
    sleep(2)
    # 价格排序
    gp.fittings_price((By.CSS_SELECTOR, 'form[name="listform"]>a:nth-of-type(2)>img'))
    sleep(2)
    # 更新时间排序
    gp.fittings_downtime((By.CSS_SELECTOR, 'form[name="listform"]>a:nth-of-type(3)>img'))
    sleep(2)
    # 默认浏览第一个商品
    gp.goods_click((By.LINK_TEXT, "立即购买"))
    sleep(2)
    # 立即购买加入购物车
    gp.goods_click((By.CSS_SELECTOR, '#ECS_FORMBUY > ul > li.padd > table > tbody > tr > td.td1 > a > img'))
