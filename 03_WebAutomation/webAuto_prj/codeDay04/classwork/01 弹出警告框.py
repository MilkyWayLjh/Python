"""
webdriver中处理JavaScript所生成的alert、confirm以及prompt是很简单的。
    具体思路是使用driver.switch_to.alert方法定位到alert/confirm/prompt。
    然后使用text/accept()/dismiss()/send_keys() 按需进行操做。

text       返回alert/confirm/prompt 中的文字信息。
accept()     点击确认按钮。
dismiss()    点击取消按钮，如果有的话。
send_keys()  输入值，这个alert/confirm没有对话框就不能用了，不然会报错。

alert:有弹出框,确认按钮,文本提示信息
prompt:有弹出框,确认按钮,取消按钮,有输入框,文本提示信息
confirm:有弹出框,确认按钮,取消按钮,文本提示信息,操作结果提示
"""
from common.open_web import *
from os import path

file_path = path.join(path.abspath('../pages'), 'example.html')
driver = open_web(file_path)

# 1 alert弹出框
driver.find_element_by_name('alterbutton').click()
text = driver.switch_to.alert.text
print(text)
if text == '测试alert对话框':
    print('alert框正常弹出,文本内容提示正确')
    sleep(1)
    driver.switch_to.alert.accept()


sleep(1)
# 2 prompt弹出框
driver.find_element_by_name('promptbutton').click()
sleep(1)
driver.switch_to.alert.send_keys('测试prompt对话框')
sleep(1)
driver.switch_to.alert.accept()
text2 = driver.switch_to.alert.text
if text2 == '测试prompt对话框':
    print('显示结果与输入内容一致,测试结果正确')
    sleep(1)
    driver.switch_to.alert.accept()


sleep(1)
# 3 confirm弹出框
driver.find_element_by_name('confirmbutton').click()
sleep(1)
text3 = driver.switch_to.alert.text
print(text3)
if text3 == '测试confirm对话框':
    driver.switch_to.alert.accept()
    sleep(1)
    text4 = driver.switch_to.alert.text
    if text4 == 'You pressed OK!':
        print('以上显示的文本内容均正确')
        sleep(1)
        driver.switch_to.alert.accept()

sleep(1)
driver.find_element_by_name('confirmbutton').click()
sleep(1)
if text3 == '测试confirm对话框':
    driver.switch_to.alert.dismiss()
    sleep(1)
    text5 = driver.switch_to.alert.text
    if text5 == "You pressed Cancel!":
        print('以上文本显示均正确')
        sleep(1)
        driver.switch_to.alert.accept()


sleep(2)
driver.quit()

