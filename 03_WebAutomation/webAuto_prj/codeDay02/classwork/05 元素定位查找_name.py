from open_web import open_web
from time import sleep

driver = open_web()

inp = driver.find_element_by_name('wd').get_attribute('outerHTML')
print('网页标签结构代码：', inp)

sleep(2)
driver.find_element_by_name('wd').send_keys('使用name定位')
sleep(1)
# driver.find_element_by_id('su').click()
driver.find_element_by_id('su').submit()    # 用于提交的方法，适用于标签存在属性 type='submit'

sleep(1)
driver.quit()

