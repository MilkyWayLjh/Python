from codeDay05.common.open_web import *
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = open_web('https://www.jq22.com/yanshi23642')
# 切换frame
driver.switch_to.frame('iframe')
sleep(1)
# 鼠标按住位置
source = driver.find_element_by_css_selector('.slider-btn')
# 生成一个鼠标对象
action = ActionChains(driver)
# 按住鼠标左键
action.click_and_hold(source)
sleep(1)
# 鼠标偏移设置,并且释放,执行
action.move_by_offset(268, 0).release().perform()
# text = driver.find_element_by_class_name('layui-layer-content').text
# print(text)
text_toast = WebDriverWait(driver, 10, 0.3). \
    until(EC.presence_of_element_located((By.CLASS_NAME, "layui-layer-content"))).text

print(text_toast)

sleep(5)

# driver.quit()
