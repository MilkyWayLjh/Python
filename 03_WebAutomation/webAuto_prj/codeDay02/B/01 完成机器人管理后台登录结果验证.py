# 完成 机器人管理后台 登录结果验证
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.get('https://tenantweb-pre.tongji.cq.cn:12080/systemMenu')
driver.maximize_window()


# 每次打开页面登录系统
sleep(1)
driver.find_element(By.CSS_SELECTOR, '#app > div > div > div.mg > button > span').click()

sleep(1)
driver.find_element(By.CSS_SELECTOR, '#LoginInput_UserNameOrEmailAddress').clear()
driver.find_element(By.CSS_SELECTOR, '#LoginInput_Password').clear()
sleep(1)
driver.find_element(By.CSS_SELECTOR, '#LoginInput_UserNameOrEmailAddress').send_keys('13219739608')
driver.find_element(By.CSS_SELECTOR, '#LoginInput_Password').send_keys('tjdx8888')
driver.find_element(By.CSS_SELECTOR, '#mobileForm > div.d-grid.gap-2 > button').click()
# driver.find_element(By.CSS_SELECTOR, '#mobileForm > div.d-grid.gap-2 > button').submit()

"""
'''使用cookie自动登录'''
sleep(30)
print(driver.get_cookies())
sleep(20)

# 将cookie信息保存
cookies = []    # 该网站浏览器前端无法获取登录cookie信息
# 再次打开浏览器进入网页
driver = webdriver.Chrome()
driver.get('https://tenantweb-pre.tongji.cq.cn:12080/systemMenu')
driver.maximize_window()
sleep(1)
# 删除所有cookie信息
driver.delete_all_cookies()
# 循环将cookies中的信息添加到浏览器cookie中
for i in cookies:
    driver.add_cookie(i)
sleep(1)
# 再次进入或直接刷新浏览器页面
# driver.get('https://tenantweb-pre.tongji.cq.cn:12080/systemMenu')
driver.refresh()
"""

'''获取并验证登录结果'''
sleep(1)
username = driver.find_element(By.CLASS_NAME, 'username').text

print('用户名：', username)
if username == '天青色等烟雨':
    print('登陆成功!')
else:
    print('登录有bug!')

sleep(1)
driver.find_element(
    By.CSS_SELECTOR, '#app > div > div.nav-container > div.app-content > div > div > div:nth-child(1) > div').click()
sleep(1)
system_name = driver.find_element(
    By.CSS_SELECTOR, '#app > div > div.menu-container > ul > div:nth-child(1) > div > div').text
print('机器人系统名称：', system_name)
if system_name == '清洁机器人管理后台':
    print('成功进入清洁机器人管理后台页面!')
else:
    print('系统进入错误!')

sleep(2)
driver.quit()
