# 定位注册A页面的所有可操作元素
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.alert import Alert
from time import sleep


driver = webdriver.Chrome()
driver.get(r'D:\MilkyWay\Self\Code\Python\03_WebAutomation\webAuto_prj\codeDay02\B\注册A.html')
driver.maximize_window()

sleep(1)
# 注册 账号A
driver.find_element(By.ID, 'userA').send_keys('输入账号了')
# 密码A
driver.find_element(By.ID, 'passwordA').send_keys('输入密码了')
# 电话号码A
driver.find_element(By.ID, 'telA').send_keys('13312345678')
# 电子邮件A
driver.find_element(By.ID, 'emailA').send_keys('1331234567@qq.com')
# 注册用户A---button
driver.find_element(By.CSS_SELECTOR, 'button[value="注册A"]').click()
driver.back()

# Span_tagName
# 访问新浪
driver.find_element(By.LINK_TEXT, '访问 新浪 网站').click()
driver.back()
# AA 新浪
driver.find_element(By.LINK_TEXT, 'AA 新浪 网站').click()
driver.back()
# 我是a标签A
driver.find_element(By.CSS_SELECTOR, '#zc>fieldset>p:nth-of-type(9)>a').click()
driver.back()
# 退出
driver.find_element(By.LINK_TEXT, '退出').click()
driver.back()

# 下拉框
select = driver.find_element(By.ID, 'selectA')
select.click()
select_list = driver.find_elements(By.CSS_SELECTOR, '#selectA option')
for i in select_list:
    # print(i.get_attribute('outerHTML'))
    if 'bj' in i.get_attribute('outerHTML'):
        i.click()
        sleep(1)
    if 'sh' in i.get_attribute('outerHTML'):
        i.click()
        sleep(1)
    if 'gz' in i.get_attribute('outerHTML'):
        i.click()
        sleep(1)
    if 'cq' in i.get_attribute('outerHTML'):
        i.click()
        sleep(1)

# 使用Select类
s = Select(select)
s.select_by_index(1)    # 上海
sleep(1)
s.select_by_value('gz')  # 广州
sleep(1)
s.select_by_visible_text('A重庆')  # 重庆
sleep(1)


# 单选框
driver.find_element(By.CSS_SELECTOR, '#pga').click()
sleep(1)
driver.find_element(By.CSS_SELECTOR, '#jza').click()
sleep(1)
driver.find_element(By.CSS_SELECTOR, '#xja').click()
sleep(1)
driver.find_element(By.CSS_SELECTOR, '#lia').click()
sleep(1)
driver.find_element(By.CSS_SELECTOR, '#xga').click()


# 复选框
cb = driver.find_elements(By.CSS_SELECTOR, 'form input[type="checkbox"]')
for i in cb:
    if not i.is_selected():
        i.click()
sleep(1)
print(driver.find_element(By.CSS_SELECTOR, '#yyA').is_selected())
print(driver.find_element(By.CSS_SELECTOR, '#yyA').is_enabled())
print(driver.find_element(By.CSS_SELECTOR, '#cancelA').is_enabled())


# alert
driver.find_element(By.CSS_SELECTOR, '#alerta').click()
alert = driver.switch_to.alert
sleep(1)
alert.accept()

# 使用Alert类
sleep(1)
driver.execute_script('alert("测试alert对话框");')
alert = Alert(driver)
print(alert.text)
sleep(1)
alert.accept()

sleep(1)
# 滚动页面窗口
driver.execute_script('window.scrollTo(0, 2000);')
# 选择文件
driver.find_element(By.CSS_SELECTOR, 'input[name="upfilea"]').send_keys(r'C:\Users\Administrator\Desktop\media\A.gif')

sleep(1)
driver.quit()
