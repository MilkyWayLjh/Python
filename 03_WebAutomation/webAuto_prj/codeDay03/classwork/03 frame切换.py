"""
掌握: 重点必须掌握
概念: frame是框架的意思,它是在一个网页中嵌套了其它网页,此时需要用到一个iframe/frame/frameset标签来定义
     以上三种情况中仅iframe和frame标签定义的网页需要用到frame的切换
为什么要切换frame:
    页面中的frame是隔离的,要想定位frame中的标签，必须切换到这个frame才能定位。
语法:
    查找进入frame的方法
        1.id切换frame
        2.name切换frame
        3.xpath切换frame
        浏览器对象.switch_to.frame(id属性值/name属性值/xpath路径表达式)
        或者
        浏览器对象.switch_to.frame(定位到的元素对象)
    退出frame的方法
        1.浏览器对象.switch_to.parent_frame()-->退出到上一层frame
        2.浏览器对象.switch_to.default_content()-->退出到最外层的frame

"""
from common.open_web import *
import pyautogui

driver = open_web('file:///E:/AAMyDocument/%E8%BD%AF%E4%BB%B6%E6%B5%8B%E8%AF%95/0825%E6%B5%8B%E8%AF%95/09%20Web%E8%87%AA%E5%8A%A8%E5%8C%96/WebAuto_res/code_res/%E7%BB%83%E4%B9%A0%E9%A1%B5%E9%9D%A2/%E6%B3%A8%E5%86%8C%E5%AE%9E%E4%BE%8B.html')

driver.find_element_by_id('user').send_keys('001')
sleep(1)
pyautogui.scroll(-1000)

# 在用户注册A页面输入之前,先要切换进入到对应的frame当中去
driver.switch_to.frame('idframe1')  # id切换frame
sleep(2)
driver.find_element_by_id('userA').send_keys('002')

# 退出当前frame,进入最外面的网页
# driver.switch_to.default_content()    #退出frame方法1
driver.switch_to.parent_frame()     # 退出frame方法2
# 进入到第二个frame
# driver.switch_to.frame('myframe2')
#   使用xpath时，需要先赋值给一个变量，再去使用
frame1 = driver.find_element_by_xpath('//iframe[@name="myframe2"]')
driver.switch_to.frame(frame1)
sleep(1)
driver.find_element_by_id('passwordB').send_keys('123456')
sleep(1)
# 退出到最外层页面
driver.switch_to.default_content()
driver.find_element_by_id('password').send_keys('123456')

sleep(2)
driver.quit()

