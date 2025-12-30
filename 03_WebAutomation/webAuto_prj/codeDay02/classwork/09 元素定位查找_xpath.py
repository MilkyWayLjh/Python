"""
    掌握: 重点必须掌握
    概念: xpath是在xml文档中进行元素和属性查找遍历的语言,同样也可用于HTML文档中进行元素查找,它是一门语言
    语法:
        1.绝对路径定位
            编写元素完整的路径表达式
            input_path = 'html/body/div/div/div[5]/div/div/form/span/input'
        2.相对路径定位
            (1)使用标签+属性定位
                浏览器对象.find_element_by_xpath("//标签名[@属性='属性值']")
                注意: 使用相对路径需要用到"//",表示在当前任意路径中查找;
                   @: 表示使用属性;
                   在路径编写中属性值的引号要与路径外面的引号类型要不一致.
            (2)层级+属性定位
                浏览器对象.find_element_by_xpath("//父标签名[@属性='属性值']/子标签/孙标签")
            (3)层级+索引+属性
                浏览器对象.find_element_by_xpath("//父标签名[@属性='属性值']/子标签[索引值]")
                标签的索引值是从1开始计算的
            (4)多条件定位,要用and
                浏览器对象.find_element_by_xpath("//父标签名[@属性1='属性值1' and @属性2='属性值2']/子标签[索引值]")
            (5)模糊定位--使用部分的属性值进行定位
                浏览器对象.find_element_by_xpath('//标签名[contains(@属性名,"部分属性值")]')

"""
from open_web import *

driver = open_web()

sleep(1)

# 绝对路径  当为第一个元素时可以不加[1],即 div[1] = div
input_xpath = '/html/body/div[1]/div[1]/div[5]/div[1]/div[1]/form/span/input'
# driver.find_element_by_xpath(input_xpath).send_keys('xpath定位')

# 相对路径
# 1 使用标签+属性定位
# driver.find_element_by_xpath('//input[@id="kw"]').send_keys('xpath定位')

# 2 层级+属性定位
# driver.find_element_by_xpath('//form[@id="form"]/span/input').send_keys('xpath定位')

# 3 层级+索引+属性
# print(driver.find_element_by_xpath('//form[@id="form"]/span/i[2]').get_attribute('outerHTML'))
# <i class="quickdelete-line"></i>

# 4 多条件定位,要用and
# driver.find_element_by_xpath('//form[@id="form" and @name="f"]/span/input').send_keys('xpath定位')

# 5 模糊定位--使用部分的属性值进行定位
driver.find_element_by_xpath('//span[contains(@class, "quickdelete")]/input').send_keys('xpath定位')

sleep(2)
driver.quit()

