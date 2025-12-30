from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get('http://www.baidu.com')

# driver.maximize_window()
driver.set_window_size(600, 600)    # 自定义窗口大小, 单位是像素

sleep(3)
driver.quit()


