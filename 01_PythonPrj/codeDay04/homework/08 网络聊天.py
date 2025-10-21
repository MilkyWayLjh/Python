# 写一个后期网络聊天项目的模块，用户不断从键盘输入，每次输入回车后，打印用户输入的字符个数和内容，当用户输入`quit`后，退出该功能

print(f"{'*****' * 16} 欢迎来到镜像聊天室! {'*****' * 16}")
while True:
    word = input('请输入内容并回车: ')
    if word == 'quit' or word == 'exit':
        print('已退出聊天咯!')
        break
    print(f'内容: {word} ({len(word)}个字符)')
