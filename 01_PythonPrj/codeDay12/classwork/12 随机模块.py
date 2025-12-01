import math
import random
"""
常用：
random.random()     [0, 1)
random.randint(a, b)    [a, b]
random.choice(seq)
random.sample(seq, k)
random.shuffle(seq)
"""

# 1 random.random()  生成一个0到1的随机浮点数：[0, 1)
print(random.random(), math.floor(random.random()*100))
num = '%.2f' % random.random()    # 小数位保留两位
print(num)

# 2 random.uniform(a, b)    生成[a, b]或[b, a]之间的均匀分布随机浮点数
print(random.uniform(1, 10))

# 3 random.randint(a, b)    生成[a, b]的随机整数，要求 a < b
print(random.randint(1, 10))

# 4 random.randrange(a, b[, step])    生成[a, b)的随机整数，第三个参数可以指定步长
print(random.randrange(1, 10))
print(random.randrange(1, 10, 2))

# 5 random.choice(seq)    从序列中随机选择一个元素，若序列为空，则抛出异常
print(random.choice(['python', 'mysql', 'linux']))
print(random.choice(('python', 'mysql', 'linux')))
print(random.choice('hello'))

# 6 random.shuffle(seq)     打乱原序列，原序列必须可写(即为list列表)
list1 = ['python', 'mysql', 'linux']
random.shuffle(list1)
print(list1)

# 7 random.sample(seq, k)      从序列中随机选择k个元素返回，原序列不变
list1 = ['python', 'mysql', 'linux', 'git', 'shell', 'zentao']
print(random.sample(list1, 2))
str1 = 'hello'
print(random.sample(str1, 2))

# 8 random.seed(n=none)     初始化随机熵池
random.seed(2)
print(random.randint(1, 10))

random.seed(5)
list1 = ['python', 'mysql', 'linux', 'git', 'shell', '禅道']
print(random.sample(list1, 2))

random.seed(None)
list1 = ['python', 'mysql', 'linux', 'git', 'shell', '禅道']
print(random.sample(list1, 2))


'''
round()函数
    -银行家舍入法（Banker's Rounding）：Python 采用这种舍入方式，也称为"四舍六入五取偶"
    -当小数部分恰好为 0.5 时，round() 函数会将数值舍入到最近的偶数
设计原因：
    这种舍入方式的主要优势是：
        减少累积误差：在大量计算中，传统的四舍五入会产生系统性偏差
        统计平衡：通过向最近偶数舍入，使得向上和向下舍入的概率更加均衡
这是 Python 遵循 IEEE 754 标准的浮点数舍入规则的体现，与其他编程语言（如 C、Java）的默认舍入行为可能不同。
'''
print(round(4.5))   # 结果为 4（向下舍入到偶数）
print(round(5.5))   # 结果为 6（向上舍入到偶数）
print(round(6.5))   # 结果为 6（向下舍入到偶数）
print(round(7.5))   # 结果为 8（向上舍入到偶数）

'''
math函数：
常用方法	        功能	        示例输入	输出
round(x)	    四舍五入	    3.7	    4
math.floor(x)	向下取整	    3.7	    3
math.ceil(x)	向上取整	    3.1	    4
int(x)	        向零取整	    3.7	    3
math.trunc(x)	截断小数	    3.7	    3
'''
