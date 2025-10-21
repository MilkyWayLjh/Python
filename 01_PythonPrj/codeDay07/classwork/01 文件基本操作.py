# 打开文件
"""
f(文件资源对象) = open(文件路径, mode='r', encoding='utf8')
文件路径：文件的位置，可以是绝对路径也可以是相对路径
mode：打开模式，确定接下来操作文件的方式读(r:read),写(w:write)
w:如果文件不存在，会自动创建该文件
"""
# 操作文件
"""
f.write(content)   写入
f.read()  读
"""
# 关闭文件
"""
f.close()
"""

"""
# 打开文件
f = open('resource/demo1.txt', 'w', encoding='utf8')
# 操作文件
f.write('hello python')
# 关闭文件
f.close()
"""

# 1 打开文件 open(文件路径, 打开模式， 字符集)
f = open('./resource/test01.txt', 'a', encoding='utf-8')

# 2 操作文件    f.read()  f.write(content)
f.write('我也是个粉刷匠\n粉刷本领还要强~')

# 3 关闭文件
f.close()
