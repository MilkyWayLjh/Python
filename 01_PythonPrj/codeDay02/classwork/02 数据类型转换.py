# int  只能转换整型字符串, 浮点数, 布尔类型
print(int('100'))
print(int(10.1))
print(int(True))
print(int(False))
# print(int('100a'))  # 不能转化
# print(int('a'))  # 不能
# print(int('10.1'))  # 不能


# float 整数，整数字符串，浮点数字符串, 布尔类型
print(float(10))
print(float('10'))
print(float('10.1'))
print(float(True))
print(float(False))


# str 数字，布尔，None
print(str(10))
print(str(10.11))
print(str(True))
print(type(str(True)))  # 'True'
print(str(False))  # 'False'
print(str(None))  # 'None'

print('***' * 20, '个人练习', '***' * 20)

# int型
str1 = '123'
print(int(str1), type(int(str1)))

# int转换的字符串，必须是包裹的整数类型
str2 = 'abc'
# print(int(str2), type(int(str2)))       # 报错,字符串无法转换类型转换为int

float1 = 7.2
print(int(float1), type(int(float1)))   # 将浮点数转化为int

bool1 = True
print(int(bool1))    # bool类型转化为int,输出结果为1
bool2 = False
print(int(bool2))    # bool类型转化为int,输出结果为0

# float型
float1 = 12.1
num1 = int(float1)
print(type(num1), num1)


# 将bool转化为int
bool1 = True  # 1
bool2 = False  # 0

# float()
# 其他数据类型转化为float
# 字符串转float

str1 = '12.1'
float1 = float(str1)
print(type(float1), float1)             # 字符串类型转换为float

# float转换的字符串，必须是包裹的数字类型
str2 = 'abc'
# float2 = float(str2)                    # 报错，字符串无法转换类型转换为float

# 整数转float
str3 = '12'
float3 = float(str3)
print(type(float3), float3)             # 输出结果为12.0

# str()
num1 = 1
print(type(str(num1)), str(num1))       # int类型转换为str类型

# float -> str
print(type(str(1.1)), str(1.1))         # float类型转换为str类型

# bool -> str
print(type(str(True)), str(True))    # bool类型转换为str类型
print(type(str(False)), str(False))  # bool类型转换为str类型

"""
案例：
通过键盘录入： 每天卖出多少碗面
通过键盘录入： 每碗面多少块
通过键盘录入： 今年共营业多少天
计算并且输出一年的总售额。
"""
# 接收用户输入  类型转化
amount = int(input('每天面的数量: '))
price = float(input('面的单价: '))
days = int(input('今年营业天数: '))
print(price * amount * days)           # 计算结果
