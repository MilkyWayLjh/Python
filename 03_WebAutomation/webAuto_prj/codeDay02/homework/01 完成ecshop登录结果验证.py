# 完成 ecshop 登录结果验证
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get('http://localhost:8080/ecshop/')
driver.maximize_window()

sleep(2)
driver.find_element_by_partial_link_text('登录').click()

sleep(1)
driver.find_element_by_name('username').clear()
driver.find_element_by_name('password').clear()
sleep(1)
driver.find_element_by_name('username').send_keys('Zeus')
driver.find_element_by_name('password').send_keys('123456')
driver.find_element_by_name('submit').click()

sleep(2)
username = driver.find_element_by_class_name('f4_b').text

print('用户名：', username)
if username == 'Zeus':
    print('登陆成功!')
else:
    print('登录有bug!')

sleep(2)
driver.quit()

