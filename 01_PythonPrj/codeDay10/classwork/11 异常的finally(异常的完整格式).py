"""
finally表示的是无论是否异常都要执行的代码，例如关闭文件。
# 异常的完整格式
try:
    可能发生异常的代码
except 异常类型:
    发生异常执行的代码
else:
    没有异常的时候执行的代码
finally:
    无论是否异常都要执行的代码
"""
# 读取文件内容
try:
    print('正在读取...')
    f = open('resource/demo.txt', 'r', encoding='utf-8')
except Exception as e:
    print(f'FileNotFoundError: {e}')
    print('文件不存在, 即将创建默认文件, 请稍后再尝试...')
    f = open('resource/demo.txt', 'w', encoding='utf-8')
    f.write('我在佛前苦苦求了几千年!')
else:
    content = f.read()
    print('读取成功! 即将显示...')
    print(f'>>>{content}')
finally:
    f.close()
    print('文件已关闭')
