# 函数 参数的加强详解
"""
定义函数-参数
    必填参数（必需参数）：必须要传入对应的实参
    默认参数：带有默认值的参数就叫做默认参数，可以不传入实参
说明：
    必填参数必须写在默认参数的前面
"""


# 默认参数
# class_name:默认参数
def fn2(name, age, class_name='0825'):
    """
    输出学生信息
    :param name: 姓名
    :param age: 年龄
    :param class_name: 班级
    :return: 返回学生信息
    """

    print(name, age, class_name)


# 必填参数
def fn1(a, b):
    print(a, b)


"""
# 调用函数-参数
    位置参数：按照形参的位置传入参数
    关键字参数：按照形参名字传递参数
"""
# 位置参数
fn1(2, 1)

# 关键字参数
fn1(b=100, a=200)
