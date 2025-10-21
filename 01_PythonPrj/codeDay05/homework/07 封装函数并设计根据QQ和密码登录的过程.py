# 封装函数，设计根据QQ和密码登录的过程(QQ和密码预设为指定的值). 执行结果为登录是否成功(boolean类型的值)

# QQ和密码预设为指定的值
# qq_account = '112233'
# qq_password = '123456'
#
# qq_account1 = input('请输入QQ账号: ')
# qq_password1 = input('请输入QQ密码: ')
#
#
# def login(account, password):
#     if account == qq_account and password == qq_password:
#         print(True)
#     else:
#         print(False)
#
# login(qq_account1, qq_password1)


def login():
    qq_account = '123'
    qq_password = '456'

    qq_account1 = input('请输入QQ账号: ')
    qq_password1 = input('请输入QQ密码: ')

    # print(qq_account1 == qq_account and qq_password1 == qq_password)
    return qq_account1 == qq_account and qq_password1 == qq_password

# login()
print(login())
