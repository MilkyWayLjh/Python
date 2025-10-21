"""
定义一个文件操作类File，方法有：读取所有内容，读取数据按行返回，写入内容，追加数据。
有以下类方法：
    File.read(文件名)
    File.readlines(文件名)
    File.write(文件名,’内容’)
    File.append(文件名,’内容’)
"""


class File:
    # 读取所有内容
    @staticmethod
    def read(filename):
        # 打开文件
        f = open(f'resource/{filename}', 'r', encoding='utf-8')
        # 读取全部文件
        content = f.read()
        # 关闭文件
        f.close()
        return content

    # 写入内容
    @staticmethod
    def write(filename, content):
        # 打开文件
        f = open(f'resource/{filename}', 'w', encoding='utf-8')
        # 写入文件
        f.write(content)
        # 关闭文件
        f.close()
        print('写入成功')

    # 读取数据按行返回
    @staticmethod
    def readlines(filename):
        # 打开文件
        f = open(f'resource/{filename}', 'r', encoding='utf-8')
        # 读取每行文件
        content_list = f.readlines()
        # 关闭文件
        f.close()
        return content_list

    # 追加数据
    @staticmethod
    def append(filename, content):
        # 打开文件
        f = open(f'resource/{filename}', 'a', encoding='utf-8')
        # 追加文件
        f.write(content)
        # 关闭文件
        f.close()
        print('追加成功')


# 建议用类名访问静态方法
File.write('demo01.txt', '天高任鸟飞\n只因你太美\n')
print(File.read('demo01.txt'))
File.append('demo01.txt', '肉食者鄙\n未能远谋\n')
print(File.readlines('demo01.txt'))

print(File.read('demo01.txt'))
