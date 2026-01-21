from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep


class Base:
    # 初始化方法，打开浏览器, 设置driver
    def __init__(self, browser='chrome'):
        if browser.lower() == 'chrome':
            self.driver = webdriver.Chrome()
        elif browser.lower() == 'edge':
            self.driver = webdriver.Edge()
        elif browser.lower() == 'firefox':
            self.driver = webdriver.Firefox()
        else:
            print('不支持该浏览器')
            self.driver = None

    # 请求目标网址
    def base_open_url(self, url):
        # 有需求可以区分环境 production environment/Pre-release environment
        self.driver.get(url)
        self.driver.maximize_window()

    # 定位单个元素
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

    # 定位多个元素
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

    # 点击操作
    def base_click(self, locator):
        self.base_find_element(locator).click()

    # 写入内容
    def base_send_keys(self, locator, content):
        self.base_find_element(locator).send_keys(content)

    # 清空文本操作
    def base_clear(self, locator):
        element = self.base_find_element(locator)
        if element:
            element.clear()

    # 获取文本内容
    def base_get_text(self, locator):
        return self.base_find_element(locator).text

    # 获取元素属性，默认获取元素标签结构
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

    # 下拉框操作 method输入1:索引 2:value值 3:文本
    def base_get_select(self, locator, method, values):
        select = Select(self.base_find_element(locator))
        if select:
            if method == 1:
                select.select_by_index(values)
            elif method == 2:
                select.select_by_value(values)
            elif method == 3:
                select.select_by_visible_text(values)
            else:
                print('没有此方法')

    # 获取警告框文本
    def base_get_alert_text(self):
        alert = self.driver.switch_to.alert
        text = alert.text
        alert.accept()
        return text

    # toast弹窗文本获取
    def base_get_toast_text(self, locator):
        return WebDriverWait(self.driver, 5, 0.2).until(EC.presence_of_element_located(locator)).text

    # 滚动条到浏览器的最底部
    def base_scroll(self):
        js = 'window.scrollTo(0, document.body.scrollHeight)'
        self.driver.execute_script(js)

    # 滚动条到浏览器的最顶部
    def base_scroll_top(self):
        js = 'window.scrollTo(0, 0)'
        self.driver.execute_script(js)

    # 聚焦到某个元素位置
    def base_focus(self, locator):
        js = "arguments[0].scrollIntoView()"
        target = self.base_find_element(locator)
        self.driver.execute_script(js, target)

    # 关闭当前窗口
    def close(self, seconds=0):
        sleep(seconds)
        self.driver.close()

    # 关闭浏览器对象
    def quit(self, seconds=0):
        sleep(seconds)
        self.driver.quit()


if __name__ == '__main__':
    base = Base()
    # base.base_open_url('http://127.0.0.1:8080/ecshop/user.php')

    # base.base_send_keys((By.NAME, 'username'), 'Zeus')
    # sleep(1)
    # base.base_send_keys(('name', 'password'), '123456')
    # sleep(1)
    # base.base_click(('name', 'submit'))

    # base.quit(2)

    # base.base_open_url('http://localhost:8080/ecshop/user.php?act=register')
    # base.base_get_select((By.NAME, 'sel_question'), 1, 1)
    # base.base_scroll()
    # sleep(1)
    # base.base_scroll_top()
    # sleep(1)
    # base.base_focus((By.NAME, 'sel_question'))
    # base.quit(2)

    base.base_open_url('https://www.jq22.com/yanshi23642')

    base.driver.switch_to.frame('iframe')
    source = base.driver.find_element_by_css_selector('.slider-btn')
    action = ActionChains(base.driver)
    action.click_and_hold(source)
    action.move_by_offset(270, 0).release().perform()

    print(base.base_get_toast_text((By.CLASS_NAME, "layui-layer-content")))

    base.quit(2)
