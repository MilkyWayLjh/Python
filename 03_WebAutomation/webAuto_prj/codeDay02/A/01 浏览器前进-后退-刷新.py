from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.baidu.com')
sleep(1)
# 导航到另一个页面
driver.get("https://www.runoob.com")

driver.back()   # 后退
sleep(1)
driver.forward()    # 前进
sleep(1)
driver.refresh()    # 刷新

sleep(2)
driver.quit()
