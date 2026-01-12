from common.open_web import *
from selenium.webdriver.common.by import By
from os import path

# 获取目录 绝对路径,根据当前脚本文件为参照的路径
dir_name = path.abspath('../../codeDay03')
print(dir_name)
# print(path.abspath(__file__))
# 生成文件全路径
file_path = path.join(dir_name, 'example.html')
print(file_path)

driver = open_web(file_path)

# 滚动条到浏览器的最底部
js1 = 'window.scrollTo(0, document.body.scrollHeight)'
driver.execute_script(js1)
sleep(1)

js = "window.scrollTo(0, 1000)"
driver.execute_script(js)
sleep(1)

js11 = 'window.scrollTo({top:document.body.scrollHeight, left:0, behavior:"smooth"})'
driver.execute_script(js11)
sleep(1)

# 滚动条到浏览器的最顶部
js2 = 'window.scrollTo(0, 0)'
driver.execute_script(js2)
sleep(1)

# 聚焦到某个元素位置
js = "arguments[0].scrollIntoView();"
target = driver.find_element(By.ID, 'edit')
driver.execute_script(js, target)

sleep(2)
driver.quit()
