from selenium import webdriver
from time import sleep

# 准备无头模式的配置对象
# 创建options对象
options = webdriver.ChromeOptions()
# 添加无头模式的参数
options.add_argument('-headless')
# 打开浏览器
driver = webdriver.Chrome(options=options)
# 请求目标网址
driver.get('https://www.baidu.com')

sleep(1)
# 输出当前页面的标题 和 URL
print("页面标题:", driver.title)     # 百度一下, 你就知道
print("当前 URL:", driver.current_url)    # https://www.baidu.com

# 退出浏览器
driver.quit()
