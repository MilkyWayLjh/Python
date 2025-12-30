from common.open_web import *
from os import path

file_name = path.abspath('../pages/example.html')
driver = open_web(file_name)

# 点击文件上传按钮
driver.find_element_by_name('attach[]').send_keys(R'C:\Users\Administrator\Desktop\document\web自动化测试面试题.md')

sleep(3)
driver.quit()

