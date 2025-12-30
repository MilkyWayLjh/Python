from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
driver.maximize_window()
# 截图
driver.save_screenshot('./img1.png')    # 需要加上具体图片的路径及文件名
sleep(3)
driver.quit()

