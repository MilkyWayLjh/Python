# 按照以下需求，封装一个函数
# 1.1 设计一个功能从键盘获取用户的姓名、性别、家庭地址
# 1.2 打印从该功能中获取的信息

def info():
    name = input('请输入姓名: ')
    sex = input('请输入性别: ')
    address = input('请输入家庭地址: ')
    return name, sex, address

# print(info())      # 打印结果是 一个元组
# print(info()[0])    # 通过索引调用并访问单个
name1, sex1, address1 = info()     # 调用info() 元组拆包
print(f'姓名: {name1}, 性别: {sex1}, 家庭地址: {address1}')
