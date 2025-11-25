import os


class File:
    # 读取文件内容
    @staticmethod
    def read(file):
        f = open('resource/' + file, 'r', encoding='utf-8')
        content = f.read()
        f.close()
        return content

    # 写入内容到文件中
    @staticmethod
    def write(file, content):
        f = open('resource/' + file, 'w', encoding='utf-8')
        f.write(content)
        f.close()
        print('写入成功!')

    # 复制文件
    @staticmethod
    def copy(file):
        f = open('resource/' + file, 'rb')
        filename, extension = os.path.splitext(file)
        new_f = open('resource/' + filename + '-副本' + extension, 'ab')
        while True:
            content = f.read(1024)
            new_f.write(content)
            if not content:
                break
        f.close()
        new_f.close()

    # 删除文件
    @staticmethod
    def delete(file):
        os.remove('resource/' + file)

    # 文件改名
    @staticmethod
    def rename(file, new_file):
        os.rename('resource/' + file, 'resource/' + new_file)


# 魔术变量 __all__
__all__ = ['File']

# 魔术变量 __name__
#   第一种：当前模块当作脚本执行，__name__的值：__main__
#   第二种：当前模块当作模块被调用执行，__name__的值：当前模块名 (file)
print(__name__)
if __name__ == '__main__':
    print('file执行了')
    # File.write('demo.txt', '千呼万唤始出来\n犹抱琵琶半遮面\n')
    print(File.read('demo.txt'))
    # File.copy('demo.txt')
    # File.rename('demo-副本-副本.txt', 'demo01.txt')
    # File.delete('demo01.txt')
