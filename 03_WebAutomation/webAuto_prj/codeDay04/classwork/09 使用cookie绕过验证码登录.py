"""
 1.先用自动化的脚本打开百度网盘的登录首页
 2.打开之后先暂停60s
 3.立即在上述页面中进行手动的登录操作--此时操作的过程可以记录在自动化脚本运行的cookie当中
 4.把登录后的cookie给保存下来
 5.再次打开百度登录首页将所有cookie给清除
 6.将之前保存的cookie给添加原cookie里面
 7.用新添加好的cookie来登录(再次打开百度网盘首页),此时就可以达到绕过验证码的登录了
    因为cookie当中已经记录了我已登录的证明
"""
from selenium import webdriver
from time import sleep

# 第一次获取登录的cookie信息
# driver = webdriver.Chrome()
# driver.get('https://pan.baidu.com/')
# driver.maximize_window()
#
# sleep(30)
# print(driver.get_cookies())

# 将cookie信息保存
cookies = [{'domain': '.baidu.com', 'expiry': 1669464089, 'httpOnly': True, 'name': 'ab_sr', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': '1.0.1_MzY1YTUxZjcwZjc5YThlNzAwZWE4N2UxZTRhYTQ5MjUxODRkN2I5NzMyZjJkNGFmNWE1YzZkZDZhZTczNmY3MmY0MzQ0ZTBlMWFmZjhmOWE2NTgzNDI4NWI3OTg5ZjgwN2QxYmVmNTVhNWViMDY3NGE3ZjE4OTQxZGRiYjQ0MWQwZDE3ZjZhNDdkM2NiMjc5ZjVlZmU4YmY1NWNhMTM4ZWRkYWNlNzlhYjBhZWEyN2FlZmNkNzczNTg2ZjMzODI3'}, {'domain': 'pan.baidu.com', 'expiry': 1672048889, 'httpOnly': False, 'name': 'ndut_fmt', 'path': '/', 'secure': False, 'value': '0228FB4791155221FF60F8C01BC304A41461A22ACBE9177866D11590FDAA723B'}, {'domain': '.pan.baidu.com', 'expiry': 1672135286, 'httpOnly': True, 'name': 'STOKEN', 'path': '/', 'secure': False, 'value': '1ecf4ad67c789f0d5748c03049a2d4404a13c9bbf77d3a41811cb7434aaee5d3'}, {'domain': 'pan.baidu.com', 'httpOnly': False, 'name': 'csrfToken', 'path': '/', 'secure': False, 'value': 'zQi6O32wcDyQyJ8iZ7UnQTC6'}, {'domain': '.baidu.com', 'httpOnly': True, 'name': 'BDUSS_BFESS', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': 'UxKQk9zaDFEVTRIZjRqSEp1M0lVUVo4S3kxc011SDF4bnVTeG5Xc2d2MzFjS2xqSUFBQUFBJCQAAAAAAAAAAAEAAADviXCbRmlyZdi8U291bOzhAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPXjgWP144Fja'}, {'domain': '.pan.baidu.com', 'expiry': 1669543287, 'httpOnly': True, 'name': 'PANPSC', 'path': '/', 'secure': False, 'value': '8047339072097827099%3ACU2JWesajwDHJUi3SoboNEy7txDAjOFZ3bcI1X9JLoMUGw1K%2FdcnjBapIuguTVEEBm6rqQ5QdYLrR%2FKgoNNny%2FL7jFxBT2FxxkjO6GmYuHpVQyOINzWMXlx65cPJdg4R0v29HoOyBxO7W09FU%2BvrLt8NRd7EA5d%2B2fNZfjs7wBY%2FcoIBUQpA2juoAeCl9TBG'}, {'domain': '.baidu.com', 'httpOnly': True, 'name': 'BDUSS', 'path': '/', 'secure': False, 'value': 'UxKQk9zaDFEVTRIZjRqSEp1M0lVUVo4S3kxc011SDF4bnVTeG5Xc2d2MzFjS2xqSUFBQUFBJCQAAAAAAAAAAAEAAADviXCbRmlyZdi8U291bOzhAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPXjgWP144Fja'}, {'domain': '.baidu.com', 'expiry': 1700992865, 'httpOnly': False, 'name': 'BAIDUID_BFESS', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': '3CE1518D4101EB2E20BDA594B5B3C8F2:FG=1'}, {'domain': 'pan.baidu.com', 'httpOnly': False, 'name': 'XFT', 'path': '/disk', 'secure': False, 'value': 'fluumQ4sSvlYAhxn6lVjbZkie5TS1AirUq9wQXT8F40='}, {'domain': '.baidu.com', 'expiry': 1700992865, 'httpOnly': False, 'name': 'BAIDUID', 'path': '/', 'secure': False, 'value': '3CE1518D4101EB2E20BDA594B5B3C8F2:FG=1'}, {'domain': '.baidu.com', 'expiry': 1672048865, 'httpOnly': True, 'name': 'newlogin', 'path': '/', 'secure': False, 'value': '1'}, {'domain': 'pan.baidu.com', 'httpOnly': False, 'name': 'XFCS', 'path': '/disk', 'secure': False, 'value': '0B087EA274755466424B054F4BD9DBB6A06F36481DCBE60759C5160DDA1C7EBA'}, {'domain': 'pan.baidu.com', 'httpOnly': False, 'name': 'XFI', 'path': '/disk', 'secure': False, 'value': '8e03eaa6-1905-0830-7935-27dcbc0d0150'}]

# 再次打开浏览器进入网页
driver = webdriver.Chrome()
driver.get('https://pan.baidu.com/')
driver.maximize_window()
sleep(1)

# 删除所有cookie信息
driver.delete_all_cookies()
# 循环将cookies中的信息添加到浏览器cookie中
for i in cookies:
    driver.add_cookie(i)

sleep(1)
# 再次进入或直接刷新浏览器页面
# driver.get('https://pan.baidu.com/')
driver.refresh()


sleep(5)
driver.quit()



