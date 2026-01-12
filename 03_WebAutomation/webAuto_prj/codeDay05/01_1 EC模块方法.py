"""
expected_conditions模块:
    expected_conditions 模块可以对网页上元素是否存在，可点击等等进行判断，一般用于断言或与WebDriverWait配合使用。
一般情况下，我们在使用expected_conditions类时都会对其进行重命名，通过as关键字对其重命名为EC。
    引包: from selenium.webdriver.support import expected_conditions as EC

title_is(title):
    判断网页title是否是特定文本（英文区分大小写），若完全相同则返回True，否则返回False
title_contains(title):
    判断网页title是否包含特定文本（英文区分大小写），若包含则返回True，不包含返回False
presence_of_element_located(locator):
    判断一个元素存在于页面DOM树中，存在则返回元素本身，不存在则报错。
    locator为一个(by, path)元祖，这个(by, path)的by是Selenium的一个类(selenium.webdriver.common.by.By)，
    包括CLASS_NAME，CSS_SELECTOR，ID，LINK_TEXT，NAME，PARTIAL_LINK_TEXT，TAG_NAME和XPATH，和我们元素定位中使用的方法相同
visibility_of_element_located(locator):
    判断特定元素是否存在于DOM树中并且可见，可见意为元素的高和宽都大于0，元素存在返回元素本身，否则返回False
    这个类和presence_of_element_located(locator)有点像，但后者只强调元素存在于DOM树中，可见不可见无所谓，
    而前者要求必须高和宽必须都大于0，因此后者在性能上会稍微快一点点
visibility_of(element):
    同上面一样，不过参数从locator的元组变为元素
presence_of_all_elements_located(locator):
    判断定位的元素范围内，至少有一个元素存在于页面当中，存在则以list形式返回元素本身，不存在则报错。
text_to_be_present_in_element(locator,text):
    判断给定文本是否出现在特定元素中，若存在则返回True，不存在返回False
text_to_be_present_in_element_value(locator,text):
    判断某文本是否是存在于特定元素的value值中，存在则返回True，不存在则返回False，对于查看没有value值的元素，也会返回False
frame_to_be_available_and_switch_to_it(locator):
    判断某个frame是否可以切换过去，若可以则切换到该frame，否则返回False .
invisibility_of_element_located(locator):
    判断元素是否隐藏。
element_to_be_clickable(locator):
    判断某元素是否可访问并且可启用，比如能够点击，若可以则返回元素本身，否则返回False
staleness_of(element):
    判断某个元素是否不再附加于于DOM树中，不再附加的话返回True，依旧存在返回False
element_selection_state_to_be (element, is_selected):
    判断某元素的选中状态是否与预期相同，相同则返回True，不同则返回False
element_located_selection_state_to_be(locator, is_selected):
    判断某元素是否与预期相同，相同则返回True，不同则返回False，locator为一个(by, path)元祖
element_to_be_selected(element):
    判断某元素是否被选中
element_located_to_be_selected(locator):
    判断某元素是否被选,locator为一个(by, path)元祖
alert_is_present:
    判断alert是否存在，若存在则切换到alert，若不存在则返回false

"""
