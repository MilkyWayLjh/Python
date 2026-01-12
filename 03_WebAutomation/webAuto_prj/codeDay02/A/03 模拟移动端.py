from selenium import webdriver
import time

# 准备模拟浏览器移动端尺寸需要的配置信息
# 创建配置对象
options = webdriver.ChromeOptions()
# 添加配置项
options.add_experimental_option('mobileEmulation', {'deviceName': 'iPhone 14 Pro Max'})

# 打开浏览器
driver = webdriver.Chrome(options=options)

# 请求目标网址
driver.get('https://www.baidu.com')
time.sleep(2)

# 退出浏览器
driver.quit()
