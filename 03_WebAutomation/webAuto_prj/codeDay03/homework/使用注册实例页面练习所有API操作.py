# 使用注册实例.html练习所有API操作
from os import path
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

file_path = path.join(path.dirname(__file__), '注册实例.html')

driver = webdriver.Chrome()
driver.get(file_path)
driver.maximize_window()
sleep(1)

driver.find_element_by_id('user').send_keys('1234')
sleep(1)
driver.find_element_by_id('user').send_keys(Keys.BACK_SPACE)
sleep(1)
driver.find_element_by_id('password').send_keys('123456')
sleep(1)
driver.find_element_by_id('password').send_keys(Keys.SPACE)
driver.find_element_by_id('password').send_keys('789')
sleep(1)
driver.find_element_by_id('tel').send_keys('13312345678')
sleep(1)
driver.find_element_by_id('tel').send_keys(Keys.TAB)
sleep(1)
driver.find_element_by_id('email').send_keys('123456789@qq.com')
sleep(1)
driver.find_element_by_id('email').send_keys(Keys.CONTROL, 'a')
driver.find_element_by_id('email').send_keys(Keys.CONTROL, 'x')
sleep(1)
driver.find_element_by_id('email').send_keys(Keys.CONTROL, 'v')
sleep(1)
driver.find_element_by_id('email').send_keys(Keys.ENTER)
sleep(1)

ac = ActionChains(driver)
ac.click(driver.find_element_by_id('fw')).perform()
sleep(2)
driver.switch_to.window(driver.window_handles[0])

select = driver.find_element_by_css_selector('#select')
s = Select(select)
s.select_by_index(1)    # 上海
sleep(1)
s.select_by_value('gz')  # 广州
sleep(1)
s.select_by_visible_text('重庆')  # 重庆

sleep(1)
driver.execute_script("window.scrollTo(0, 1000)")

sleep(1)
driver.find_element_by_id('pg').click()
sleep(1)
driver.find_element_by_id('jz').click()

driver.find_element_by_css_selector('#qc').click()
sleep(1)
driver.find_element_by_css_selector('#gw').click()

js = "document.getElementById('yy').removeAttribute('disabled')"
driver.execute_script(js)
sleep(1)
driver.find_element_by_css_selector('#yy').click()

sleep(1)
driver.find_element_by_css_selector('#alert').click()
driver.switch_to.alert.accept()

sleep(1)
driver.find_element_by_css_selector('input[name="upfile"]').send_keys(file_path)

driver.switch_to.frame('idframe1')
sleep(1)
driver.find_element_by_id('userA').send_keys('1234')
sleep(1)
driver.find_element_by_id('userA').send_keys(Keys.BACK_SPACE)
sleep(1)

driver.switch_to.parent_frame()
driver.switch_to.frame('myframe2')
sleep(1)
driver.find_element_by_id('userB').send_keys('123456')
sleep(1)
driver.find_element_by_id('userB').send_keys(Keys.BACK_SPACE)
sleep(1)
driver.switch_to.default_content()
driver.find_element_by_link_text('hao123').click()
driver.find_element_by_link_text('淘宝').click()


sleep(2)
driver.quit()

