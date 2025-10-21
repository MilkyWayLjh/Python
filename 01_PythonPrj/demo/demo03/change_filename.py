# 修改`resource`目录下的文件名字
import os
import re

# 先创建目录和文件
os.mkdir('resource')
for i in range(1, 63):
    file = open('resource/img' + str(i) + '.jpg', 'w')
    file.close()

# 1 字符串 切片 索引，强行rename
i = 1
for item in os.listdir('resource'):
    if item.startswith('img'):
        os.rename('resource/' + item, 'resource/' + 'img-' + str(i) + '.jpg')
    i += 1

# 2 使用正则 rename
for item in os.listdir('resource'):
    if item.startswith('img') and len(item) == 9:
        filename = re.search('^(img-)([1-9])', item).groups()
        # print(filename, filename[0], filename[1])
        os.rename('resource/' + item, 'resource/' + filename[0] + '0' + filename[1] + '.jpg')
