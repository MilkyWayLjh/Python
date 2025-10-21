# 案例一：用户登录
"""
需求：
    1.程序启动，提示用户登录或者注册
    2.选择注册->要求输入用户名和密码->返回注册提示信息
    3.选择登录->要求输入用户和密码->判断是否登录成功
    4.判断注册用户名重复问题
分析:
    1.根据录入的1,2 判断用户为登录和注册
    2.注册: 将用户录入的用户名和密码以下面的格式写入到文件中
     用户名1,密码1
     用户名2,密码2
    3.登录: 读取出每一行并且通过,分割出来用户名和密码与用户录入的用户名和密码进行比对
"""


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
            # exit(0)


main()
