"""
pyperclip的主要用法有两个：
1、复制内容到剪贴板---pyperclip.copy("str")
2、粘贴剪贴板里的内容---pyperclip.paste()
"""
import pyperclip as pc


text = 'hello Kirin'
pc.copy(text)
print(pc.paste())

