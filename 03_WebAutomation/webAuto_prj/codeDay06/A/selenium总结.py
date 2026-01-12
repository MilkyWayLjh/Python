"""
第一天
1.自动化的相关的概述
2.selenium环境搭建
    (1)下载selenium --pip install selenium==3.141.0
    (2)安装chrome浏览器
    (3)安装chromedriver
3.元素定位
    1.id
    2.name
    3.classname
    4.link_text
    5.partial_link_test
    6.tag_name
    7.css定位
        两类6种
        基础选择器
            使用id，class直接定位
            #表示id，.class
        其它选择器
            （1）标签+属性
             (2)层次+属性 --使用”>“表示层次
            （3）多条件（不用and）
                find_element_by_css_selector('标签名[属性1=”属性值1“][属性2=”属性值2“]')
            (4)模糊定位 --用粗略的属性值
                find_element_by_css_selector('标签名[属性1 *=”部分属性值“][属性2=”属性值2“]')
            (5)标签加索引--索引值是从1开始计算
              :nth-child(n)--在当标签下选择第几个标签
                 find_element_by_css_selector('父标签名> :nth-child(子标签编号)')
              :nth-of-type(n)--从当前标签下选择指定类型标签中的第几个标签
                find_element_by_css_selector('父标签名>子标签名:nth-of—type(子标签编号)')

    8.xpath定位
        绝对路径：写个完成的标签路径
        相对路径：
            标签+属性
            层次+属性-- 使用”/“表示层次
            多条件(使用and)
                 find_element_by_xpath('标签名[属性1=”属性值1“ and 属性2=”属性值2“]')
            模糊定位 --用粗略的属性值--contains
                find_element_by_xpath('标签名[contains （@属性名,部分属性值))
            标签+索引-->索引值是从1开始
                find_element_by_xpath('父标签名[contains （@属性名,部分属性值)/子标签[索引值])


"""
from selenium import webdriver

# 打开浏览器
driver = webdriver.Chrome()

# 打开网址
driver.get('url')
# 窗口最大化，设置窗口大小，前进，后退，刷新
# 无头模式


"""
第二天
页面操作方法
    获取文本，获取url，获取title，获取属性值，输入 ，点击
多窗口切换
    切换句柄
    driver。switch_to.window()
frame切换
    driver.switch_to.frame(id/name/xpath)

面试题：如果在元素提示元素找不到，请问你觉得有哪些原因导致？
没有切换frame，没有切换窗口，元素是动态属性，网络加载慢等等

如果在web自动化中存在多路由的情况该如何操作？
切换frame

"""

"""
每三天

API操作:
鼠标事件
from selenium.webdriver.common.action_chains import ActionChains

键盘事件
from selenium.webdriver.common.keys import Keys

下拉菜单
from selenium.webdriver.support.select import Select

单选框，复选框
    单元框，直接元素定位
    复选框，定位一组元素然后遍历过滤使用
js操作
    操作滚动条
    当时间输入框为readonly属性，通过js写入时间数据
        js = ”document.getElementByxx('属性值')[索引].value='2022-12-01 12:53:53'“
    关闭自定义弹窗

"""

"""
第四天
1.文件上传
直接元素定位后使用send_keys()方法上传文件
send_keys("文件路径")

2.处理验证码
（1）设置万能验证码
（2）去掉验证码
 (3)使用图像识别技术来识别验证码
 (4）使用cookie来绕过验证码
        首先selenim打开登录首页，并暂时60s
        手动输入登录账号——>让selenium获取到手动登录后的cookie
        保存上一步获取的cookie
        再打编写自动化脚本
            打开浏览器
            删除了所有的cookie--->会将原有的cookie清空，但是cookie名字还在
            将手动登录后保存的cookie添加到原有的空的cookie当中-->重新生成了一个包含登录过程的cookie
            这此过程不能关闭浏览器
        再次打开浏览器和登录首页就可以直接登录成功了
        
元素等待--等待的目的是加强脚本的稳定性
 1.sleep:强制休眠
 2.隐式等待
    它是全局的等待，当超过最大等待时间后会报nosuchelement
 3.显示等待
    它是一个单一元素的等待方式，它需要结合until来使用，一般用它是作断言使用,有时也可用它来对显示时间较短的元素进行操作(toast弹窗)
    当超过最大等待时间后它会报timeout
    
"""

"""
第五天
自动化用例的相关概念
pom模型
    1.common--公共
        它是放置在自动化测试过程中需要用到公共的操作行为
        例如：向pandas获取数据，向数据库获取数据（pymysql）
    2.base--基本
        放置一些基本操作行为
        例如：点击，输入，清空，切换句柄，切换窗口，查找元素，获取文本
    3.reports
        放置自动化测试报告
    4.case
        用unittest框架来将pageobject层的内容组成测试用例
    5.data
        用来存放测试相关的数据
    6.pageobject
        将每个页面单独进行定义，将每一个页面中每一个单独用独立的方法来进行编写（一个页面用一个.py文件一个类来编写）
好处：让脚本关联性降低(便于后期维护修改)，将数据和脚本分离，提高编写效率


pandas
    用来管理测试数据，也就是将一个文件中内容读取测试用例当中


"""

"""
第六天
unittest框架相关


"""
