import unittest
from pageObject.shopping_car_page import ShoppingCarPage, By


class CarsTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.sc = ShoppingCarPage()
        self.sc.common_user_login('Zeus', '123456')

    # TODO 因为购物车的自动化bug需要每次用例执行前都添加商品
    def add_goods(self):
        self.sc.base_click((By.LINK_TEXT, "首页"))
        self.sc.base_click((By.LINK_TEXT, "配件"))
        self.sc.add_shopcart()

    # 添加购物车
    def test_01_shopcart(self):
        self.sc.base_click((By.LINK_TEXT, "首页"))
        self.sc.base_click((By.LINK_TEXT, "配件"))
        # 获取商品标题
        goods_name1 = self.sc.base_get_attribute(
            (By.XPATH, '/html/body/div[4]/div[2]/div/div[2]/form/div/div/div[1]/div/div[1]/a'),
            'title'
        )
        self.sc.add_shopcart()
        # 断言跳转到购物车后里面的商品是添加的商品
        goods_name2 = self.sc.base_get_text(
            (By.XPATH, '/html/body/div[6]/div[1]/form/table[1]/tbody/tr[2]/td[1]/a[2]'))
        self.assertEqual(goods_name1, goods_name2)

    def test_02_shopcart(self):
        self.add_goods()
        # 点击继续购物返回主页
        self.sc.continue_shop()
        # 断言点击继续购物后是跳转到首页
        title = self.sc.driver.title
        self.assertEqual('ECSHOP演示站 - Powered by ECShop', title)

    def test_03_shopcart(self):
        self.sc.base_click((By.LINK_TEXT, "首页"))
        self.sc.base_click((By.LINK_TEXT, "配件"))
        # 获取商品标题
        goods_name1 = self.sc.base_get_attribute(
            (By.XPATH, '/html/body/div[4]/div[2]/div/div[2]/form/div/div/div[1]/div/div[1]/a'),
            'title'
        )
        self.sc.add_shopcart()
        # 查看购物车
        self.sc.check_shopcart()
        # 断言购物车内的商品名和点击添加购物车时的相同
        goods_name = self.sc.base_get_text((By.XPATH, '//*[@id="formCart"]/table[1]/tbody/tr[2]/td[1]/a[2]'))
        self.assertEqual(goods_name1, goods_name)

    def test_04_shopcart(self):
        self.add_goods()
        # 修改购物车商品数量
        self.sc.modify_shopcart()
        # 断言修改购物车内商品的购买数量点击刷新购物车后，右上角查看购物车里的数字也会随着改变
        goods_number = self.sc.base_get_text((By.XPATH, '//*[@id="ECS_CARTINFO"]/a'))
        self.assertEqual('购物车(3)', goods_number)

    def test_05_shopcart(self):
        self.add_goods()
        # 删除购物车
        self.sc.delete_goods()
        # 断言删除购物车后，右上角查看购物车里的数字为0
        goods_number = self.sc.base_get_text((By.XPATH, '//*[@id="ECS_CARTINFO"]/a'))
        self.assertEqual('购物车(0)', goods_number)

    def test_06_shopcart(self):
        self.add_goods()
        # 清空购物车
        self.sc.clear_shopcart()
        # 断言清空购物车后，右上角查看购物车里的数字为0
        goods_number = self.sc.base_get_text((By.XPATH, '//*[@id="ECS_CARTINFO"]/a'))
        self.assertEqual('购物车(0)', goods_number)

    def tearDown(self) -> None:
        self.sc.quit(2)


if __name__ == '__main__':
    unittest.main()
