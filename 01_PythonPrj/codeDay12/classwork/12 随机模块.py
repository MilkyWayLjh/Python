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
print(random.random())
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


