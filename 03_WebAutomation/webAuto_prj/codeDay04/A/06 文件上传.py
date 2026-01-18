from codeDay04.A.common.open_web import *
from selenium.webdriver.common.by import By
from os import path


file = path.abspath('../pages/example.html')
driver = open_web(file)

# 点击文件上传按钮
# driver.find_element(By.NAME, 'attach[]').send_keys(R'C:\Users\Administrator\Desktop\logwatch.exe')


def upload(by, el_path, file_path):
    driver.find_element(by, el_path).send_keys(file_path)


loc = (By.NAME, 'attach[]')
# upload(*loc, r'C:\Users\Administrator\Desktop\logwatch.exe')
# upload(*loc, path.abspath('../pages/example.html'))
# upload(*loc, '../pages/example.html')   # error：path is not absolute: ../pages/example.html

# filename = 'example.html'
filename = r'C:\Users\Administrator\Desktop\logwatch.exe'

if ':' not in filename:
    # 认为只输入文件名
    full_path = path.join(path.abspath('../pages'), filename)
    upload(*loc, full_path)
else:
    # 则认为输入绝对路径, 直接输入路径需要在路径前加 r
    upload(*loc, filename)
    for i in filename:
        print(i, end=' ')

sleep(1)
driver.quit()
