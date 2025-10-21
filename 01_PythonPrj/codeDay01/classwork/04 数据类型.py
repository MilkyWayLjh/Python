"""
数据类型
  基本数据类型
      Number数字型 --> int(有符号整型) float(浮点型) complex(复数)
      String字符型 --> 单引号/双引号  三单引号/三双引号
      Boolean布尔型 --> True False
  容器数据类型
      List列表
      Tuple元组
      Dictionary字典
      Set集合

Python3 的六个标准数据类型中：
    不可变数据（3 个）：Number（数字）、String（字符串）、Tuple（元组）；
    可变数据（3 个）：List（列表）、Dictionary（字典）、Set（集合）。
注意：Python3 中，bool 是 int 的子类，True 和 False 可以和数字相加， True==1、False==0 会返回 True，但可以通过 is 来判断类型。
"""
# type() 检测数据类型函数
print(type(1))
print(type(1.1))
print('''
            woshi 
            ikun
            ''')
print(type('''
            woshi 
            ikun
            '''))
print(type(False))

age, str1 = 22, '22'
print(age == str1)
print(type(age == str1))

'''
isinstance 和 type 的区别在于：
type()不会认为子类是一种父类类型。
isinstance()会认为子类是一种父类类型。
'''
a = 11
print(isinstance(a, int))  # True
