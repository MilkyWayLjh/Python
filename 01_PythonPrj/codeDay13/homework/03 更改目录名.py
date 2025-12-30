# 将`resource`目录下的目录名字改为`day01, day02,..., day09, day10...`
import os
import re

# 先创建目录
os.mkdir('resource')
for i in range(1, 14):
    os.mkdir('resource/day' + str(i))

# 1 使用正则
for item in os.listdir('resource'):
    if item.startswith('day') and len(item) == 4:
        filename = re.search('^(day)([1-9])', item).groups()
        # print(filename, filename[0], filename[1])
        os.rename('resource/' + item, 'resource/' + filename[0] + '0' + filename[1])

# 2 字符串 切片 索引，强行rename
for item in os.listdir('resource'):
    if len(item) == 4:
        os.rename('resource/' + item, 'resource/' + item[:3] + '0' + item[3])

# 3 字符串转列表，列表插入0，再列表转字符串
for item in os.listdir('resource'):
    if len(item) == 4:
        li = list(item)
        li.insert(3, '0')
        name = ''.join(li)
        os.rename('resource/' + item, 'resource/' + name)

print(os.listdir('resource'))
