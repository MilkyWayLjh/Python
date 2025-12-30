import pandas
import os
from pprint import pprint


class DataOperation:
    """
    读取.csv,xls,xlsx文件
    """
    def __init__(self, file_name):
        # 获取路径
        common_path = os.path.dirname(__file__)
        project_path = os.path.dirname(common_path)
        # 拼接路径
        full_path: str = os.path.join(project_path, 'data', file_name)     # : str 声明为字符串类型

        # 判断文件的类型是否是.csv格式
        if full_path.endswith('.csv'):
            self.data = pandas.read_csv(full_path)
        # 判断文件的类型是否是.xls格式
        elif full_path.endswith('.xls'):
            self.data = pandas.read_excel(full_path)
        # 判断文件的类型是否是.xlsx格式
        elif full_path.endswith('.xlsx'):
            self.data = pandas.read_excel(full_path)
        else:
            print('其它类型的文本暂时不读取')

    def common_get_data_to_list(self):
        """ 将文本的内容转为一个列表"""
        return self.data.values.tolist()

    def common_get_data_to_dict(self):
        """将文本数据转为字典"""
        return [self.data.loc[i].to_dict() for i in self.data.index.values]


if __name__ == '__main__':
    do = DataOperation("login_data.csv")
    pprint(do.common_get_data_to_list())
    pprint(do.common_get_data_to_dict())


