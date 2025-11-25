# 需要在终端使用python命令启动脚本文件: python '.\01 给程序传参.py' 127.0.0.1 'hello'
# print(111)

import sys

print(sys.argv)     # 返回一个列表，内容是终端传递的参数
# ['01 给程序传参.py', '127.0.0.1', 'hello']


def send_msg(ip, msg):
    print(f'向{ip}地址 发送消息为：{msg}')


send_msg(sys.argv[1], sys.argv[2])
