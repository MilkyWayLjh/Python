# complex(x) 将x转换到一个复数，实数部分为 x，虚数部分为 0。
# complex(x, y) 将 x 和 y 转换到一个复数，实数部分为 x，虚数部分为 y。x 和 y 是数字表达式。
c = complex(2)
z = complex(2, 1)
print(c, z)

# 以下几个内置的函数可以执行数据类型之间的转换。这些函数返回一个新的对象，表示转换的值。
# int(x [,base])  将x转换为一个整数
# float(x)    将x转换到一个浮点数
# complex(real [,imag])   创建一个复数
# str(x)  将对象 x 转换为字符串
# repr(x)     将对象 x 转换为表达式字符串
# eval(str)   用来计算在字符串中的有效Python表达式,并返回一个对象
# tuple(s)    将序列 s 转换为一个元组
# list(s)     将序列 s 转换为一个列表
# set(s)      转换为可变集合
# dict(d)     创建一个字典。d 必须是一个 (key, value)元组序列。
# frozenset(s)    转换为不可变集合
# chr(x)  将一个整数转换为一个字符
# ord(x)      将一个字符转换为它的整数值
# hex(x)      将一个整数转换为一个十六进制字符串
# oct(x)      将一个整数转换为一个八进制字符串

# 数学函数
# abs(x)	返回数字的绝对值，如abs(-10) 返回 10
# ceil(x)	返回数字的上入整数，如math.ceil(4.1) 返回 5
# exp(x)	返回e的x次幂(ex),如math.exp(1) 返回2.718281828459045
# fabs(x)	返回数字的绝对值，如math.fabs(-10) 返回10.0
# floor(x)	返回数字的下舍整数，如math.floor(4.9)返回 4
# log(x)	如math.log(math.e)返回1.0,math.log(100,10)返回2.0
# log10(x)	返回以10为基数的x的对数，如math.log10(100)返回 2.0
# max(x1, x2,...)	返回给定参数的最大值，参数可以为序列。
# min(x1, x2,...)	返回给定参数的最小值，参数可以为序列。
# modf(x)	返回x的整数部分与小数部分，两部分的数值符号与x相同，整数部分以浮点型表示。
# pow(x, y)	x**y 运算后的值。
# round(x [,n])   返回浮点数 x 的四舍五入值，如给出 n 值，则代表舍入到小数点后的位数。其实准确的说是保留值将保留到离上一位更近的一端。
# sqrt(x)	返回数字x的平方根。

# 随机数函数
# choice(seq)	从序列的元素中随机挑选一个元素，比如random.choice(range(10))，从0到9中随机挑选一个整数。
# randrange ([start,] stop [,step])	从指定范围内，按指定基数递增的集合中获取一个随机数，基数默认值为 1
# random()	随机生成下一个实数，它在[0,1)范围内。
# seed([x])	改变随机数生成器的种子seed。如果你不了解其原理，你不必特别去设定seed，Python会帮你选择seed。
# shuffle(lst)	将序列的所有元素随机排序
# uniform(x, y)	随机生成下一个实数，它在[x,y]范围内。
import random
a = random.random()
print(a)
