# 1 山高800米，板厚0.5米，请问对折几次板(x2) 板的厚度超过山
height, thickness, count = 800, 0.5, 0
while True:
    if thickness >= height:
        break
    else:
        thickness *= 2
        count += 1
print(thickness, count)  # 1024.0 11

# 2 已知列表 i = ['1', 3, '5', 7, '9', 2, '4', 6, '8', 10],
#   请首先排除字符串，并按照降序排列，最后切片得到[2, 7]
i = ['1', 3, '5', 7, '9', 2, '4', 6, '8', 10]
for item in i:
    if type(item) == str:
        i.remove(item)

print(i)  # [3, 7, 2, 6, 10]
i.sort(reverse=True)
print(i)  # [10, 7, 6, 3, 2]
print(i[::-3])  # [2, 7]


# 3 看下面代码，写出答案
# li = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(li[0::-3])      # [1]
def fn(a, b, c=None, *args, **kwargs):
    _sum = 1
    for m in args:
        _sum *= m
    for n in kwargs.values():
        _sum += n
    return _sum - a - b
print(fn(1, 2, 3, 4, n1=18, n2=20))     # 39


# 4 看下面代码写出执行结果。（有错报错，没错说出结果）
class Cat:
    name = 'Tom'
    __age = 3

    def run(self):
        return self.name + '正在跑'

    def __listen(self):
        return self.name + '正在听'


class Dog:
    name = 'XiaoHei'
    __age = 4

    def run(self):
        return self.name + '正在跑'

    def __watch(self):
        return self.name + '正在看'


class Zoo(Dog, Cat):
    def run(self):
        return super(Zoo, self).run()

    def animal(self):
        return super(Zoo, self)._Cat__listen()

    def fn1(self, num):
        self.age = num  # 相当于对象自己给自己设置了一个age，只是没有在__init__()里面设置而已

c1 = Cat()
print(c1.name)  # Tom
# print(c1.age)   # 报错 AttributeError: 'Cat' object has no attribute 'age'
print(c1.run())   # Tom正在跑

z1 = Zoo()
z1.fn1(10)

print(z1.name)  # XiaoHei
print(z1.age)   # 10
print(z1.run())     # XiaoHei正在跑
print(z1.animal())    # XiaoHei正在听


# 5 什么是单例模式？请定义1个 单例类People，具备以下功能：
"""
a.使用初始化方法，实例化一个对象p1，name为'哈哈哥'，age为18
b.People类有一个change_info(name2, age2)方法，p1调用此方法，name改为'呵呵妹'，age改为20
c.print(p1)的时候，控制台输出p1的自我介绍，'大家好,我叫xxx,今年xx岁'
d.del p1的时候，控制台输出 'xxx消失了'
"""


class People:
    # 保存创建好的对象
    __instance = None
    # 是否已经初始化
    __has_init = False

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super().__new__(cls, *args, **kwargs)
        return cls.__instance

    def __init__(self):
        if not self.__has_init:
            self.name = '哈哈哥'
            self.age = 18
            self.__has_init = True

    def change_info(self, name2, age2):
        self.name = name2
        self.age = age2

    def __str__(self):
        return f'大家好，我叫{self.name}，今年{self.age}岁'

    # def __del__(self):
    #     print(f'{self.name}消失了')

p1 = People()
print(p1)
# p2 = People()
# print(p2)
p1.change_info('呵呵妹', 20)
print(p1)
# del p1
print('本程序最后一行')


# 6 已知列表[1, 3, 5, 7, 9], 请使用列表推导式得到列表 [109, 107, 105, 103, 101]
print([i + 100 for i in [1, 3, 5, 7, 9][::-1]])


# 7 什么是装饰器？请为下列函数添加一个装饰器，装饰器生成一个1-10的随机数，如果随机数大于5则抛出异常，小于5则正常执行。
"""
def fn():
    pass
fn()
"""
import random


class NumError(Exception):
    def __str__(self):
        return 'NumError: 随机数大于5!'


def decorator(f):
    def inner(*args, **kwargs):
        num = random.randint(1, 10)
        try:
            if num > 5:
                raise NumError()
            else:
                return f(*args, **kwargs)
        except NumError as e:
            return e

    return inner


@decorator
def fun():
    return '随机数小于5，正常执行!'

print(fun())

# 8 简述python变量名查找原则LEGB？并说出查找顺序。
"""
作用域链：变量名解析LEGB法则:
        当在函数中使用未确定的变量名时，Python会按照优先级依次搜索4个作用域，以此来确定该变量名的意义。
        首先搜索局部作用域(Local)，之后是上一层嵌套结构中def或lambda函数的嵌套作用域(Enclosing)，之后是全局作用域(Global)，最后是内置作用域(Built-in)。
        按这个查找原则，在第一处找到的地方停止。如果没有找到，则会出发NameError错误。
搜索变量名的优先级(查找顺序)：局部作用域 > 嵌套作用域 > 全局作用域 > 内置作用域
"""


# 9 定义一个Fn类，具备实例方法、类方法、静态方法功能
"""
1.实例方法：fn1(num1, num2) 控制台输出 num1+num2 的和
2.类方法：fn2(name, age) 控制台输出 '名字：xxx，年龄：xx'
3.静态方法：fn3() 控制台输出 九九乘法表 (for循环版)
"""


class Fn:
    def fn1(self, num1, num2):
        print(num1 + num2)

    @classmethod
    def fn2(cls, name, age):
        print(f'名字：{name}，年龄：{age}')

    @staticmethod
    def fn3():
        for a in range(1, 10):
            for b in range(1, a+1):
                print(f'{b}x{a}={a * b}', end='\t')
            print()

Fn().fn1(1, 1)
Fn.fn2('李四', 18)
Fn.fn3()


# 10 已知存在文件data.txt, 请写一个函数具备以下功能。
"""
1.按行读取data.txt
2.如果在文本内容中发现以下内容 words = ['抢劫', '偷盗', '杀人'] 即替换为 *
3.在文本尾部追加 '已审核2022-10-10 10:10:10', 主要这儿要写获取当前时间的代码，不是固定的时间
4.将修改好的内容写入 data_check.txt 文件中
"""
from datetime import datetime


def file():
    """
    # 文件普通操作方式
    f = open('resource/data.txt', 'r', encoding='utf-8')
    content = f.readlines()
    li, words = [], ['抢劫', '偷盗', '杀人']
    for item1 in content:
        for word in words:
            if word in item1:
                item1 = item1.replace(word, '*' * len(word))
        li.append(item1)
    datetime_obj = datetime.now()
    datetime_str = datetime_obj.strftime('%Y-%m-%d %H:%M:%S')
    li.append('已审核' + datetime_str)
    li_str = ''.join(li)
    f1 = open('resource/data_check.txt', 'w', encoding='utf-8')
    f1.write(li_str)
    f1.close()
    f.close()
    """
    # with语句来操作上下文管理器对象
    with open('resource/data.txt', 'r', encoding='utf-8') as f:
        content = f.readlines()
        li, words = [], ['抢劫', '偷盗', '杀人']
        for item1 in content:
            for word in words:
                if word in item1:
                    item1 = item1.replace(word, '*' * len(word))
            li.append(item1)
        datetime_obj = datetime.now()
        datetime_str = datetime_obj.strftime('%Y-%m-%d %H:%M:%S')
        li.append('已审核' + datetime_str)
        li_str = ''.join(li)
        with open('resource/data_check.txt', 'w', encoding='utf-8') as f1:
            f1.write(li_str)

file()





