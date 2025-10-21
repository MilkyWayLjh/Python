# 导入os模块
import os

# 1 os.rename("文件名","新的文件名")  文件或目录重命名
# Python3.3中新增 os.replace(src, dst)  用于重命名文件或目录
# 区别：  目标文件已经存在，去替换它，应该使用 os.replace；
#       而如果只是简单地重命名并且不需要覆盖已存在的文件，可以使用 os.rename。
# demo.txt my_demo.txt
"""
os.rename('resource/demo.txt', 'resource/my_demo.txt')
"""

# 2 os.remove ("文件名") 删除文件
"""
os.remove('del_demo.txt')
os.remove('my_demo.txt')
"""

# 3 os.unlink(path) 用于删除文件,如果文件是一个目录则返回一个错误。
# os.unlink('resource/1.txt')

# 4 os.removedirs(path)   用于递归删除空目录。
#   像rmdir(), 如果子文件夹成功删除, removedirs()才尝试它们的父文件夹,直到抛出一个error(它基本上被忽略,因为它一般意味着你文件夹不为空)。
# os.removedirs('resource/1/3')

# 5 os.rmdir('目录路径') 删除空目录(单层)
# os.rmdir('resource/1/3')  # 空目录可以删除
# os.rmdir('resource')  # 有内容删除不了

# 5.1 删除非空目录 shutil.rmtree(path)
"""
import shutil
shutil.rmtree('resource/2')
"""

# 6 os.mkdir ("文件夹的名字") 创建文件夹
"""
os.mkdir('resource/dir1')
"""

# 7  os.getcwd()  获取当前目录路径
# print(os.getcwd())

# 8  os.chdir ()  切换目录
"""
# 切换到resource
os.chdir('resource')
# 新建一个demo6.txt
f = open('demo6.txt', 'w', encoding='utf8')
f.close()
"""

# 9 os.listdir("目录路径")  列出目录下的资源
# print(os.listdir())
# print(os.listdir('resource'))


# 10 os.path.isdir("目录路径") 判断资源是文件夹
"""
print(os.path.isdir('resource'))
print(os.path.isdir('resource/demo1.txt'))
"""

# 11 os.path.isfile("文件路径") 判断资源是文件
"""
print(os.path.isfile('resource'))
print(os.path.isfile('resource/demo1.txt'))
"""

# 12 os.path.splitext('文件路径')  extension: 扩展 获取文件扩展
# filename, extension = os.path.splitext('01 文件基本操作.py')  # 返回：（文件名, 后缀） -> (‘user’, ‘.txt’)
# print(filename)
# print(extension)

# 13 os.path.split(path)   把路径分割成 dirname 和 basename，返回一个元组
# 分割成 路径名 和 文件名

# 14 os.path.join(path1[, path2[, ...]])    把目录和文件名合成一个路径
# 15 os.path.abspath(path)      返回绝对路径
# os.path.dirname(path)     返回文件路径
# os.path.basename(path)    返回文件名
# os.path.exists(path)  路径存在则返回True,路径损坏返回False
# os.path.getatime(path)	返回最近访问时间（浮点型秒数）
# os.path.getmtime(path)	返回最近文件修改时间
# os.path.getctime(path)	返回文件 path 创建时间
# os.path.getsize(path)	返回文件大小，如果文件不存在就返回错误
# os.path.isabs(path)	判断是否为绝对路径
# os.path.isfile(path)	判断路径是否为文件
# os.path.isdir(path)	判断路径是否为目录
