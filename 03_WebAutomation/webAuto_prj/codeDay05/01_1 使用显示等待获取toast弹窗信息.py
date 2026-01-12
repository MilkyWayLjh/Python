from codeDay05.common.open_web import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


driver = open_web('https://www.jq22.com/yanshi23642')
# 切换frame
driver.switch_to.frame('iframe')
sleep(1)
# 鼠标按住位置
source = driver.find_element(By.CSS_SELECTOR, '.slider-btn')
# 生成一个鼠标对象
action = ActionChains(driver)
# 按住鼠标左键
action.click_and_hold(source)
sleep(1)
# 鼠标偏移设置,并且释放,执行
action.move_by_offset(270, 0).release().perform()

# action.drag_and_drop_by_offset(source, 268, 0).perform()

# text = driver.find_element(By.CLASS_NAME, 'layui-layer-content').text
# print(text)
toast = WebDriverWait(driver, 10, 0.3). \
    until(EC.presence_of_element_located((By.CLASS_NAME, "layui-layer-content")))

print(toast.text)

sleep(2)
driver.quit()
