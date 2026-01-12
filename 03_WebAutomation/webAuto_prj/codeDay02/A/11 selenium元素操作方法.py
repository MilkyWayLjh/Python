"""
    selenium元素操作相关方法
        1. clear()            清除文本
            需要元素定位 (通过获取的元素来调用该方法)
        2. send_keys()        模拟输入
            需要元素定位 (通过获取的元素来调用该方法)
        3. click()            单击元素
            需要元素定位 (通过获取的元素来调用该方法)
            注：submit()       用于提交的方法，仅适用于标签存在属性 type='submit'
        4. size                 返回元素大小
            需要元素定位 (通过获取的元素来调用该属性)
        5. text                 获取元素的文本
            它是用来获取某个标签内的文本内容,获取的文本内容可用于测试结果验证
            它的使用要做元素定位 (通过获取的元素来调用该属性)
        6. title                 获取页面title
            不需要元素定位 (直接使用浏览器对象调用该属性)
        7. current_url            获取当前页面URL
            不需要元素定位 (直接使用浏览器对象调用该属性)
        8. get_attribute("属性名") 获取属性值;xxx：要获取的属性
            它是获取某个标签内对应的元素属性值
            它的需要使用元素定位 (通过获取的元素来调用该方法)
        9. is_displayed()            判断元素是否可见
            它得到的返回值是True或者False
            它需要使用元素定位 (通过获取的元素来调用该方法)
        10. is_enabled()            判断元素是否可用
            它得到的返回值是True或者False
            它需要使用元素定位 (通过获取的元素来调用该方法)

"""
from open_web import *

driver = open_web()

sleep(1)
driver.find_element(By.ID, 'chat-textarea').send_keys('1+1=')
sleep(1)

# """在做自动化时,每一次输入之前先做清空"""
driver.find_element(By.ID, 'chat-textarea').clear()
sleep(1)
# 获取元素大小
print(driver.find_element(By.ID, 'chat-textarea').size)

driver.find_element(By.ID, 'chat-textarea').send_keys('1+1=')
driver.find_element(By.ID, 'chat-submit-button').click()
sleep(2)

el = driver.find_element(By.CSS_SELECTOR, '#result')
print(el.text)
if el.text == '2':
    print('测试通过')
    print(el.get_attribute('outerHTML'))
    print(el.get_attribute('innerHTML'))
    print(el.get_attribute('id'))
    print(el.get_attribute('class'))
    print(el.get_attribute('style'))
else:
    print('测试失败')

print(driver.title)
print(driver.current_url)

sleep(1)

if driver.find_element(By.CSS_SELECTOR, '#result_logo > img.index-logo-src').is_displayed():
    print('元素可见')
else:
    print('元素不可见')

if driver.find_element(By.CSS_SELECTOR, '#result_logo > img.index-logo-src').is_enabled():
    print('元素可用')
else:
    print('元素不可用')

sleep(2)
driver.quit()
