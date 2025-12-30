from selenium import webdriver
from time import sleep

# driver = webdriver.Edge()
driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
driver.maximize_window()
sleep(3)

# 使用js脚本编写新建浏览器窗口
js_script = "window.open('https://www.bilibili.com')"
driver.execute_script(js_script)

# 点击新闻超链接
# 定位新闻标签，然后点击
# driver.find_element_by_link_text('新闻').click()
sleep(3)

driver.close()    # 关闭 驱动对象.get()打开的tab窗口
# driver.quit()   # 关闭退出整个浏览器


