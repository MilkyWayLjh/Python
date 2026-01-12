from common.open_web import *
from selenium.webdriver.common.by import By
from os import path


file_name = path.abspath('../pages/example.html')
driver = open_web(file_name)

# 点击文件上传按钮
driver.find_element(By.NAME, 'attach[]').send_keys(R'C:\Users\Administrator\Desktop\logwatch.exe')

sleep(2)
driver.quit()
