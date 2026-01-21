import unittest
from pageObject.goods_fitting_page import GoodsFittingPage, By
from pprint import pprint


class BrowseTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.goods = GoodsFittingPage()
        self.goods.user_login('Zeus', '123456')
        self.goods.browse()

    # 商品浏览
    def test_browse(self):
        # 获取商品外部标题 列表
        elements_list = self.goods.base_find_elements((By.CSS_SELECTOR, '.goods-title>a'))
        # pprint(elements_list)
        # 通过列表推导式 创建商品标题列表
        title_list = [i.get_attribute('title') for i in elements_list]
        # print(title_list)
        for title in title_list:
            # 通过商品标题点击进入详情
            self.goods.base_click((By.CSS_SELECTOR, f'.goods-title>a[title="{title}"]'))
            # 获取内部商品标题
            title1 = self.goods.base_get_text((By.CSS_SELECTOR, '#ECS_FORMBUY>div'))
            # print(title1)
            # 断言 去除两边空格再比较
            self.assertEqual(title.strip(), title1.strip())
            # 浏览器返回
            self.goods.driver.back()

    def tearDown(self) -> None:
        self.goods.quit(2)


if __name__ == '__main__':
    unittest.main()
