"""
语法:
    操作事件是由Keys类提供,需要先导入
    from selenium.webdriver.common.keys import Keys
    方法介绍:
    send_keys(Keys.BACK_SPACE) 删除键（Backspace）
    send_keys(Keys.SPACE) 空格键（Space）
    send_keys(Keys.TAB) Tab键
    send_keys(Keys.ESCAPE) 回退键（Esc）
    send_keys(Keys.ENTER) 回车键（Enter）
    send_keys(Keys.CONTROL,'a') 全选（Ctrl+A）
    send_keys(Keys.CONTROL,'c') 复制（Ctrl+C）
    send_keys(Keys.CONTROL,'x') 剪切（Ctrl+X）
    send_keys(Keys.CONTROL,'v') 粘贴（Ctrl+V）
    sen_keys(Keys.UP)   键盘方向键向上
    sen_keys(Keys.DOWN) 键盘方向键向下
    send_keys(Keys.F1)  键盘F1
    send_keys(Keys.F12) 键盘F12

"""
from common.open_web import *
from selenium.webdriver.common.keys import Keys

driver = open_web()

# 在百度输入一句话
# driver.find_element_by_id('kw').send_keys('我命由我不由天')
# sleep(1)
# driver.find_element_by_id('kw').send_keys(Keys.BACK_SPACE)
# driver.find_element_by_id('kw').send_keys(Keys.BACK_SPACE)
# driver.find_element_by_id('kw').send_keys(Keys.BACK_SPACE)
# # 输入空格
# driver.find_element_by_id('kw').send_keys(Keys.SPACE)
# driver.find_element_by_id('kw').send_keys('不由天')

"""使用方向键操作百度搜索联想框"""
driver.find_element_by_id('kw').send_keys('web')
sleep(1)
driver.find_element_by_id('kw').send_keys(Keys.DOWN)
sleep(1)
driver.find_element_by_id('su').click()

sleep(2)
driver.quit()

