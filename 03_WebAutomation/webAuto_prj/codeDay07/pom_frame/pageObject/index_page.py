from codeDay07.pom_frame.common.base import Base
from selenium.webdriver.common.by import By


class IndexPage(Base):
    def index_username_text(self):
        return self.base_get_text((By.XPATH, '//font[@class="f4_b"]'))

    def index_logout(self):
        self.base_click((By.LINK_TEXT, '退出'))

    def index_login(self):
        self.base_click((By.PARTIAL_LINK_TEXT, '请登录'))


if __name__ == '__main__':
    index = IndexPage()
    index.index_username_text()
    # index.index_logout()
    # index.index_logout()
