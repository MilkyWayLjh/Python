# https://www.runoob.com/w3cnote/python-understanding-dict-copy-shallow-or-deep.html

# Python 直接赋值、浅拷贝和深度拷贝解析
"""
直接赋值：其实就是对象的引用（别名）。
浅拷贝(copy)：拷贝父对象，不会拷贝对象的内部的子对象。
深拷贝(deepcopy)： copy 模块的 deepcopy 方法，完全拷贝了父对象及其子对象。
"""

"""
1: b = a: 赋值引用，a 和 b 都指向同一个对象。
2: b = copy.copy(a): 浅拷贝, a 和 b 是一个独立的对象，但他们的子对象还是指向统一对象（是引用）。
3: b = copy.deepcopy(a): 深度拷贝, a 和 b 完全拷贝了父对象及其子对象，两者是完全独立的。
"""

import copy

a = [1, 2, 3, 4, ['a', 'b']]  # 原始对象

b = a  # 赋值，传对象的引用
b1 = a[:]
c = copy.copy(a)  # 对象拷贝，浅拷贝
d = copy.deepcopy(a)  # 对象拷贝，深拷贝

a.append(5)  # 修改对象a
a[4].append('c')  # 修改对象a中的['a', 'b']数组对象

print('a = ', a)    # a = [1, 2, 3, 4, ['a', 'b', 'c'], 5]
print('b1 = ', b1)  # b1 = [1, 2, 3, 4, ['a', 'b', 'c']]
print('b = ', b)    # b = [1, 2, 3, 4, ['a', 'b', 'c'], 5]
print('c = ', c)    # c = [1, 2, 3, 4, ['a', 'b', 'c']]
print('d = ', d)    # d = [1, 2, 3, 4, ['a', 'b']]


