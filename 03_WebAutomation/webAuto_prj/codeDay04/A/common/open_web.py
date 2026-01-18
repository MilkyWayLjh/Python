from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from time import sleep


def open_web(url='https://www.baidu.com'):
    # driver = webdriver.Chrome()
    options = webdriver.ChromeOptions()
    service = ChromeService(executable_path=r"D:\ProgramData\Python\Python310\Scripts\chromedriver.exe")
    driver = webdriver.Chrome(options=options, service=service)

    driver.get(url)
    driver.maximize_window()
    sleep(1)
    return driver


if __name__ == '__main__':
    my_driver = open_web()
    my_driver.quit()
