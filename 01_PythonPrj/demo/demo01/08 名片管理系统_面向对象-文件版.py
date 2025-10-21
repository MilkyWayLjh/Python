class CardsSystem:
    def __init__(self):
        # 定义功能序号的字典，存储相关函数
        self.fun_dict = {
            '1': self.add,
            '2': self.show,
            '3': self.modify,
            '4': self.delete,
            '0': self._quit
        }

    @staticmethod
    def input_data():
        # 接收用户数据
        name = input('输入姓名: ')
        age = input('输入年龄: ')
        tel = input('输入手机号: ')
        return name, age, tel

    def add(self):
        # 从文件中读取名片内容
        cards = self.read_cards()

        print('===>已切换到<添加名片>模块, 请开始操作~')
        # 接收用户数据, 调用input_data()并拆包
        name, age, tel = self.input_data()
        # 判断手机号是否重复(姓名可能重复，但手机号却是唯一的)
        for card_info in cards:
            while True:
                if card_info['tel'] == tel:
                    print('===>手机号重复，请重新输入!')
                    name, age, tel = self.input_data()
                else:
                    break
        else:
            # 存储名片信息
            card_info = {'name': name, 'age': age, 'tel': tel}
            # 将每个名片添加到名片盒内
            cards.append(card_info)
            # 查看名片信息
            print(f'姓名\t\t年龄\t\t手机号')
            for card_info in cards:
                for info in card_info.values():
                    print(info, end='\t\t')
                print()
            print('======= 添加成功! =======')

        # 将cards写入文件
        self.write_cards(cards)

    # 定义显示名片函数
    def show(self):
        # 从文件中读取名片内容
        cards = self.read_cards()

        print('===>已切换到<显示名片>模块, 请查看~')
        # 查看名片信息
        print(f'姓名\t\t年龄\t\t手机号')
        for card_info in cards:
            for info in card_info.values():
                print(info, end='\t\t')
            print()
        print('======= 没有更多了哦~ =======')

    # 定义修改名片函数
    def modify(self):
        # 从文件中读取名片内容
        cards = self.read_cards()

        # 通过接收唯一手机号来修改用户名片信息
        tel = input('===>输入手机号进行查找: ')
        for card_info in cards:
            if card_info['tel'] == tel:
                print(f'姓名\t\t年龄\t\t手机号')
                print(f"{card_info['name']}\t\t{card_info['age']}\t\t{card_info['tel']}")
                print('===>对应的名片信息存在, 可以修改, 请操作~')
                # 修改新的信息
                name, age, tel = self.input_data()
                # 清空字典（自身），确保自身的 'tel' 键不会被遍历和判断到
                card_info.clear()
                # 重新遍历盒子内容，判断手机号是否相等，不相等则无限重新输入，直到手机号不重复
                for info in cards:
                    while True:
                        # if info['tel'] == tel:
                        if info.get('tel') == tel:
                            print('===>手机号重复，请重新修改!')
                            name, age, tel = self.input_data()
                        else:
                            break
                # 重新填充 修改新的信息
                card_info['name'] = name
                card_info['age'] = age
                card_info['tel'] = tel
                print('======= 修改成功! =======')
                break
        else:
            print('手机号不存在!')

        # 将cards写入文件
        self.write_cards(cards)

    # 定义删除名片函数
    def delete(self):
        # 从文件中读取名片内容
        cards = self.read_cards()

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
                break
        else:
            print('手机号不存在!')

        # 将cards写入文件
        self.write_cards(cards)

    @staticmethod
    def _quit():
        print('退出系统!')
        exit(0)

    # 定义读取卡片操作
    @staticmethod
    def read_cards():
        # 从文件中以行的形式读取所有内容
        f = open('resource/cards.txt', 'r', encoding='utf8')
        cards_list = f.readlines()
        f.close()

        # 遍历所有行，将字符串转化为列表字典形式
        result = []  # 准备返回的结果
        for card_str in cards_list:
            # 将字符串先取出掉最右侧的\n,然后再用逗号分割列表
            card_list = card_str.rstrip('\n').split(',')
            # 将列表拼接为名片格式的字典
            card_dict = {"name": card_list[0], "age": card_list[1], "tel": card_list[2]}
            # 将字典追加到结果列表中
            result.append(card_dict)
        return result

    # 定义写入卡片操作
    @staticmethod
    def write_cards(cards_list):
        # 打开文件
        f = open('resource/cards.txt', 'w', encoding='utf8')
        # 操作文件
        for card_dict in cards_list:
            # 将字典中的所有value转化为类列表，然后字符串join拼接为字符串
            card_str = ','.join(card_dict.values()) + '\n'
            f.write(card_str)

        # 关闭文件
        f.close()

    def main(self):
        print(f"{'*****' * 15} 欢迎来到名片管理系统! {'****' * 20}")
        while True:
            fun_id = input('请选择输入功能的序号[添加:1 | 显示:2 | 修改:3 | 删除:4 | 退出:0]: ')
            if fun_id in self.fun_dict.keys():
                self.fun_dict[fun_id]()
            else:
                print('没有此功能! 请重新选择功能序号[0-4]')


card_sys = CardsSystem()
card_sys.main()
