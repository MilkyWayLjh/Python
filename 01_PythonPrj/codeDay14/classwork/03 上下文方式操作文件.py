# 打开文件
# 操作文件
# 关闭文件


# 上下文管理器对象
# with语句用来操作上下文管理器对象
"""
语法：
with 打开文件 as f:
    # 文件操作
    f.write()
    f.read()
特点：
在代码块执行完毕之后，自动关闭资源
"""
with open('resource/demo.txt', 'w+', encoding='utf8') as f:
    # 文件操作
    f.write('hello python')
    f.seek(0)
    content = f.read()
    print(content)

# 在代码块with语句外也能访问
print(content)

