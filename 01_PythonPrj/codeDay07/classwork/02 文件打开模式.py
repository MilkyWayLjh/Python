"""
打开模式：r:read, w:write（覆盖写）, a:追加写(指针光标在文件内容的结尾处)
        b:二进制操作 +:扩展功能
"""
# r模式
"""
# 打开文件-读
# f = open('resource/demo1.txt', mode='r', encoding='utf8')
f = open('resource/demo1.txt', encoding='utf8')
# 操作文件
content = f.read()  # 返回读到的内容
print(content)
# 关闭文件
f.close()
"""

# w模式
# 特点:不存在则创建，有内容会覆盖
"""
# 打开文件-w
f = open('resource/demo1.txt', 'w', encoding='utf8')
# 操作文件
f.write('w是覆盖写操作')
# 关闭文件
f.close()
"""

# a模式
# 特点:不存在则创建，有内容会在后面进行追加
"""
f = open('resource/demo1.txt', 'a', encoding='utf8')
f.write('\na模式是追加写模式2\n')
f.close()
"""

# b模式，不能单独使用
# 注意：b模式，不能设置encoding
"""
f = open('resource/pic1.png', 'rb')
print(f.read())
f.close()
"""

# +模式，不能单独使用
# r+ 原文件读和写   w+ 可以创建
"""
f = open('resource/test02.txt', 'r+', encoding='utf8')
r = f.read()
print(r)
w = f.write('\nhello mysql1')
print(w)    # 返回写入的字符数
print(f.tell())     # 返回文件对象当前所处的位置, 它是从文件开头开始算起的字节数。
f.close()
"""

"""
f = open('resource/demo2.txt', 'w+', encoding='utf8')
# f.seek(0)
# print(f.read())
f.write('use w+ mode')
f.seek(0)
print(f.read())
f.close()
"""
