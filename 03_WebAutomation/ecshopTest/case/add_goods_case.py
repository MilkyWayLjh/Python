import unittest
from pageObject.backstage_page import *
from common.data_operation import DataOperation
from os import path
from ddt import ddt, data, unpack

# pandas读取数据
data_operation = DataOperation('add_goods_data.csv')
add_goods_data = data_operation.common_get_data_to_list()


@ddt
class BrowseCase(unittest.TestCase):
    add_goods_data = add_goods_data

    @classmethod
    def setUpClass(cls) -> None:
        # 登录后台
        cls.ga = GoodsAddPage()
        cls.ga.common_admin_login('admin', 'admin123456')
        # 商品管理→添加商品
        cls.ga.driver.switch_to.frame('menu-frame')
        cls.ga.goods_click((By.CSS_SELECTOR, '#main-div>div>ul>li:nth-of-type(2)'))
        cls.ga.goods_click((By.LINK_TEXT, "添加新商品"))
        cls.ga.driver.switch_to.default_content()  # 切换回父frame
        cls.ga.driver.switch_to.frame('main-frame')

    def setUp(self) -> None:
        # 判断如果右侧添加新商品按钮存在 就点击
        if self.ga.base_find_element((By.CSS_SELECTOR, 'body>h1>a.btn.btn-right.btn-add-goods')):
            self.ga.goods_click((By.CSS_SELECTOR, 'body>h1>a.btn.btn-right.btn-add-goods'))

    # 测试 添加商品用例
    @data(*add_goods_data)
    @unpack
    def test_add_goods(self, goods_name, font_style, goods_type, goods_brand, supplier,
                       price1, price2_1, price2_2, price2_3, discount_num, discount_price,
                       price3, vir_num, score1, score2, goods_number):
        # 通用信息
        self.ga.goods_click((By.ID, 'general-tab'))
        self.ga.goods_send_keys((By.NAME, 'goods_name'), goods_name)
        # 字体样式
        self.ga.select((By.NAME, 'goods_name_style'), 2, font_style)
        # 商品分类
        self.ga.select((By.NAME, 'cat_id'), 2, str(goods_type))
        # 商品品牌
        self.ga.select((By.NAME, 'brand_id'), 2, str(goods_brand))
        # 选择供货商
        self.ga.select((By.XPATH, '//*[@id="suppliers_id"]'), 2, str(supplier))
        # 本店售价
        self.ga.goods_send_keys((By.XPATH, '//*[@id="general-table"]/tbody/tr[7]/td[2]/input[1]'), price1)

        # 会员价格
        #   注册用户
        self.ga.goods_send_keys((By.XPATH, '//*[@id="rank_1"]'), price2_1)
        #   代销用户
        self.ga.goods_send_keys((By.XPATH, '//*[@id="rank_3"]'), price2_2)
        #   vip
        self.ga.goods_send_keys((By.XPATH, '//*[@id="rank_2"]'), price2_3)

        # 商品优惠价格
        #    优惠数量
        self.ga.goods_send_keys((By.XPATH, '//*[@id="tbody-volume"]/tbody/tr/td/input[1]'), discount_num)
        #    优惠价格
        self.ga.goods_send_keys((By.XPATH, '//*[@id="tbody-volume"]/tbody/tr/td/input[2]'), discount_price)

        # 市场售价
        self.ga.goods_send_keys((By.XPATH, '//*[@id="general-table"]/tbody/tr[10]/td[2]/input[1]'), int(price3))
        # 取整数
        self.ga.goods_click(
            (By.CSS_SELECTOR, '#general-table>tbody>tr:nth-child(10)>td:nth-child(2)>input.btn.btn-def'))
        # 虚拟销量
        self.ga.goods_send_keys((By.NAME, 'virtual_sales'), vir_num)
        #  赠送消费积分数
        self.ga.goods_send_keys((By.NAME, 'give_integral'), score1)
        #  赠送等级积分数
        self.ga.goods_send_keys((By.NAME, 'rank_integral'), score2)

        # 上传商品图片  使用绝对路径
        # self.ga.base_send_keys(
        #     (By.CSS_SELECTOR, '#general-table input[name="goods_img"]'),
        #     path.abspath('../data/Volunteer_to_work.jpg')
        # )

        # 其他信息(重点关注 库存数量)
        self.ga.goods_click((By.ID, 'mix-tab'))
        self.ga.goods_send_keys((By.NAME, 'goods_number'), goods_number)

        # 确定
        self.ga.goods_click((By.XPATH, '//*[@id="tabbody-div"]/form/div/input[2]'))

        # 重置
        # self.ga.goods_click((By.CSS_SELECTOR, '#tabbody-div > form > div > input:nth-child(3)'))

        # 显示等待进入商品列表
        if self.ga.base_find_element(
                (By.CSS_SELECTOR, '#listDiv>table:nth-child(1)>tbody>tr:nth-child(3)>td.first-cell>span'),
                timeout=10
        ):
            goods_name2 = self.ga.base_get_text(
                (By.CSS_SELECTOR, '#listDiv>table:nth-child(1)>tbody>tr:nth-child(3)>td.first-cell>span')
            )
            # 断言
            self.assertEqual(goods_name, goods_name2)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.ga.quit(3)


if __name__ == '__main__':
    unittest.main()
