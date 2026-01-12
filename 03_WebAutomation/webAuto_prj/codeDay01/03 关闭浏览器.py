from selenium import webdriver
from time import sleep

# driver = webdriver.Edge()
driver = webdriver.Chrome()
driver.get('https://www.baidu.com')
driver.maximize_window()
sleep(1)

# 使用js脚本编写新建浏览器窗口
js_script = "window.open('https://www.bilibili.com')"
driver.execute_script(js_script)

# 点击新闻超链接
# 定位新闻标签，然后点击
# driver.find_element_by_link_text('新闻').click()
sleep(1)

driver.close()    # 关闭tab标签页 驱动对象.get()打开的tab窗口(因为没有切换到新窗口，所以关闭的是之前的窗口)
sleep(2)
driver.quit()   # 关闭退出整个浏览器
