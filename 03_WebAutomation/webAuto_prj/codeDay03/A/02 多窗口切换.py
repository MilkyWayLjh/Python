"""
    掌握:重点必须掌握
    概念:句柄是操作系统生成一种智能指针,当cpu需要切换到对不同的对象操作时,要用到句柄指向该对象
    语法:
        1.获取当前窗口句柄-->浏览器对象.current_window_handle
        2.获取所有窗口句柄-->浏览器对象.window_handles   注意获取的是一个列表
        3.切换句柄 -->浏览器对象.switch_to.window(窗口句柄名)
            如：driver.switch_to.window(浏览器对象.window_handles[下标])

    需求: 打开百度新闻窗口后,再回到百度首页输入切换窗口成功

"""
from codeDay03.A.common.open_web import *
from selenium.webdriver.common.by import By

driver = open_web()

driver.find_element(By.LINK_TEXT, '新闻').click()
print("第二个窗口句柄", driver.current_window_handle)
print("获取当前浏览器中打开的所有窗口句柄:", driver.window_handles)
# 切换句柄
driver.switch_to.window(driver.window_handles[1])
# driver.switch_to_window(driver.window_handles[1])  # 该方法在当前新版本中被废弃
sleep(2)
# 获取页面中第一个链接的文本内容
text = driver.find_element(By.CSS_SELECTOR, '#pane-news > div > ul > li.hdline0 > strong > a').text
print(text)

# 需求
sleep(2)
driver.switch_to.window(driver.window_handles[0])
sleep(1)
if driver.find_element(By.TAG_NAME, 'title').text == '百度一下，你就知道':
    print('切换成功')

sleep(1)
driver.close()
sleep(1)
driver.quit()
