from selenium import webdriver
from time import sleep
# 1、打开Chrome，打开百度首页
# 得到的是驱动对象实例
driver = webdriver.Chrome()
# 浏览器最大化
driver.maximize_window()

# 请求百度首页
# driver.get(网址)  请求目标网址
driver.get('https://www.baidu.com')

# 2、搜索框输入 天气预报，点击百度一下
# 通过id来获取标签, 得到的是标签对象
kw = driver.find_element_by_id('kw')
# 输入框输入内容
# kw.send_keys(要输入的内容)
kw.send_keys('天气预报')
# 通过id方式定位百度一下按钮,然后点击
driver.find_element_by_id('su').click()

# 3、等待2秒
sleep(2)

# 4、获取页面标题，并打印出来
# title = driver.title
print(driver.title)

# 5、检查’天气’关键字是否在标题中
# if title.find('hello') != -1:
#     print('存在')
# else:
#     print('不存在')
if '天气' in driver.title:
    print('存在')
else:
    print('不存在')

# 6、关闭Chrome浏览器
driver.quit()
