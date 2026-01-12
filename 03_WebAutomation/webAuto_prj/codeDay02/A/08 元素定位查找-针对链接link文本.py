from open_web import *

driver = open_web()

sleep(1)

# 1 link_text   完整链接文本名称
driver.find_element(By.LINK_TEXT, '新闻').click()
sleep(1)

# 2 partial_link_text   部分链接文本名称
driver.find_element(By.PARTIAL_LINK_TEXT, '新').click()
sleep(1)
print(driver.find_elements(By.PARTIAL_LINK_TEXT, '图'))   # 有地图、图片
sleep(1)
driver.find_elements(By.PARTIAL_LINK_TEXT, '图')[1].click()   # find_elements列表第2个，elements_list[1]

sleep(2)
driver.quit()
