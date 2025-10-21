"""
python编写一个聊天记录保存功能，不断获取用户输入信息，保存到record.log文件
"""
print(f"{'*****' * 16} 欢迎来到聊天室! {'*****' * 16}")
user1, user2 = input('请输入聊天的两个人(以空格隔开): ').split()
print('聊天开始咯! 输入quit可以退出聊天哦!')
# f = open('source/record.log', 'a', encoding='utf-8')
# while True:
#     msg1 = input(f'{user1}说: ')
#     f.write(f'{user1}说: {msg1}\n')
#     msg2 = input(f'{user2}说: ')
#     f.write(f'{user2}说: {msg2}\n')
#     if msg1 == 'quit' or msg2 == 'quit':
#         print('已退出聊天咯! 内容已保存, 请前往source/record.log去查看聊天内容!')
#         break
# f.close()

with open('resource/record.log', 'a', encoding='utf-8') as f:
    while True:
        msg1 = input(f'{user1}说: ')
        if msg1 == 'quit':
            print('已退出聊天咯! 内容已保存, 请前往source/record.log去查看聊天内容!')
            break
        msg2 = input(f'{user2}说: ')
        if msg2 == 'quit':
            print('已退出聊天咯! 内容已保存, 请前往source/record.log去查看聊天内容!')
            break
        f.write(f'{user1}说: {msg1}\n')
        f.write(f'{user2}说: {msg2}\n')
