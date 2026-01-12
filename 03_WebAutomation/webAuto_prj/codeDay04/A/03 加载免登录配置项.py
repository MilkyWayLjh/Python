"""
概念:某些有名登录设置,但是自动化用例执行时无法直接使用此设置结果的,需要修改自动化浏览器启动的选项配置
语法:
    步骤:
    1.先要手动进行免登录的操作--让浏览器记录30天免登录的配置(自动化脚本运行的哪个浏览,此步骤必须选择同一种浏览器操作)
    2.查找浏览器安装路径中的个人资源路径-->在浏览器url地址栏中输入  chrome://version
    3.设置用户数据目录
        路径变量 = "--user-data-dir=C:\\Users\\admin\\AppData\\Local\\Google\\Chrome\\User Data\\"
    4.生成浏览器选项配置对象
        options = webdriver.ChromeOptions()
    5.将第3步生成的用户数据目录添加到options当中
        options.add_argument(路径变量)
    6.用此选项来打开登录首页
        浏览器对象 = webdriver.Chrome(options=options)
        浏览器对象.get(url)
        此步完成之后会直接登录
    注意:在运行测试脚本时,先要将所有浏览器给关闭

"""
from selenium import webdriver
from time import sleep

# user_data = '--user-data-dir=C:\\Users\\Administrator\\AppData\\Local\\Google\\Chrome\\User Data'
user_data = r'--user-data-dir=C:\Users\Administrator\AppData\Local\Google\Chrome\User Data'
options = webdriver.ChromeOptions()
options.add_argument(user_data)
driver = webdriver.Chrome(options=options)

driver.get('https://mail.163.com/')
driver.maximize_window()

sleep(2)
driver.quit()
