"""
f.write(content) 一次性写入内容
f.writelines(list) 一次性写入多行
"""

# f.write(content) 一次性写入内容
"""
f = open('resource/test04.txt', 'w', encoding='utf8')
# f.write('123\n456\n789\n')
f.write('123\n')
f.write('456\n')
f.write('789\n')
f.close()
"""

# f.writelines(list) 一次性写入多行, 内容为列表
# """
f = open('resource/test04.txt', 'w', encoding='utf8')
f.writelines(['123\n', '456\n', '789\n'])
f.writelines(['123\n', '456\n', '789'])
f.close()
# """
