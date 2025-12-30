# 使用163邮箱/QQ邮箱发邮件
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get('https://mail.163.com/')
driver.maximize_window()
sleep(1)

# 登录
frame_element = driver.find_element_by_xpath('//iframe[contains(@id, "x-URS-iframe")]')
driver.switch_to.frame(frame_element)
sleep(1)
driver.find_element_by_name('email').send_keys('Lijh_zeus')
sleep(1)
driver.find_element_by_name('password').send_keys('Ljh19991029')
sleep(1)
driver.find_element_by_id('dologin').click()
sleep(2)

# 获取并点击'写信'元素
driver.find_element_by_css_selector('#_mail_component_74_74 .oz0').click()
sleep(1)
# 输入收件人和主题信息
driver.find_element_by_class_name('nui-editableAddr-ipt').send_keys('1712240212@qq.com')
sleep(1)
path1 = '/html/body/div[2]/div[1]/div[2]/div[1]/section/header/div[2]/div[1]/div/div/input'
driver.find_element_by_xpath(path1).send_keys('测试发邮件')
sleep(1)

# 切换frame 输入内容
frame = driver.find_element_by_class_name('APP-editor-iframe')
driver.switch_to.frame(frame)
driver.find_element_by_xpath('/html/body/p').send_keys('你好世界！')
driver.switch_to.default_content()
sleep(1)

# 添加附件
path2 = '/html/body/div[2]/div[1]/div/div[1]/section/header/div[3]/div[1]/div[2]/input'
driver.find_element_by_xpath(path2).send_keys(r'C:\Users\Administrator\Desktop\document\web自动化测试面试题.md')
sleep(1)
# 点击发送
driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[1]/section/footer/div[1]/span[2]').click()


sleep(3)
driver.quit()

