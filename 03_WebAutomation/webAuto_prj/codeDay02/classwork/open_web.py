from selenium import webdriver
from time import sleep


def open_web(url='https://www.baidu.com'):
    driver = webdriver.Chrome()
    driver.get(url)
    driver.maximize_window()
    return driver

if __name__ == '__main__':
    my_driver = open_web()
    my_driver.quit()
