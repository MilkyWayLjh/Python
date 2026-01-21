from base.base import *
from common.common_login import CommonLogin


# 定义收货地址的类
class AddressPage(CommonLogin):
    # 登录
    def login(self, username, password):
        self.common_user_login(username, password)

    # 点击用户中心
    def user_center_click(self, locator):
        self.base_click(locator)

    # 点击收货地址
    def address_click(self, locator):
        self.base_click(locator)

    # 定位省
    def select_province(self, locator, method, values):
        self.base_get_select(locator, method, values)

    # 定位市
    def select_city(self, locator, method, values):
        self.base_get_select(locator, method, values)

    # 定位区
    def select_district(self, locator, method, values):
        self.base_get_select(locator, method, values)

    # 定位收货人姓名
    def input_receiving_name(self, locator, content):
        # 先清空
        self.base_clear(locator)
        self.base_send_keys(locator, content)

    # 定位详细地址
    def input_receiving_address(self, locator, content):
        # 先清空
        self.base_clear(locator)
        self.base_send_keys(locator, content)

    # 定位电话
    def input_receiving_phone(self, locator, content):
        # 先清空
        self.base_clear(locator)
        self.base_send_keys(locator, content)

    # 定位电子邮箱
    def input_receiving_email(self, locator, content):
        # 先清空
        self.base_clear(locator)
        self.base_send_keys(locator, content)

    # 定位邮政编码
    def input_postal_code(self, locator, content):
        # 先清空
        self.base_clear(locator)
        self.base_send_keys(locator, content)

    # 定位手机
    def input_receiving_tel(self, locator, content):
        # 先清空
        self.base_clear(locator)
        self.base_send_keys(locator, content)

    # 点击新增按钮
    def add_address_click(self, locator):
        self.base_click(locator)

    # 删除地址
    def del_address_button(self, locator):
        self.base_click(locator)

    # 获取弹窗
    def get_alert(self):
        return self.base_get_alert_text()

    # 获取文本
    def get_text(self, locator):
        return self.base_get_text(locator)


if __name__ == '__main__':
    address = AddressPage()
    address.login('Zeus', 123456)
    address.user_center_click((By.LINK_TEXT, '用户中心'))
    address.address_click((By.PARTIAL_LINK_TEXT, '收货地址'))
    # 如果你的收货地址已存在一列或更多地址信息，就把下列对应的 xxx_0 改为 xxx_1, xxx_1 改为 xxx_2 以此类推...
    address.select_province(('id', 'selProvinces_1'), 3, '四川省')
    if address.base_find_element((By.CSS_SELECTOR, '#selCities_1 option[value="271"]')):
        address.select_city(('id', 'selCities_1'), 3, '成都市')
        if address.base_find_element((By.CSS_SELECTOR, '#selDistricts_1 option[value="2713"]')):
            address.select_district(('id', 'selDistricts_1'), 3, '武侯区')
            address.input_receiving_name(('id', 'consignee_1'), 'Zeus')
            address.input_receiving_address(('id', 'address_1'), '111')
            address.input_receiving_phone(('id', 'tel_1'), 13212312312)
            address.input_receiving_email(('id', 'email_1'), '123@qq,com')
            address.input_receiving_email(('id', 'email_1'), '123@qq,com')
            address.add_address_click(('class name', 'bnt_blue_2'))

    # address.del_address_button(('class name', 'bnt_blue'))

    address.quit(2)
