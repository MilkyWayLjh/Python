import os
import shutil
from pathlib import Path

Path('os_demo/a').mkdir()
Path('os_demo/a.txt').touch()
Path('os_demo/b').mkdir()
Path('os_demo/b/1').mkdir()
Path('os_demo/b.txt').touch()

# shutil.move(): 移动文件或目录。如果不存在目标文件或目录，则创建该文件或目录。
shutil.move('os_demo/a', 'os_demo/c')
shutil.move('os_demo/b.txt', 'os_demo/c.txt')
shutil.move('os_demo/a.txt', 'os_demo/b/1/')
# shutil.rmtree(): 删除整个目录树（包括其中的所有文件和子目录）
shutil.rmtree('os_demo/b')


# 文件重命名或替换文件
os.rename('os_demo/c', 'os_demo/a')
os.rename('os_demo/c.txt', 'os_demo/a.txt')
os.replace('os_demo/a', 'os_demo/1')
os.replace('os_demo/a.txt', 'os_demo/1.txt')

# 删除文件
os.remove('os_demo/1.txt')

# 删除空目录(单层)
os.rmdir('os_demo/1')

# 创建空目录
# os.mkdir('os_demo/1')

# ----------------------------------------------

# 获取当前目录
print(os.getcwd())

# 切换目录
os.chdir('resource')
print(os.getcwd())

# 列出目录下的资源
print(os.listdir())
print(os.listdir('../../homework'))

# 判断资源是文件夹
os.chdir('../')
print(os.getcwd())
print(os.path.isdir('os_demo'))  # True
print(os.path.isdir('resource/demo1.txt'))  # False

# 判断资源是文件
print(os.path.isfile('os_demo'))    # False
print(os.path.isfile('resource/demo1.txt'))  # True

# 获取文件扩展名
filename, extension = os.path.splitext('os操作.py')  # 返回：（文件名, 后缀） -> (‘user’, ‘.txt’)
print(os.path.splitext('os操作.py'))  # ('os操作', '.py')
print(filename)
print(extension)

# 把路径分割成 目录路径 和 文件名(包含扩展名) 两部分，返回一个元组
print(os.path.split('os操作.py'))  # ('', 'os操作.py')
print(os.path.split('os_demo/1.txt'))   # ('os_demo', '1.txt')

# 把目录和文件名合成一个路径
print(os.path.join('os_demo', '1.txt'))  # os_demo/1.txt

# 返回绝对路径
print(os.path.abspath('os_demo'))
print(os.path.abspath(''))  # 更适合用于获取指定其他文件的绝对路径
print(os.getcwd())  # 获取当前工作目录时，推荐使用 os.getcwd()，因为它更直接、效率更高
