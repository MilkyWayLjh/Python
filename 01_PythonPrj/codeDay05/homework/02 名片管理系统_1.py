# 名片管理系统
"""
名片管理 系统

# 名片盒子  列表中存放字典,为什么要这样存放?为什么不是字典中存放列表?
cards = [
    {“name”:”张三”,”tel”:”17715154242”,”job”:”CEO”,”addr”:”天府新谷”,”company”:”源码时代”},  # 字典
    {名片信息2},
    {名片信息3}
]
需要完成的功能 就是对 名片盒子 进行增删改查
1. 添加名片: 根据用户录入的信息, 组装成字典 追加到名片盒子里面  cards.append(一个人的名片字典)
2. 显示所有名片: 遍历名片盒子输出名片信息
3. 修改名片:  录入需要修改名片的姓名, 根据名字到名片合子查找对应的哪一张名片,
    如果找到 , 重写录入新的名片信息, 完成修改操作
4. 删除名片: 录入需要删除名片的姓名, 根据名字到名片盒子中查到对应的名片并删除.
"""


def user_data():
    # 接收用户数据
    name = input('输入姓名: ')
    age = input('输入年龄: ')
    tel = input('输入手机号: ')
    return name, age, tel


def add():
    print('===>已切换到<添加名片>模块, 请开始操作~')
    # 接收用户数据, 调用user_data()并拆包
    name, age, tel = user_data()
    # 判断手机号是否重复(姓名可能重复，但手机号却是唯一的)
    for card_info in cards:
        while True:
            if card_info['tel'] == tel:
                print('===>手机号重复，请重新输入!')
                name, age, tel = user_data()
            else:
                break
    else:
        # 组装名片信息
        card_info = {
            'name': name,
            'age': age,
            'tel': tel
        }
        # 将每个名片添加到名片盒内
        cards.append(card_info)
        # 查看名片信息
        print(f'姓名\t\t年龄\t\t手机号')
        for card_info in cards:
            for info in card_info.values():
                print(info, end='\t\t')
            print()
        print('======= 添加成功! =======')


def show():
    print('===>已切换到<显示名片>模块, 请查看~')
    # 查看名片信息
    print(f'姓名\t\t年龄\t\t手机号')
    for card_info in cards:
        for info in card_info.values():
            print(info, end='\t\t')
        print()
    print('======= 没有更多了哦~ =======')
    # TODO 遗留优化问题：表格间距显示仍有问题,如输入 三字中文


def modify():
    print('===>已切换到<修改名片>模块, 请开始操作~')
    # 通过接收唯一手机号来修改用户名片信息
    tel = input('===>输入手机号进行查找: ')
    for card_info in cards:
        if card_info['tel'] == tel:
            print(f'姓名\t\t年龄\t\t手机号')
            print(f"{card_info['name']}\t\t{card_info['age']}\t\t{card_info['tel']}")
            print('===>对应的名片信息存在, 可以修改, 请操作~')
            # 修改新的信息
            name, age, tel = user_data()
            card_info['name'] = name
            card_info['age'] = age
            card_info['tel'] = tel
            print('======= 修改成功! =======')
            break
            # TODO 遗留优化问题：修改信息时，输入与其他名片相同的手机号 不允许修改的功能没有实现。且允许输入自己原来的手机号
    else:
        print('手机号不存在!')
        # TODO 遗留优化问题：如果手机号不存在，应提示重新输入，从而能再多次输入手机号进行查找 随后修改，而不是直接退回到选择功能的地方


def delete():
    print('===>已切换到<删除名片>模块, 请开始操作~')
    tel = input('===>输入手机号进行查找: ')
    for card_info in cards:
        if card_info['tel'] == tel:
            print(f'姓名\t\t年龄\t\t手机号')
            print(f"{card_info['name']}\t\t{card_info['age']}\t\t{card_info['tel']}")
            ack = input('===>对应的名片信息存在, 是否确认删除?(y/n): ')
            if ack == 'y':
                cards.remove(card_info)
                print('======= 删除成功! =======')
            else:
                print('===>已取消, 请重新选择功能~')


# 定义cards盒子 存储初始名片
cards = [
    {'name': '艾鲲', 'age': '20', 'tel': '123666'},
    {'name': '鹿人', 'age': '21', 'tel': '132666'},
    {'name': '黑子', 'age': '22', 'tel': '133666'}
]
fun_dict = {
    '1': add,
    '2': show,
    '3': modify,
    '4': delete
}

print(f"{'*****' * 15} 欢迎来到名片管理系统! {'****' * 20}")
while True:
    fun_id = input('请选择输入功能的序号[添加:1 | 显示:2 | 修改:3 | 删除:4 | 退出:其他字符]: ')
    if fun_id in fun_dict.keys():
        # pass
        fun_dict[fun_id]()
    else:
        print('没有此功能，退出系统!')
        break



