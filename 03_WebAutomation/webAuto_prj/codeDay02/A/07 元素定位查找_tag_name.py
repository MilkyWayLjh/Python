from open_web import *

driver = open_web()

sleep(1)
elements_list = driver.find_elements(By.TAG_NAME, 'span')   # 使用find_elements查找所有匹配到的元素，会形成对象的列表
print(elements_list)
print(len(elements_list))

for i in elements_list:
    print(i.get_attribute('outerHTML'))
    print(type(i.get_attribute('outerHTML')))
    if 'class="title-content-title"' in i.get_attribute('outerHTML'):
        i.click()
        break

sleep(2)
driver.quit()
