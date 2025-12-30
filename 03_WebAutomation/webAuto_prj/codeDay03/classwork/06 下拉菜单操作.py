"""
掌握:需要掌握
概念:web页面中面对下拉菜,一般是通过元素定位后再进行操作即可,但是selenium的API中提供的专用方法
    这些方法由Select类提供
语法:
    引入Select
    from selenium.webdriver.support.select import Select
    使用步骤:
    1.生成select对象
     对象名 = Select(element)
    2.使用value属性进行下拉菜单的选择
     对象名.select_by_value("value属性值")
    3.使用index索引进行下拉菜单的选择
     对象名.select_by_index(索引值)-->索引值是从0开始计算
    4.使用标签内的文本进行选择
     对象名.select_by_visible_text("标签内文本内容")
    注意: 2,3,4步骤只需要选择一种使用即可
"""
from common.open_web import *
from selenium.webdriver.support.select import Select
from os import path

# 获取顶级目录
# path.dirname(__file__)获取当前文件所在的上一层目录
dir_name = path.dirname(path.dirname(__file__))
# 生成文件全路径
file_path = path.join(dir_name, 'example.html')
driver = open_web(file_path)

# Select(webelement)
select = Select(driver.find_element_by_id('Selector'))
# select.select_by_value('banana')
# select.select_by_index(1)
select.select_by_visible_text('芒果')
sleep(2)
driver.quit()


