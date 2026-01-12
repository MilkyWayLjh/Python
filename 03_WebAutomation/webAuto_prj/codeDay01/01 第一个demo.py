from selenium import webdriver
from time import sleep
# from selenium.webdriver.chrome.service import Service as ChromeService

driver = webdriver.Chrome()
# service = ChromeService(executable_path="D:\ProgramData\Python\Python310\Scripts\chromedriver.exe")
# options = webdriver.ChromeOptions()
# driver = webdriver.Chrome(service=service, options=options)

driver.get('https://www.baidu.com/')
driver.maximize_window()
# driver.set_window_size(600, 600)    # 自定义窗口大小, 单位是像素

sleep(1)
driver.quit()
