# 定义一个元组
info = ('hello', 18, '成都省高天市')

# 元组拆包  (给多个变量赋值)
name, age, address = info
print(name, age, address)

# 列表拆包
name, age, address = list(info)
print(name, age, address)

a, b, c = 'god'
print(a, b, c)

# 注意：
#    变量个数和后面的元素个数一一对应
