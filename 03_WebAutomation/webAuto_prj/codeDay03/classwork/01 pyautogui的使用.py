import pyautogui
from common.open_web import *

driver = open_web('file:///E:/AAMyDocument/%E8%BD%AF%E4%BB%B6%E6%B5%8B%E8%AF%95/0825%E6%B5%8B%E8%AF%95/09%20Web%E8%87%AA%E5%8A%A8%E5%8C%96/WebAuto_prj/codeDay02/pom_frame/%E6%B3%A8%E5%86%8CA.html')

pyautogui.scroll(-2000)     # 滚动，+向上  -向下
width, height = pyautogui.size()    # 获取window分辨率大小
print(width, height)
# 点击alert
print(845/width, 920/height)    # 0.4401041666666667 0.8518518518518519
pyautogui.moveTo(width * 0.44, height * 0.85, duration=1)
pyautogui.click()
# 点击确认
print(1182/width, 208/height)    # 0.615625 0.1925925925925926
pyautogui.moveTo(width * 0.62, height * 0.19, duration=1)
pyautogui.click()

sleep(1)
driver.quit()

