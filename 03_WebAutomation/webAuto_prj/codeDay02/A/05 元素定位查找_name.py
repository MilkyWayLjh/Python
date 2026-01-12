from open_web import open_web
from selenium.webdriver.common.by import By
from time import sleep

driver = open_web()

inp = driver.find_element(By.NAME, 'description').get_attribute('outerHTML')
print('网页标签结构代码：', inp)

# sleep(1)
# driver.find_element(By.ID, 'chat-submit-button').click()
# driver.find_element(By.ID, 'chat-submit-button').submit()    # 用于提交的方法，适用于标签存在属性 type='submit'

sleep(1)
driver.quit()
