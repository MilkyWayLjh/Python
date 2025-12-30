"""
find_element: 定位匹配到的第一个元素,如果没有匹配到会抛出错误
find_elements: 定位匹配到的所有元素,返回一个列表.匹配不到,返回空列表
"""
from open_web import open_web
from time import sleep
from selenium.webdriver.common.by import By

driver = open_web()

# inp = driver.find_element_by_id('kw').get_attribute('outerHTML')
# inp = driver.find_element('id', 'kw').get_attribute('outerHTML')
inp = driver.find_element(By.ID, 'kw').get_attribute('outerHTML')
print('网页标签结构代码：', inp)
print('浏览器查找元素对象：', driver.find_element_by_id('kw'))

sleep(2)
driver.find_element_by_id('kw').send_keys('使用id定位')
sleep(1)
driver.find_element_by_id('su').click()

sleep(1)
driver.quit()


