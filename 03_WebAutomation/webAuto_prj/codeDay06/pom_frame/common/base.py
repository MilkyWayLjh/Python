"""
放置基本的操作
    打开网址
    点击
    输入
    清空
    查找元素
    获取文本
"""
from selenium import webdriver
from time import sleep
# from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Base:
    def __init__(self, browser='chrome'):
        # 打开浏览器, 设置driver
        if browser == 'chrome':
            self.driver = webdriver.Chrome()
        elif browser == 'edge':
            self.driver = webdriver.Edge()
        elif browser == 'firefox':
            self.driver = webdriver.Firefox()
        else:
            print('不支持该浏览器')
            self.driver = None

    def base_open_url(self, url):
        self.driver.get(url)
        self.driver.maximize_window()

    def base_find_element(self, locator, timeout=5):
        """
        定位单个元素
        :param locator: 定位器,元组类型
        :param timeout: 超时时间
        :return: WebElement对象|None
        """
        try:
            return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator), message='元素定位失败')
        except Exception as e:
            print(e)
            return None

    def base_find_elements(self, locator, timeout=5):
        """
        定位多个元素
        :param locator: 定位器
        :param timeout: 超时时间
        :return: WebElement对象|None
        """
        try:
            return WebDriverWait(self.driver, timeout) \
                .until(EC.presence_of_all_elements_located(locator), message='元素定位失败')
        except Exception as e:
            print(e)
            return []

    def base_click(self, locator):
        self.base_find_element(locator).click()

    def base_send_keys(self, locator, content):
        self.base_find_element(locator).send_keys(content)

    def base_get_text(self, locator):
        return self.base_find_element(locator).text

    def base_get_attribute(self, locator, name='outerHTML'):
        """
        获取标签属性值
        :param locator: 定位器
        :param name: 属性名
        :return:
        """
        element = self.base_find_element(locator)
        if element:
            return element.get_attribute(name)

    def close(self, seconds=0):
        sleep(seconds)
        self.driver.close()

    def quit(self, seconds=0):
        sleep(seconds)
        self.driver.quit()


if __name__ == '__main__':
    base = Base()
    base.base_open_url('http://127.0.0.1:8080/ecshop/user.php')

    base.base_send_keys(('name', 'username'), 'Zeus')
    sleep(1)
    base.base_send_keys(('name', 'password'), '123456')
    sleep(1)
    base.base_click(('name', 'submit'))

    base.quit(2)



