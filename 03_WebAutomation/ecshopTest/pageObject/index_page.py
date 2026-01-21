from base.base import Base, By, sleep


class IndexPage(Base):
    def index_open_url(self, url='http://localhost:8080/ecshop/index.php'):
        self.base_open_url(url)

    def index_username_text(self):
        return self.base_get_text((By.XPATH, '//font[@class="f4_b"]'))

    def index_login(self):
        self.base_click((By.PARTIAL_LINK_TEXT, '请登录'))

    def index_logout(self):
        self.base_click((By.LINK_TEXT, '退出'))

    def index_register(self):
        self.base_click((By.LINK_TEXT, '免费注册'))

    def index_user_center(self):
        self.base_click((By.LINK_TEXT, '用户中心'))

    def index_shop_cart(self):
        self.base_click((By.PARTIAL_LINK_TEXT, '购物车'))


if __name__ == '__main__':
    index = IndexPage()
    index.index_open_url()
    sleep(1)

    # index.index_username_text()
    # index.index_login()
    # index.index_logout()
    # index.index_register()
    # index.index_user_center()
    # index.index_shop_cart()

    index.quit(2)

