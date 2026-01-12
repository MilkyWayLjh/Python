"""
语法:
    1.复选框操作可以先定位一组元素,然后再进行遍历整个列表来操作每一个元素
        元素列表名 = driver.find_elements(定位器)
        通过for遍历列表,每个元素执行click()方法
    2.有条件的选择复选框,可以结合获取一组元素的下标索引值来进行判断,但是需要到enumerate()方法
        enumerate(对象名)可以用来获取序列当中元素值以及元素所对应的索引值
        for index,value in enumerate(对象名):	# enumerate列举/枚举
            index就是下标值
            value就是元素值
    3.单个元素定位进行点击
    4.将某个复选框选择之后取消的方法
        (1)对该选项进行定位重复的点击
        (2)使用pop(索引值)方法
            首先它必须在定位一组元素时才能用,否则无效
            元素列表对象.pop(索引值).click()
            如果取消第一个选项--pop(0)
            如果取消最后一个选项--pop()/pop(-1)

    5.判断某个复选框是否已被选中-->得到的一个布尔值
        定位元素.is_selected()

"""
from common.open_web import *
from selenium.webdriver.common.by import By
from os import path

file_name = path.abspath('../pages/example.html')
driver = open_web(file_name)

# 将滚动条拖到底部
js = 'window.scrollTo(0,1000)'
driver.execute_script(js)
sleep(1)

# 常规方法
# driver.find_element(By.NAME, 'checkbox1').click()
# 定位一组元素操作复选框

ele_list = driver.find_elements(By.CSS_SELECTOR, "div[id='checkbox']>input")

# 将复选框全部选中
"""有条件的筛选选择复选框"""
for index, value in enumerate(ele_list):
    if index == 0 or index == 3:
        value.click()
    else:
        continue

"""全部选中每个复选框"""
for i in ele_list:
    i.click()

"""选择之后取消某此选项"""
sleep(1)
ele_list.pop(-1).click()
sleep(1)
ele_list.pop(0).click()
sleep(1)

"""判断某条选择是否被选中"""
print(ele_list[0].is_selected())
print(ele_list[1].is_selected())


sleep(3)
driver.quit()
