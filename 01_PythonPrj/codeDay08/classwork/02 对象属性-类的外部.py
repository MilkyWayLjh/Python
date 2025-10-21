# 定义类
class Person:
    pass


# 创建对象
p1 = Person()

# 设置对象属性
p1.name = 'hello'

# 修改对象属性
p1.name = '你好'

# 查看对象属性
print(p1.name)

# 删除对象属性
del p1.name
# print(p1.name)

# 判断属性是否存在或者是属性是否有值
#   hasattr(对象,”属性名称”)
#   返回值: bool 存在True 不存在False
print(hasattr(p1, 'name'))  # False
p1.name = 'hello'
print(hasattr(p1, 'name'))  # True
