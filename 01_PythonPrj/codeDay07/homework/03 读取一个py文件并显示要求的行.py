"""
读取一个py文件，显示除了以井号(#)开头的行以外的所有行
"""
py_file = input('输入一个py文件: ')
f = open(py_file, 'r', encoding='utf-8')
for line in f:
    if not line.startswith('#'):
        print(line, end='')
f.close()
