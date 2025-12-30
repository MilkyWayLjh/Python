from open_web import *

driver = open_web()

sleep(1)
# elements_list = driver.find_element_by_tag_name('input').send_keys('tag_name定位')    # input有很多，默认第一个，所以定位不到
elements_list = driver.find_elements_by_tag_name('input')   # 使用find_elements查找所有匹配到的元素，会形成对象的列表
print(elements_list)
print(len(elements_list))

for i in elements_list:
    # print(i.get_attribute('outerHTML'))
    # print(type(i.get_attribute('outerHTML')))
    if 'id="kw"' in i.get_attribute('outerHTML'):
        i.send_keys('tag_name定位')
    if 'id="su"' in i.get_attribute('outerHTML'):
        i.click()
        break

sleep(2)
driver.quit()

