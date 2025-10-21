# 索引
str1 = 'hello'
print(str1[1])
# str1[2] = 'e'   #字符串不能修改

print('==' * 20)

# 切片
print(str1[::-1])  # 字符串反转
print(str1[:])  # 复制
print('==' * 20)

# 遍历
i = 0
while i < len(str1):
    print(str1[i])
    i += 1

print('==' * 20)

# 数据类型（可变/不可变）：
# 可变数据类型
"""
list    dict    set
"""
# 不可变数据类型
"""
int,float
bool
str
tuple
None
"""
