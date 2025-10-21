# 开发敏感词语过滤程序，提示用户输入内容，如果用户输入的内容中包含特殊的字符： 如 "手枪"等，将内容替换为 `*`
inp = input('请输入: ')
word = ['手枪', '杀', '血', '死']
for item in word:
    if item in inp:
        inp = inp.replace(item, '*' * len(item))    # 每次循环应该在原字符串上持续替换，确保每次替换的敏感词不被覆盖
print(inp)
