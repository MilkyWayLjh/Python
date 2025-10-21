"""
文件操作步骤
1. 打开文件
2. 操作文件
3. 关闭文件

类名：File
    方法：
        init：创建文件句柄：   self.f = open(xx)
        read
        write
        del: self.f.close()
"""


class File:
    def __init__(self, filename, mode, encoding=None):
        file_path = 'resource/' + filename
        # 打开文件
        self.f = open(file_path, mode, encoding=encoding)

    def read(self):
        return self.f.read()

    def write(self, content):
        self.f.write(content)

    def __del__(self):
        self.f.close()


file = File('demo01.txt', 'w+', 'utf-8')
file.write('人生得意须尽欢\n莫使金樽空对月\n')

file.f.seek(0)
print(file.read())
