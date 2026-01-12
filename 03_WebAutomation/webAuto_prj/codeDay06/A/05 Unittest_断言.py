"""
断言方法
    在执行测试用例的过程中，最终用例是否执行通过，是通过判断测试得到的实际结果和预期结果是否相等决定的，这时会用到断言方法。

常用的断言方法：
    断言方法名称	        使用方法	                        验证
*   assertEqual()	    a,b,[msg='测试失败时打印的信息']	断言a和b是否相等，相等则测试用例通过
    assertNotEqual()	a,b,[msg='测试失败时打印的信息']	断言a和b是否相等，不相等则测试用例通过。
*   assertTrue()	    x,[msg='测试失败时打印的信息']	    断言x是否True，是True则测试用例通过
    assertFalse()	    x,[msg='测试失败时打印的信息']	    断言x是否false，是false则测试用例通过
"""
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get('http://127.0.0.1:8080/ecshop/user.php')
        self.driver.maximize_window()
        sleep(1)

    def test_login(self):
        self.driver.find_element(By.NAME, 'username').send_keys('Zeus')
        self.driver.find_element(By.NAME, 'password').send_keys('123456')
        self.driver.find_element(By.NAME, 'submit').click()
        sleep(1)
        username = self.driver.find_element(By.CLASS_NAME, 'f4_b').text
        self.assertEqual(username, 'Zeus', msg='两者不相等,登录失败')

    # def test_01(self):
    #     number = 1
    #     # number = 0
    #     self.assertTrue(number, msg='number is False!')


if __name__ == '__main__':
    unittest.main()
