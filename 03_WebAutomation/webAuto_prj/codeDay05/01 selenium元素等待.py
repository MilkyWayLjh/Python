"""
掌握: 必须掌握
概念:
什么是元素等待:
    在自动化执行时由于网络和不同的硬件设备的影响导致元素的定位查找失败,
    为了提高脚本稳定性需要脚本中加入相应的元素等待方式.
    ( WebDriver定位页面元素时如果未找到，会在指定时间内一直等待的过程；
    为了保证脚本运行的稳定性，需要脚本中添加等待时间。)

为什么要设置元素等待:
    1.由于网络速度原因
    2.电脑配置原因
    3.服务器处理请求原因

等待方式:
非智能等待(强制等待)
    (1)sleep:它是执行sleep时当前进程所有内容全部停止,当到达了等待时间后再恢复苏醒
        sleep等待过程中不会有任何的报错抛出,也不会提前结束等待,效率较低

智能等待:
    (1)隐式等待--它不需要导包
        1.它是一个全局的等待方法,放置隐式等待下面的所有脚本(找元素的脚本)都会受到约束
        2.当等待元素在最大等待时内提前出现,此时它会结束本次等待,让脚本继续执行
        3.它等待最大的时间后仍然没有等待到该元素出现,它会抛出:NoSuchElementException
        语法:driver.implicitly_wait(时间)


    (2)显示等待--它需要导包 from selenium.webdriver.support.wait import WebDriverWait
        1.它只是对单一的元素进行等待
        2.它不仅是在等待,它还会主动地去找元素
        3.它还按照设定的频率去找
        4.当超过最大的等待时长以后,它会抛出:TimeOutException
        5.通常将显示等待用作断言,断言就是检查测试结果
        语法:
        (1)WebDriverWait(driver, timeout, poll_frequency=POLL_FREQUENCY, ignored_exceptions=None)
        driver:浏览器对象
        timeout:最大等待时间长
        poll_frequency:每次查找元素的时间间隔
        ignored_exceptions:找不到元素时,抛出一个指定的提醒信息,可选项

        (2)until(method, message='')
        method:将要等待的元素定位方式用一个函数来体现; 在等待期间，每隔一段时间调用这个传入的方法，直到返回True
        message:自定义的一种异常提醒信息; 如果超时，抛出TimeoutException，将message传入异常

        (3)until_not():它与until相反

        (4)EC模块
        该模块主要用来对页面元素是否存在进行判断,它需要搭配WebDriverWait和Until方法一起使用
        使用之前需要导入:
            from selenium.webdriver.support import expected_conditions as EC


"""
from codeDay05.common.open_web import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# driver = open_web('https://www.baidu.com')
#
# driver.implicitly_wait(5)
# driver.find_element_by_id('chat-textarea').send_keys('123')
# driver.find_element_by_id('chat-submit-button').click()
# driver.quit()

"""使用EC模块来实现显示等待"""
driver = open_web('https://www.baidu.com')

# locator为一个(by, path)元祖，这个(by, path)的by是Selenium的一个类(selenium.webdriver.common.by.By), path为元素的定位路径
# 包括CLASS_NAME，CSS_SELECTOR，ID，LINK_TEXT，NAME，PARTIAL_LINK_TEXT，TAG_NAME和XPATH，和我们元素定位中使用的方法相同
locator = (By.ID, 'chat-textarea')

print(EC.visibility_of_element_located(locator))

try:
    result = WebDriverWait(driver, 5, 0.5).until(
        EC.element_to_be_clickable(locator), message='没有找到该元素')  # locator一定是元组格式
    if result is not None:
        result.send_keys('1223')
except:
    print('该元素不存在')

sleep(2)
driver.quit()
