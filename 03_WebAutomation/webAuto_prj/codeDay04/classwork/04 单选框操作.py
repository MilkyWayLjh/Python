from os import path
from common.open_web import *

file_name = path.abspath('../pages/example.html')
driver = open_web(file_name)

# 将滚动条拖到底部
js = 'window.scrollTo(0,1000)'
driver.execute_script(js)
sleep(1)

driver.find_element_by_id('AliBaBa').click()


sleep(2)
driver.quit()
