"""
    selenium元素操作相关方法
        1. clear()            清除文本
            需要元素定位
        2. send_keys()        模拟输入
            需要元素定位
        3. click()            单击元素
            需要元素定位
        4. size                 返回元素大小
            需要元素定位
        5. text                 获取元素的文本
            它是用来获取某个标签内的文本内容,获取的文本内容可用于测试结果验证
            它的使用要做元素定位
        6. title                 获取页面title
            不需要元素定位
        7. current_url            获取当前页面URL
            不需要元素定位
        8. get_attribute("属性名") 获取属性值;xxx：要获取的属性
            它是获取某个标签内对应的元素属性值
            它的需要使用元素定位
        9. is_displayed()            判断元素是否可见
            它的得到的返回值是True或者False
            它需要使用元素定位
        10. is_enabled()            判断元素是否可用
            它的得到的返回值是True或者False
            它需要使用元素定位

"""
from open_web import *

# driver = open_web('http://www.baidu.com')
# sleep(2)
# driver.find_element_by_id('kw').send_keys('输入一句话')
# sleep(1)
#
# """在做自动化时,每一次输入之前先做清空"""
# driver.find_element_by_id('kw').clear()

# 获取元素大小
# print(driver.find_element_by_id('kw').size)

driver = open_web('http://localhost:8080/ecshop/user.php')
sleep(2)
print(driver.find_element_by_name('username').is_displayed())
# 输入账号
driver.find_element_by_name('username').send_keys('itsource')
sleep(1)
driver.find_element_by_name('password').send_keys('qlc123456')
sleep(1)
driver.find_element_by_name('submit').click()
sleep(2)
# 获取登录用户名
user_name = driver.find_element_by_class_name('f4_b').text
values = driver.find_element_by_class_name('f4_b').get_attribute('class')
print("属性值:", values)

# 获取当前窗口的url地址
print(driver.current_url)

print(user_name)
if user_name == 'itsource':
    print('登录成功')
else:
    print('登录有bug')

sleep(5)
driver.quit()

