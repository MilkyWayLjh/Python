"""
 掌握:
    重点,必须掌握
 概述:
    CSS(Cascading Style Sheets)是一种语言，它被用来描述HTML 和XML 文档的表现。
    CSS 使用选择器来为页面元素绑定css属性。这些选择器可以被selenium 用作另外的定位策略。
 语法:
    浏览器对象.find_element_by_css_selector("选择器")
    1.使用id和class选择器进行定位
        浏览器对象.find_element_by_css_selector("#id属性值")--"#"表示id属性
        浏览器对象.find_element_by_css_selector(".class属性值")--"."表示class属性
    2.css定位其它方法
        (1)标签+属性
            浏览器对象.find_element_by_css_selector('标签名[属性名="属性值"]')
        (2)层级+属性
            浏览器对象.find_element_by_css_selector('父标签名[属性名="属性值"]>子标签名')
                css使用层级+属性定位时,各层级之间用">"隔开
        (3)多条件定位 (不用and)
            浏览器对象.find_element_by_css_selector('父标签名[属性名1="属性值1"][属性名2="属性值2"]>子标签名')
        (4)模糊定位
            浏览器对象.find_element_by_css_selector('标签名[属性名 *="部分属性值"]')
                "*":表示任意属性值
                "^":表示以某个特定字符开始
                "$":表示以某个特定的字符结束
        (5)层级+属性+索引相结合
          [1]:nth-child(n)--直接索引值
            n:表示标签索引值
            浏览器对象.find_element_by_css_selector('父标签名[属性名="属性值"]> :nth-child(索引值)')
                注意:在使用":nth-child(n)"时前面一定要有空格
          [2]:nth-of-type(n)--根据标签类型使用索引值
            浏览器对象.find_element_by_css_selector('父标签名[属性名="属性值"]>标签名:nth-of-type(索引值)')
"""
from open_web import *

driver = open_web()

sleep(1)

# driver.find_element_by_css_selector('#kw').send_keys('css使用id属性定位')
# driver.find_element_by_css_selector('.s_ipt').send_keys('css使用class定位')
# driver.find_element_by_css_selector('input[id="kw"]').send_keys('css标签+属性定位')
# driver.find_element_by_css_selector('form[id="form"]>span>input').send_keys('css层级+属性定位')
# driver.find_element_by_css_selector('form[id="form"][action="/s"]>span>input').send_keys('css多条件定位')
# driver.find_element_by_css_selector('form[id="form"][class *="has"]>span>input').send_keys('css模糊匹配定位')
# driver.find_element_by_css_selector('form[id="form"][class ^="fm"]>span>input').send_keys('css模糊匹配定位')
# driver.find_element_by_css_selector('form[id="form"][class $="tu"]>span>input').send_keys('css模糊匹配定位')
# driver.find_element_by_css_selector('form[id="form"]>span> :nth-child(2)').send_keys('css索引定位nth-child(n)')
print(driver.find_element_by_css_selector('form[id="form"]>span>i:nth-of-type(2)').get_attribute('outerHTML'))

sleep(2)
driver.quit()

