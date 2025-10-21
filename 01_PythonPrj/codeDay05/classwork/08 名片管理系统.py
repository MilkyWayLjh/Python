"""
名片管理 系统

# 名片盒子  列表中存放字典,为什么要这样存放?为什么不是字典中存放列表?
cards = [
    {“name”:”张三”,”tel”:”17715154242”,”job”:”CEO”,”addr”:”天府新谷”,”company”:”源码时代”},  # 字典
    {名片信息2},
    {名片信息3}
]
需要完成的功能 就是对 名片盒子 进行增删改查
1. 添加名片: 根据用户录入的信息, 组装成字典 追加到名片盒子里面
2. 显示所有名片: 遍历名片盒子输出名片信息
3. 修改名片:  录入需要修改名片的姓名, 根据名字到名片合子查找对应的哪一张名片,
    如果找到 , 重写录入新的名片信息, 完成修改操作
4. 删除名片: 录入需要删除名片的姓名, 根据名字到名片盒子中查到对应的名片并删除.
"""

# 名片存储
cards = [
    {'name': '张三', 'age': 18, 'tel': 111111}
]

while True:
    code = input('选择功能[1添加|2显示|3修改|4删除]: ')
    if code == '1':
        print('====添加名片====')
        # 接收用户数据
        name = input('姓名：')
        age = input('年龄：')
        tel = input('手机：')
        # 组装名片信息
        card_info = {'name': name, 'age': age, 'tel': tel}
        # 添加到列表中[名片盒]
        cards.append(card_info)
        print(cards)
        print('添加成功')
    elif code == '2':
        print('====查看名片====')
        print(f'姓名\t年龄\t手机号')
        for card_info in cards:
            for info in card_info.values():
                print(info, end='\t')
            print()
    elif code == '3':
        print('====修改名片====')
        # 接收要修改的姓名
        name = input('要修改名片的姓名：')
        for card_info in cards:
            if card_info['name'] == name:
                # 新的信息
                name = input('姓名：')
                age = input('年龄：')
                tel = input('手机：')
                card_info['name'] = name
                card_info['age'] = age
                card_info['tel'] = tel
                print('修改完成')
                break
        else:
            print('姓名不存在')

    elif code == '4':
        print('====删除名片====')
        name = input('请输入需要删除名片的姓名：')
        for card_info in cards:
            if card_info['name'] == name:
                # del cards[cards.index(card_info)]
                cards.remove(card_info)
                print('删除成功')
    else:
        print('退出系统')
        break
