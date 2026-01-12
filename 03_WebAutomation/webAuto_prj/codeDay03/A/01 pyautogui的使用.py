import pyautogui
from codeDay03.A.common.open_web import *


driver = open_web(r'D:\MilkyWay\Self\Code\Python\03_WebAutomation\webAuto_prj\codeDay03\注册A.html')

pyautogui.scroll(-2000)     # 滚动，+向上  -向下
width, height = pyautogui.size()    # 获取window分辨率大小
print(width, height)
# 点击alert
print(1330/width, 1884/height)    # 0.4401041666666667 0.8518518518518519
pyautogui.moveTo(width * 0.41, height * 0.94, duration=1)
pyautogui.click()
# 点击确认
print(1900/width, 330/height)    # 0.615625 0.1925925925925926
pyautogui.moveTo(width * 0.59, height * 0.16, duration=1)
pyautogui.click()

sleep(1)
driver.quit()
