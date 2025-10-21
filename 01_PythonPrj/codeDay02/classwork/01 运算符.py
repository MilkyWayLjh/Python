a, b = 21, 10

# 算数运算符
print(a + b)    # 加---31
print(a - b)    # 加减---11
print(a * b)    # 乘---210
print(a / b)    # 除---2.1
print(a ** b)    # 幂---21^10
print(a % b)    # 取余---1
print(a // b)    # 整除---2
print(2 ** -1)
print(4 ** 0.5)
print(8 ** (1/3))

print('===' * 20)

# 比较运算符
print(a == b)   # 是否等于
print(a != b)   # 是否不等于
print(a > b)   # 是否大于
print(a < b)   # 是否小于
print(a >= b)   # 是否大于等于
print(a <= b)   # 是否小于等于

print('===' * 20)

# 赋值运算符
c = a + b   # 赋值
print(c)
c += a   # +赋值 c = c + a
print(c)
c -= a   # -赋值 c = c - a
print(c)
c *= a   # *赋值 c = c * a
print(c)
c /= a   # /赋值 c = c / a
print(c)
c %= a   # %赋值 c = c % a
print(c)
c //= a   # //赋值 c = c // a
print(c)
c **= a   # **赋值 c = c ** a
print(c)

print('===' * 20)

# 身份运算符
name1 = '张三'
name2 = '张三'
print(id(name1))    # 打印name1的内存地址
print(id(name2))    # 打印name2的内存地址
print(name1 is name2)   # 判断 name1 和 name2 的内存地址是否一致 --- True

names1 = ['张三', '李四']
names2 = ['张三', '李四']
print(id(names1))    # 打印names1的内存地址
print(id(names2))    # 打印names2的内存地址
print(names1 is names2)   # 判断 names1 和 names2 的内存地址是否一致 --- False
print(names1 is not names2)   # 判断 names1 和 names2 的内存地址是否一致 --- True

print('===' * 20)

# 逻辑运算符
# and
print(1 and 'a')    # 'a'
print(1 and 0)    # 0
print(1 and '')    # ''
print(1 and None)    # None
print('---' * 20)
# or
print(1 or 'a')    # 1
print(0 or 'a')    # 'a'
print(0 or '')    # ''
print(1 or None)    # 1
print('' or None)    # None
print('---' * 20)
# not
print(not 1)    # False
print(not 0)    # True
print(not '')    # True
print(not '0')    # False

print('===' * 20)

if a != b:
    print('a和b不相等')

if a is not b:
    print('a和b不相等')

if a not in [1, 2, 3]:
    print('a不在列表中')
