"""
js操作时间控件介绍:
在进行ui自动化如果一个时间输入框,无法通过send_keys()直接输入一个时间值,请问如何处理才能将时间正确的写入进去
答:  因为加了readonly属性,需使用js通过修改属性来写入时间值
js = "document.getElementById('id属性值').value("时间值")"

"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


driver = webdriver.Chrome()
driver.get('http://172.16.20.203:8080/crm')     # 已失效，直接看44行
driver.maximize_window()
sleep(2)
driver.find_element(By.ID, 'userNum').send_keys('admin')
driver.find_element(By.NAME, 'userPw').send_keys('123456')
driver.find_element(By.ID, 'in1').submit()

sleep(2)
# 切换frame   /html/frameset/frameset/frame[1]
frame1 = driver.find_element(By.XPATH, '/html/frameset/frameset/frame[1]')
driver.switch_to.frame(frame1)
sleep(2)
# 点击"客户信息”按纽
driver.find_element(By.PARTIAL_LINK_TEXT, '信息').click()
sleep(2)
# 再次切换frame--但要先退出当前frame
driver.switch_to.parent_frame()
frame2 = driver.find_element(By.XPATH, '/html/frameset/frameset/frame[2]')

driver.switch_to.frame(frame2)
# 点击“添加”按纽
driver.find_element(By.CSS_SELECTOR, 'input[type="button"][value="添加"]').click()
sleep(2)

# 在出生日期栏输入日期
# 输入姓名
driver.find_element(By.NAME, 'customerName').send_keys('小朋友')
sleep(1)
# driver.find_element_by_name('customerBirthday').send_keys('2022-11-14 11:11:11')

# js操作时间控件 将时间正确的写入进去
time_js = "document.getElementsByName('customerBirthday')[0].value='2022-11-25 18:46:15'"
driver.execute_script(time_js)

sleep(2)
driver.quit()
