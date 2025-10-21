"""
目录操作模块有以下功能：
    创建目录
    删除目录（空目录或非空目录）
    查找目录中是否存在某个文件
"""
import os
# import shutil


class Directory:
    # 创建目录
    @staticmethod
    def create_dir(dirname):
        os.mkdir(dirname)

    # 删除目录（空目录或非空目录）
    @staticmethod
    def del_dir(dirname):
        # shutil.rmtree(dirname)
        try:
            os.rmdir(dirname)
        except Exception as e:
            print(f'{e}>>>即将强制递归删除以下文件...')
            file_list = os.listdir(dirname)
            print(file_list)
            for file in file_list:
                # file_path = f'{dirname}\\{file}'
                file_path = f'{dirname}/{file}'
                if os.path.isdir(file_path):
                    Directory.del_dir(file_path)
                else:
                    os.remove(file_path)
            else:
                os.rmdir(dirname)

    # 查找目录中是否存在某个文件
    @staticmethod
    def is_exit_file(dirname, filename):
        file_list = os.listdir(dirname)
        print(file_list)
        """
        for file in file_list:
            if file == filename:
                return True
        else:
            return False
        """
        return filename in file_list


# Directory.create_dir('dir')
# Directory.create_dir('dir/dir1')
# Directory.create_dir('dir/dir1/dir2')
# Directory.del_dir('dir')
# Directory.del_dir('dir1')
print(Directory.is_exit_file('dir', 'test01.txt'))
print(Directory.is_exit_file('dir', 'test06.txt'))
print(Directory.is_exit_file('dir/dir1/dir2', 'test06.txt'))

