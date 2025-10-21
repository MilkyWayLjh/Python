# 文件操作类-面向对象版本
class File:
    def __init__(self, file_path, mode, encoding=None):
        filename = 'resource/' + file_path
        # 打开文件
        self.f = open(filename, mode, encoding=encoding)

    def read(self):
        return self.f.read()

    def write(self, content):
        self.f.write(content)

    def __del__(self):
        self.f.close()

file = File('demo01.txt', 'w', 'utf-8')
file.write('人生得意须尽欢\n莫使金樽空对月\n')
# print(file.read())

