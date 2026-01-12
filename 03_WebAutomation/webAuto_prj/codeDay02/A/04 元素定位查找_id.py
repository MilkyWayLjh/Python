"""
find_element: 定位匹配到的第一个元素,如果没有匹配到会抛出错误
find_elements: 定位匹配到的所有元素,返回一个列表.匹配不到,返回空列表
"""
from open_web import open_web
from selenium.webdriver.common.by import By
from time import sleep

driver = open_web()

inp = driver.find_element(By.ID, 'chat-textarea').get_attribute('outerHTML')
print('网页标签结构代码：', inp)
print('浏览器查找元素对象：', driver.find_element(By.ID, 'chat-textarea'))

sleep(1)
driver.find_element(By.ID, 'chat-textarea').send_keys('使用id定位')
sleep(1)
driver.find_element(By.ID, 'chat-submit-button').click()

sleep(2)
driver.quit()
