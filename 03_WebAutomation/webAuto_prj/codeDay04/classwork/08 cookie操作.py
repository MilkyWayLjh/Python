"""
学习目标:掌握
概念:
    1.cookie:它是一小段文本，是由软件系统的服务器产生，并保存浏览器上的。它的主要作用是用来
    进行身份验证（鉴权），可以将cookie理解为身份证，有了身份证就可以免登录了
    2.cookie一般是由登录所产生的
语法(操作):
    driver.get_cookies()            获得所有cookie 信息,是以列表的形式进行获取
    driver.get_cookie(name)         返回特定name 有cookie 信息
    driver.add_cookie(cookie_dict)  添加cookie，必须有name 和value 值
    driver.delete_cookie(name)      删除特定(部分)的cookie 信息
    driver.delete_all_cookies()     删除所有cookie 信息
"""
from common.open_web import *

driver = open_web()

print("原有的:", driver.get_cookies())
cookie = driver.get_cookie('BAIDUID_BFESS')
print(cookie)

# for i in driver.get_cookies():
#     driver.add_cookie(i)
#
# print("添加之后的:",driver.get_cookies())

driver.delete_all_cookies()
print(driver.get_cookies())

sleep(2)
driver.quit()
