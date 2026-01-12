"""
    1.先用自动化的脚本打开百度/百度网盘的登录首页
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
# # driver.get('https://pan.baidu.com/')
# driver.get('https://www.baidu.com/')
# driver.maximize_window()
#
# sleep(60)
# print(driver.get_cookies())

# 将cookie信息保存
cookies = [{'domain': '.baidu.com', 'expiry': 1799135353, 'httpOnly': False, 'name': 'ZFY', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': 'zcubl0dNNu9tbUOt0Jbnqjpxbnw6D69K2scy8x:BhnOU:C'}, {'domain': '.baidu.com', 'expiry': 1802159412, 'httpOnly': True, 'name': 'BDUSS_BFESS', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': 'w3QVIzS0NRMEtPWXlNU1pSbW5lRS10OFp6US1yQk0yQ3B4Z0JOU1l-Z3gtb0pwRVFBQUFBJCQAAAAAAAAAAAEAAADviXCbzOzH4Ln90-pfMWlqaAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADFtW2kxbVtpNU'}, {'domain': '.baidu.com', 'expiry': 1802159412, 'httpOnly': True, 'name': 'BDUSS', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'w3QVIzS0NRMEtPWXlNU1pSbW5lRS10OFp6US1yQk0yQ3B4Z0JOU1l-Z3gtb0pwRVFBQUFBJCQAAAAAAAAAAAEAAADviXCbzOzH4Ln90-pfMWlqaAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADFtW2kxbVtpNU'}, {'domain': '.baidu.com', 'expiry': 1799135354, 'httpOnly': False, 'name': 'BAIDUID_BFESS', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': '09345B893869BDB32DDD7086A5EDCD94:FG=1'}, {'domain': '.baidu.com', 'expiry': 1767685752, 'httpOnly': False, 'name': 'BA_HECTOR', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '8sa4a4a52l0000ekak8g042hak8g2g1klmr7p27'}, {'domain': 'www.baidu.com', 'httpOnly': False, 'name': 'BD_HOME', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '1'}, {'domain': 'www.baidu.com', 'httpOnly': False, 'name': 'XFI', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '086f0a00-ea0b-11f0-9a42-f33408d98038'}, {'domain': 'www.baidu.com', 'httpOnly': False, 'name': 'XFCS', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '0970A270B83F46A40D34C9916DD3697819A4A7E10E10A5492B0AE004A0E03366'}, {'domain': '.baidu.com', 'expiry': 1799135351, 'httpOnly': False, 'name': 'BAIDUID', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '09345B893869BDB32DDD7086A5EDCD94:FG=1'}, {'domain': 'www.baidu.com', 'httpOnly': False, 'name': 'XFT', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'H/G7m0jSDgQdhljFPwQZE9mYTlwWlhKmzpYlgTeHEMQ='}, {'domain': '.baidu.com', 'expiry': 1802159351, 'httpOnly': False, 'name': 'BIDUPSID', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '09345B893869BDB3CD6A26E04368979F'}, {'domain': '.baidu.com', 'httpOnly': False, 'name': 'ppfuid', 'path': '/', 'sameSite': 'Lax', 'secure': True, 'value': 'FOCoIC3q5fKa8fgJnwzbE67EJ49BGJeplOzf+4l4EOvDuu2RXBRv6R3A1AZMa49I27C0gDDLrJyxcIIeAeEhD8JYsoLTpBiaCXhLqvzbzmvy3SeAW17tKgNq/Xx+RgOdb8TWCFe62MVrDTY6lMf2GrfqL8c87KLF2qFER3obJGmwKsggvQ93gWKRRjAgI2cnGEimjy3MrXEpSuItnI4KDxsDW/slC+uEItnUE1AcCFO0lBXl5v3/LKjxpuUw7Ym6Rr6eAA3wSMa1a5aQBusBuRJsVwXkGdF24AsEQ3K5XBbh9EHAWDOg2T1ejpq0s2eFy9ar/j566XqWDobGoNNfmfpaEhZpob9le2b5QIEdiQe/UUOOs2fkuUdvUcIGr3f6FCMUN0p4SXVVUMsKNJv2T2CQf+Hv9swTKvjW4dK8z6a8jR6nMT6ahBlb99DkUdC0zkWOdjFiy1eD/0R8HcRWYqtAmDJG1J/knCZtJ3rCRcip+HBavJhpxl858h16cMtKQmxzisHOxsE/KMoDNYYE7ucLE22Bi0Ojbor7y6SXfVj7+B4iuZO+f7FUDWABtt/WWQqHKVfXMaw5WUmKnfSR5wwQa+N01amx6X+p+x97kkGmoNOSwxWgGvuezNFuiJQdt51yrWaL9Re9fZveXFsIu/gzGjL50VLcWv2NICayyI8BE9m62pdBPySuv4pVqQ9Sl1uTC//wIcO7QL9nm+0N6JgtCkSAWOZCh7Lr0XP6QztjlyD3bkwYJ4FTiNanaDaDHAw5LdV5Xu0s6nXYqp9fya4at8wf8BUHCgbSuBznn5yMS/76+qi5vj/nH2tA07PTSGk66HDxtjKMU4HPNa0dtv9tmNi5OLf3trbXvvpFbLWEB8hf4s5ieWYkugh95AkbJXzxzBwzWy+n7NUONSlz67BPqpuUhe65/b9ltjpoL6fpdtQcQSh9joeJ0J5/037rxap2Id38bvwL5+x9bM6YuOAFGQM9PC1eNi2DOZbvibR8NTYxlrGkFlkXxi6t+hxhyYN1zEUp6ggVCZWoCgBT7dhxdC3bEpOFlnJXW/ewK+fOJ1Rm0oz1xFFR9FYG1BJvnQA8z6Cz/jTzGDsocIHwA4qlml8ik+FDREmF7DwZHRpOpiwmjUhELAzdRtuu+0nt6o8w3MlwZxJhxBabUW5sicyie973hz6nxWLbBzvYx9F54WJPMynUbqkO3Z7jSA8MZt1Aj6NtrhSNGXID70JtNd6jbmAuXAR4EGVsr+DCMt/KTLoU96dsmC3+9Ar1MCJM'}, {'domain': 'www.baidu.com', 'expiry': 1768463352, 'httpOnly': False, 'name': 'BD_UPN', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '12314753'}, {'domain': '.baidu.com', 'expiry': 1802159351, 'httpOnly': False, 'name': 'PSTM', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '1767599349'}]

# 再次打开浏览器进入网页
driver = webdriver.Chrome()
# driver.get('https://pan.baidu.com/')
driver.get('https://www.baidu.com/')
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
# driver.get('https://www.baidu.com/')
driver.refresh()

sleep(5)
driver.quit()
