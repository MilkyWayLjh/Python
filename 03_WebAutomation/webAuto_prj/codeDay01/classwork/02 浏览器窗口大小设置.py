from selenium import webdriver
import time

# 打开浏览器
driver = webdriver.Chrome()

# 访问目标网址
driver.get('https://www.baidu.com')
time.sleep(1)

# 设置浏览器最大化
driver.maximize_window()
time.sleep(1)

# 设置浏览器固定大小 500 * 800
driver.set_window_size(500, 800)
time.sleep(1)

# 设置浏览器最小化
driver.minimize_window()
time.sleep(2)

# 退出浏览器
driver.quit()
