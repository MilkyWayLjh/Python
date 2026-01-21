import unittest
from pageObject.address_page import *
from common.data_operation import DataOperation
from ddt import ddt, data, unpack

# pandas读取数据
data_operation = DataOperation('address_data.csv')
address_data = data_operation.common_get_data_to_list()


@ddt
class AddressTestCase(unittest.TestCase):
    address_data = address_data

    @classmethod
    def setUpClass(cls) -> None:
        # 打开登录浏览器
        cls.address = AddressPage()
        cls.address.login('Zeus', 123456)
        # 点击进入用户中心
        cls.address.user_center_click((By.LINK_TEXT, '用户中心'))

    def setUp(self) -> None:
        # 点击收货地址
        self.address.address_click((By.PARTIAL_LINK_TEXT, '收货地址'))

    # TODO 用例执行的前提是：你的收货地址中 有且只存在一条信息，这样才能从 查看收货地址信息 开始
    # 1 查看地址
    def test_01_view_address(self):
        # 查看
        # self.address.address_click((By.PARTIAL_LINK_TEXT, '收货地址'))
        # 查找删除按钮元素
        btn_element = self.address.base_find_element(('class name', 'bnt_blue'))
        # 断言 按钮是否为真/存在
        self.assertTrue(btn_element)

    # 2 删除地址
    def test_02_del_address(self):
        # 删除
        self.address.del_address_button(('class name', 'bnt_blue'))
        text = self.address.get_alert()
        self.assertEqual('你确认要删除该收货地址吗？', text)

    # 3 新增地址 -- 单条数据
    @data(*[address_data[0]])
    @unpack
    def test_03_add_address(self, num, province, city, district, name, addr, phone, email, postal_code, tel):
        print(num)
        # 输入省
        self.address.select_province(('id', 'selProvinces_0'), 3, province)
        # 输入市
        if self.address.base_find_element((By.CSS_SELECTOR, '#selCities_0>option:nth-of-type(2)')):
            self.address.select_city(('id', 'selCities_0'), 3, city)
            # 输入区
            if self.address.base_find_element((By.CSS_SELECTOR, '#selDistricts_0>option:nth-of-type(2)')):
                self.address.select_district(('id', 'selDistricts_0'), 3, district)
                self.address.input_receiving_name(('id', 'consignee_0'), name)
                self.address.input_receiving_address(('id', 'address_0'), addr)
                self.address.input_receiving_phone(('id', 'tel_0'), phone)
                self.address.input_receiving_email(('id', 'email_0'), email)
                self.address.input_postal_code(('id', 'zipcode_0'), postal_code)
                self.address.input_receiving_tel(('id', 'mobile_0'), tel)
                # 点击新增
                self.address.add_address_click(('class name', 'bnt_blue_2'))
        # 断言
        # 文本获取
        text = self.address.base_get_text((By.XPATH, '/html/body/div[5]/div/div/div/div/p[1]'))
        self.assertEqual('您的收货地址信息已成功更新！', text)

    # 4 修改地址 -- 单条数据
    @data(*[address_data[1]])
    @unpack
    def test_04_add_address(self, num, province, city, district, name, addr, phone, email, postal_code, tel):
        print(num)
        # 输入省
        self.address.select_province(('id', 'selProvinces_0'), 3, province)
        # 输入市
        if self.address.base_find_element((By.CSS_SELECTOR, '#selCities_0>option:nth-of-type(2)')):
            self.address.select_city(('id', 'selCities_0'), 3, city)
            # 输入区
            if self.address.base_find_element((By.CSS_SELECTOR, '#selDistricts_0>option:nth-of-type(2)')):
                self.address.select_district(('id', 'selDistricts_0'), 3, district)
                self.address.input_receiving_name(('id', 'consignee_0'), name)
                self.address.input_receiving_address(('id', 'address_0'), addr)
                self.address.input_receiving_phone(('id', 'tel_0'), phone)
                self.address.input_receiving_email(('id', 'email_0'), email)
                self.address.input_postal_code(('id', 'zipcode_0'), postal_code)
                self.address.input_receiving_tel(('id', 'mobile_0'), tel)
                # 点击 确认修改
                self.address.add_address_click(('class name', 'bnt_blue_1'))
        # 断言
        # 文本获取
        text = self.address.base_get_text((By.XPATH, '/html/body/div[5]/div/div/div/div/p[1]'))
        self.assertEqual('您的收货地址信息已成功更新！', text)

    # 5 再次删除地址
    def test_05_del_address(self):
        # 删除
        self.address.del_address_button(('class name', 'bnt_blue'))
        text = self.address.get_alert()
        self.assertEqual('你确认要删除该收货地址吗？', text)

    # 6 新增地址 -- 多条数据
    @data(*address_data)
    @unpack
    def test_06_add_address(self, num, province, city, district, name, addr, phone, email, postal_code, tel):
        # 输入省
        self.address.select_province(('id', f'selProvinces_{num}'), 3, province)
        # 输入市
        if self.address.base_find_element((By.CSS_SELECTOR, f'#selCities_{num}>option:nth-of-type(2)')):
            self.address.select_city(('id', f'selCities_{num}'), 3, city)
            # 输入区
            if self.address.base_find_element((By.CSS_SELECTOR, f'#selDistricts_{num}>option:nth-of-type(2)')):
                self.address.select_district(('id', f'selDistricts_{num}'), 3, district)
                self.address.input_receiving_name(('id', f'consignee_{num}'), name)
                self.address.input_receiving_address(('id', f'address_{num}'), addr)
                self.address.input_receiving_phone(('id', f'tel_{num}'), phone)
                self.address.input_receiving_email(('id', f'email_{num}'), email)
                self.address.input_postal_code(('id', f'zipcode_{num}'), postal_code)
                self.address.input_receiving_tel(('id', f'mobile_{num}'), tel)
                # 点击新增
                self.address.add_address_click(('class name', 'bnt_blue_2'))
        # 断言
        # 文本获取
        text = self.address.base_get_text((By.XPATH, '/html/body/div[5]/div/div/div/div/p[1]'))
        self.assertEqual('您的收货地址信息已成功更新！', text)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.address.quit(2)

if __name__ == '__main__':
    unittest.main()
