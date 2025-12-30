# 需求: 验证用户输入的是否是一个文件
# 接收用户输入 aa.txt bb.mp4 aa.doc xx.JPEG
import re

filename = input('文件名:')
# 判断用户输入的是否是一个文件
if re.search('^\w{1,32}\.[a-zA-Z0-9]{2,5}$', filename):
    print('文件格式正确')
else:
    print('文件格式不正确')
