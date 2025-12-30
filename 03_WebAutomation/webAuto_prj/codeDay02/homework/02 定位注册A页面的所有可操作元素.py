# 定位注册A页面的所有可操作元素,每个元素至少使用2种定位方法
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.get('file:///E:/AAMyDocument/%E8%BD%AF%E4%BB%B6%E6%B5%8B%E8%AF%95/0825%E6%B5%8B%E8%AF%95/09%20Web%E8%87%AA%E5%8A%A8%E5%8C%96/WebAuto_prj/codeDay02/pom_frame/%E6%B3%A8%E5%86%8CA.html')
driver.maximize_window()

sleep(1)
# 注册 账号A
# 1 xpath
# driver.find_element_by_xpath('//div[@id="zc"]/fieldset/p[1]/input').send_keys('输入账号了')
# 2 css
driver.find_element_by_css_selector('#p1 input').send_keys('输入账号了')

# 密码A
# 1 xpath
# driver.find_element_by_xpath('//div[@id="zc"]/fieldset/p[2]/input').send_keys('输入密码了')
# 2 css
driver.find_element_by_css_selector('div[id="zc"]>fieldset>p:nth-of-type(2)>input').send_keys('输入密码了')

# 电话号码A
# 1 xpath
# driver.find_element_by_xpath('//div[@id="zc"]/fieldset/p[3]/input').send_keys('13312345687')
# 2 css
driver.find_element_by_css_selector('div[id="zc"]>fieldset>p:nth-of-type(3)>input').send_keys('13312345678')

# 电子邮件A
# 1 xpath
# driver.find_element_by_xpath('//div[@id="zc"]/fieldset/p[4]/input').send_keys('1331234567@qq.com')
# 2 css
driver.find_element_by_css_selector('div[id="zc"]>fieldset>p:nth-of-type(4)>input').send_keys('1331234567@qq.com')

# 注册用户A
# 1 xpath
# driver.find_element_by_xpath('//div[@id="zc"]/fieldset/button[@type="submitA"]').click()
# 2 css
driver.find_element_by_css_selector('div[id="zc"]>fieldset>button[type="submitA"]').click()


# Span_tagName
# 访问新浪
# 1 xpath
# driver.find_element_by_xpath('//div[@id="zc"]/fieldset/p[6]/a[@id="fwA"]').click()
# 2 css
# driver.find_element_by_css_selector('#fwA').click()

# AA 新浪
# 1 xpath
# driver.find_element_by_xpath('//div[@id="zc"]/fieldset/p[7]/a[@id="AAA"]').click()
# 2 css
# driver.find_element_by_css_selector('#AAA').click()

# 我是a标签A
# 1 xpath
# driver.find_element_by_xpath('//div[@id="zc"]/fieldset/p[9]/a[contains(@href, "log")]').click()
# 2 css
# driver.find_element_by_css_selector('a[href="logout"]').click()
# driver.find_element_by_css_selector('div[id="zc"]>fieldset>p:nth-of-type(9)>a').click()

# 退出
# 1 xpath
# driver.find_element_by_xpath('//div[@id="zc"]/fieldset/p[10]/a').click()
# 2 css
# driver.find_element_by_css_selector('a[href*="taobao"]').click()


# 下拉框
# 1 xpath
# driver.find_element_by_xpath('//div[@id="zc"]/fieldset/p[11]/select').click()
# 2 css
select = driver.find_element_by_css_selector('#selectA')
select.click()
select_list = driver.find_elements_by_css_selector('#selectA option')
for i in select_list:
    # print(i.get_attribute('outerHTML'))
    if 'bj' in i.get_attribute('outerHTML'):
        i.click()
        sleep(1)
    if 'sh' in i.get_attribute('outerHTML'):
        i.click()
        sleep(1)
    if 'gz' in i.get_attribute('outerHTML'):
        i.click()
        sleep(1)
    if 'cq' in i.get_attribute('outerHTML'):
        i.click()
        sleep(1)
# s = Select(select)
# s.select_by_index(1)    # 上海
# sleep(1)
# s.select_by_value('gz')  # 广州
# sleep(1)
# s.select_by_visible_text('A重庆')  # 重庆


# 单选框
# 1 xpath
# driver.find_element_by_xpath('//div[@id="zc"]/fieldset/label[1]/input').click()
# sleep(1)
# driver.find_element_by_xpath('//div[@id="zc"]/fieldset/label[2]/input').click()
# sleep(1)
# driver.find_element_by_xpath('//div[@id="zc"]/fieldset/label[3]/input').click()
# sleep(1)
# driver.find_element_by_xpath('//div[@id="zc"]/fieldset/label[4]/input').click()
# sleep(1)
# driver.find_element_by_xpath('//div[@id="zc"]/fieldset/label[5]/input').click()
# 2 css
driver.find_element_by_css_selector('#pga').click()
sleep(1)
driver.find_element_by_css_selector('#jza').click()
sleep(1)
driver.find_element_by_css_selector('#xja').click()
sleep(1)
driver.find_element_by_css_selector('#lia').click()
sleep(1)
driver.find_element_by_css_selector('#xga').click()


# 复选框
# 1 xpath
# driver.find_element_by_xpath('//div[@id="zc"]/fieldset/form/input[1]').click()
# sleep(1)
# driver.find_element_by_xpath('//div[@id="zc"]/fieldset/form/input[2]').click()
# sleep(1)
# driver.find_element_by_xpath('//div[@id="zc"]/fieldset/form/input[3]').click()
# sleep(1)
# print(driver.find_element_by_xpath('//div[@id="zc"]/fieldset/form/input[4]').is_enabled())  # False 不可用
# print(driver.find_element_by_xpath('//div[@id="zc"]/fieldset/form/input[5]').is_enabled())  # False 不可用
# 2 css
driver.find_element_by_css_selector('#qcA').click()
sleep(1)
driver.find_element_by_css_selector('#gwA').click()
sleep(1)
driver.find_element_by_css_selector('#lyA').click()
sleep(1)
print(driver.find_element_by_css_selector('#yyA').is_enabled())
print(driver.find_element_by_css_selector('#cancelA').is_enabled())


# alert
# 1 xpath
# driver.find_element_by_xpath('//div[@id="zc"]/fieldset/form/input[6]').click()
# 2 css
driver.find_element_by_css_selector('#alerta').click()
# alert = driver.switch_to.alert
# alert.accept()
driver.switch_to.alert.accept()


# 选择文件
# 1 xpath
# driver.find_element_by_xpath('//div[@id="zc"]/fieldset/form/input[7]').send_keys('C:\\Users\\Administrator\\Desktop\\TODO.txt')
# 2 css
driver.find_element_by_css_selector('input[name="upfilea"]').send_keys('C:\\Users\\Administrator\\Desktop\\TODO.txt')

sleep(1)
driver.quit()


