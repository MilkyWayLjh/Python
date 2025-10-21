# 案例一：用户登录


def user_data():
    username = input('请输入用户名: ')
    password = input('请输入密码: ')
    return username, password


def register():
    print('欢迎来到注册页面!')
    username, password = user_data()
    f = open('resource/user.txt', 'r+', encoding='utf-8')
    user_list = f.readlines()
    li = []
    for userinfo in user_list:
        userinfo = userinfo.strip('\n').split(',')
        li.append(userinfo[0])
    while True:
        if username in li:
            print('用户名相同, 请重新输入!')
            username, password = user_data()
        else:
            f.write(f'{username},{password}\n')
            f.close()
            print('注册成功!')
            key = input('===>请选择是否跳转到登录页面(y/n): ')
            if key == 'y':
                login()
            else:
                print('退回首页!')
            break

# 一次性的判断，没有死循环判断
# for userinfo in user_list:
#     userinfo = userinfo.strip('\n').split(',')
#     if username == userinfo[0]:
#         print('用户名相同, 请重新输入!')
#         f.close()
#         break
# else:
#     f.write(f'{username},{password}\n')
#     print('注册成功!')
#     f.close()
#     key = input('===>请选择是否跳转到登录页面(y/n): ')
#     if key == 'y':
#         login()
#     else:
#         print('退回首页!')


def login():
    print('欢迎来到登录页面!')
    username, password = user_data()
    f = open('resource/user.txt', 'r', encoding='utf-8')
    user_list = f.readlines()
    f.close()
    for userinfo in user_list:
        userinfo = userinfo.rstrip('\n').split(',')
        if username == userinfo[0] and password == userinfo[1]:
            print('登录成功!\n欢迎来到召唤师峡谷!')
            while True:
                key = input('===>请选择是否退回首页(y/n): ')
                if key == 'y':
                    print('成功退回!')
                    break
                else:
                    print('不想退就继续玩咯!')
            break
    else:
        print('登录失败!')


flags = {
    '1': register,
    '2': login
}


def main():
    while True:
        flag = input('请选择注册或登录(1 / 2): ')
        if flag in flags.keys():
            flags[flag]()
        else:
            print('输入选择错误, 退出系统!')
            break

main()
