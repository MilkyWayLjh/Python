# from open_web import open_web
from open_web import *

driver = open_web()

sleep(2)
driver.find_element_by_class_name('s_ipt').send_keys('使用class_name定位')
sleep(1)
driver.find_element_by_class_name('s_btn').click()
print(driver.find_element_by_class_name('bg').get_attribute('outerHTML'))

sleep(2)
driver.quit()

"""
    1.浏览器对象.find_element_by_class_name("class属性值")
    2.HTML文档中当一个class属性有多个值,是以" "空格隔开,
        使用class_name定位只能选择其中一个class来使用
    3.不论使用何种定位方式,都必须保证元素的唯一性
"""
