from open_web import *

driver = open_web()

sleep(1)

# 1 link_text   完整链接文本名称
# driver.find_element_by_link_text('新闻').click()

# 2 partial_link_text   部分链接文本名称
# driver.find_element_by_partial_link_text('新').click()
# driver.find_element_by_partial_link_text('图').click()   # 有地图、图片，默认第一个
driver.find_elements_by_partial_link_text('图')[1].click()   # find_elements列表第2个，elements_list[1]

sleep(2)
driver.quit()

