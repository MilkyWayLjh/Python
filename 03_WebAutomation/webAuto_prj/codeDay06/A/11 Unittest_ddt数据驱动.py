"""
ddt
1.ddt它是一个数据驱动测试模块,需要单独下载:pip install ddt
2.它包含3个部分:ddt,data,unpack
    @ddt:在类上面声明使用ddt数据驱动
    @data:在类的方法中进行参数传递的,data中的每一组参数是用','隔开
        如果data()中传入一个多值的对象,此时需要在对象的前面加"*"
            @data(*csv_data)
    @unpack:针对方法中有多个形参需要传递参数时,它进行分配
        在unpack分配时它可对列表/元组/字典格式数据进行分配
        方法有多少个形参,对应的data就应该有相等的元素个数
        在data中每一组数据可以单独列表或者元组来进行存放
3.ddt的数据驱动要结合unittest使用才可以有效果

"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import unittest
from ddt import ddt, data, unpack
from codeDay06.pom_frame.common.data_operation import DataOperation

do = DataOperation("login_data.csv")
csv_data = do.common_get_data_to_list()  # 二维列表


@ddt  # 声明当前要使用ddt数据驱动
class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get('http://127.0.0.1:8080/ecshop/user.php')
        self.driver.maximize_window()
        sleep(1)

    @data(*csv_data)  # 它是用来给方法传递参数的
    @unpack  # 分配参数
    def test_input(self, message, pwd):
        # print(message)
        print(message, pwd)
        self.driver.find_element(By.NAME, 'username').send_keys(message)
        self.driver.find_element(By.NAME, 'password').send_keys(pwd)
        self.driver.find_element(By.NAME, 'submit').click()
        sleep(2)


if __name__ == '__main__':
    unittest.main()
