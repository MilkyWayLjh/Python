"""
概念:
    有些网站为了将网而做的更加美观,会话使用传统alert对话框,而选择自定义的广告弹出框来吸引用户
    这些广告框的特点时,无法永久性关闭.即便关闭后它也会再次弹出来,这样就会影响到页面元素的操作.
    所在做自动化需要将此类的广告给永久性关闭(这种方式只是修改当前浏览器中的网页效果)
语法:
    js = "document.getElementByXxx('属性值').style.display='none'"
    浏览器对象.execute_script(js)

"""
from common.open_web import *

driver = open_web('https://www.itsource.cn')
sleep(2)

# 测试操作：正常用户的操作
# close_element = driver.find_element_by_xpath('//*[@id="iframe_company_mini_div"]/h6/span[2]')
# close_element.click()

# javascript = ECMAScript + Bom + Dom
js = "document.getElementById('div_company_mini').style = 'display: none'"
driver.execute_script(js)

sleep(2)
driver.quit()

