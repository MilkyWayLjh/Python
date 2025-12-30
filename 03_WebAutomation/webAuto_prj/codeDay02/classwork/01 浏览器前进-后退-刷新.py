from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
driver.maximize_window()

sleep(2)
driver.back()   # 后退
sleep(2)
driver.forward()    # 前进
sleep(2)
driver.refresh()    # 刷新

sleep(3)
driver.quit()


