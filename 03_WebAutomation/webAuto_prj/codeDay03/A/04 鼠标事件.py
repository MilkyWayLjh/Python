"""
掌握:必须掌握
概念:自动化测试时需要使用到鼠标的操作,此时selenium webdriver原生的方法中不能够实现相关的要求
    此时就需要使用ActionChains类来提供相关的操作方法

语法(常用):
context_click() 右击
double_click()  双击
drag_and_drop() 拖动
move_to_element() 鼠标悬停在一个元素上
click_and_hold() 按下鼠标左键在一个元素上
move_by_offset() 鼠标偏移设置

举例: 拖拽的操作步骤:
引入ActionChains()
from selenium.webdriver.common.action_chains import ActionChains
第1步：初始化ActionChians类（动作链条）：actions = ActionChains(driver)
第2步：找到要操作的元素：find_element
第3步：调用鼠标操作方法：actions.move_to_element(element)
第4步：执行鼠标操作方法：actions.perform()

ActionChains类 常用方法
1、click_and_hold(on_element=None)：点击鼠标左键，不松开
2、context_click(on_element=None)：点击鼠标右键
    说明：对于点击鼠标右键，如果弹出的是浏览器默认的菜单，Selenium没有提供操作菜单选项的方法；
    如果是自定义的右键菜单，则可以通过元素定位来操作菜单中的选项。
3、double_click(on_element=None)：双击鼠标左键
4、drag_and_drop(source, target)：拖拽到某个元素然后松开
    说明：模拟鼠标拖动动作，选定拖动源元素释放到目标元素后鼠标松开。
    1.源元素：source = driver.find_element_by_id(xxx)
    2.目标元素：target = driver.find_element_by_id(xxx)
    3.调用方法：action.drag_and_drop(source, target).perform()
5、move_by_offset(xoffset, yoffset)：鼠标从当前位置移动到某个坐标
6、move_to_element(to_element) ：鼠标移动到某个元素
    说明: 模拟鼠标悬停在指定的的元素上
7、release(on_element=None)：在元素上释放按住的鼠标按钮（在某个元素位置松开鼠标左键）
8、pause(seconds)：暂停操作(秒)

ActionChains类 其他方法
1、perform(self)--执行鼠标操作方法
2、reset_actions()：清除已在队列中的鼠标操作命令
3、click(on_element=None)：点击鼠标左键
4、click_and_hold(on_element=None)：点击鼠标左键，不松开
5、context_click(on_element=None)：点击鼠标右键
6、double_click(on_element=None)：双击鼠标左键
7、drag_and_drop(source, target)：拖拽到某个元素然后松开（需要获取到目标位置的元素定位）
8、drag_and_drop_by_offset(source, xoffset, yoffset)：拖拽到某个坐标然后松开（需要获取到目标位置的位置坐标）
9、key_down(value, element=None)：按下某个键盘上的键
10、key_up(value, element=None)：松开某个键
11、move_by_offset(xoffset, yoffset)：鼠标从当前位置移动到某个坐标（需要获取到目标位置的位置坐标）
12、move_to_element(to_element)：鼠标移动到某个元素
13、move_to_element_with_offset(to_element, xoffset, yoffset)：移动到距某个元素（左上角坐标）多少距离的位置
14、pause(seconds)：暂停操作(秒)---结合使用，比如：鼠标移动到某元素上悬停的时间。（暂停所有动作，相当于等待，用于链式操作过程中的等待）
15、release(on_element=None)：在元素上释放按住的鼠标按钮，与click_and_hold(on_element=None)点击鼠标左键不松开结合使用。（如果有鼠标按下的操作，那么需要通过release()方法释放鼠标）
16、send_keys(*keys_to_send)：发送某个键到当前焦点的元素
17、send_keys_to_element(element, *keys_to_send)：发送某个键到指定元素
"""
from common.open_web import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

# driver = open_web('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')   # 菜鸟拖拽
# driver = open_web()     # 百度更多 悬停
driver = open_web('https://www.jq22.com/yanshi23642')     # 移动滑块

"""
# 菜鸟拖拽
# 切换进入到指定的iframe
driver.switch_to.frame('iframeResult')
source = driver.find_element(By.ID, 'draggable')
target = driver.find_element(By.ID, 'droppable')
ac = ActionChains(driver)
# ac.drag_and_drop(source, target).release().perform()    # release()在元素上释放按住的鼠标按钮,perform()执行事件
# ActionChains类源码方法中已经使用了release()释放方法，所以不再需要用此方法
ac.drag_and_drop(source, target).perform()
"""

"""
# 百度更多 悬停
ac = ActionChains(driver)
target = driver.find_element(By.LINK_TEXT, '更多')
# 将鼠标悬停到"更多"选项上
ac.move_to_element(target).perform()
"""

# 移动滑块
#   切换进入iframe
iframe = driver.find_element(By.ID, 'iframe')
driver.switch_to.frame(iframe)
# 鼠标按住位置
source = driver.find_element(By.CSS_SELECTOR, '.slider-btn')
# 生成一个鼠标对象
ac = ActionChains(driver)
# 按住鼠标左键
ac.click_and_hold(source)
sleep(1)
# 鼠标偏移设置,并且释放,执行
ac.move_by_offset(268, 0).release().perform()

# 点击重置滑块
driver.find_element(By.ID, 'reset').click()
sleep(1)

# 重新获取元素(元素引用失效：source 元素在页面重置后已不存在)
source = driver.find_element(By.CSS_SELECTOR, '.slider-btn')
# 直接使用drag_and_drop_by_offset(source, xoffset, yoffset)方法, 因为没有目标元素，无法直接使用drag_and_drop()方法，所以xoffset和yoffset必须指定
ac.drag_and_drop_by_offset(source, 268, 0).perform()

sleep(2)
driver.quit()
