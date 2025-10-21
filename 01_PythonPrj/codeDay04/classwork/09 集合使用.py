# 集合（set）是一个 无序的 不重复 元素序列(容器)。
# 可以使用大括号 { } 或者 set() 函数创建集合，
# 注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。

# 定义集合 set
# 简单方式
set1 = {'python', 'mysql', 'linux'}
print(type(set1))   # <class 'set'>
# set1 = {}   # {}不能创建空集合
set1 = {}
print(type(set1))   # <class 'dict'>
# 注意：{}表示字典，不是集合

# 函数方式
set2 = set('hello')
set3 = set(['python', 'mysql', 'linux'])
set4 = set(('python', 'mysql', 'linux'))
print(set2)
print(set3)
print(set4)

# 集合操作
# 随机增加与删除
print(set4.pop())
print(set4)
set4.add('git')
print(set4)

# 集合特点：
# 1. 集合是无序的，没有索引
# 2. 集合元素是唯一的。去重。


# 基本功能是进行成员关系测试和删除重复元素（去重）。
set5 = {'Google', 'Hello', 'Facebook', 'Spider', 'Baidu'}
print(set5)   # 输出集合，重复的元素被自动去掉

# 成员测试
if 'Hello' in set5:
    print('Hello 在集合中')
else:
    print('Hello 不在集合中')

# set可以进行集合运算
a = set('fjoawjfjaskdjfiw')
b = set('wfoijadkfaj')
print(a)
print(a - b)     # a 和 b 的差集
print(a | b)     # a 和 b 的并集
print(a & b)     # a 和 b 的交集
print(a ^ b)     # a 和 b 中不同时存在的元素
# 元组不能 + 拼接
print('===' * 30)


li = [1, 5, 2, 3, 3, 4, 2]
s1 = set(li)
print(s1)   # {1, 2, 3, 4, 5}
li1 = list(s1)
print(li1)  # [1, 2, 3, 4, 5]
"""
问题：集合是无序的，但是为什么每次打印s1出来都是{1, 2, 3, 4, 5}？
回答：
集合确实是无序的
集合(set)在概念上是无序的，这意味着你不能通过索引来访问元素
集合中的元素没有固定的排列顺序
为什么看起来是有序的
在较新版本的Python（3.7+）中，set的内部实现使用了一种哈希表结构
当元素较少且哈希值分布均匀时，元素在内存中的存储顺序可能看起来是"有序"的
特别是对于连续的小整数，它们的哈希值就是它们本身，所以存储顺序可能恰好与数值顺序一致
不能依赖这种"有序"现象
这只是实现细节导致的巧合，不是集合的特性
在不同Python版本或不同环境下，或者添加更多元素后，顺序可能会改变
不应该依赖集合的显示顺序，因为这是不可预测的
如果需要有序的结果
如果你需要有序的唯一元素，应该使用:
     li = [1, 5, 2, 3, 3, 4, 2]
     s1 = set(li)
     sorted_list = sorted(s1)  # [1, 2, 3, 4, 5]
所以虽然你看到的是有序输出，但这只是巧合，集合本质上仍然是无序的数据结构。
"""
li = ['a', 'b', 1, '5', 2, 3, 3, '4', 2]
s1 = set(li)
print(s1)
li1 = list(s1)
print(li1)
