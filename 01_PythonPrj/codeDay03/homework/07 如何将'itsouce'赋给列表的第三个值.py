"""
如何将'itsource'赋给列表的第三个值，而列表保存在名为bags的变量中？
bags = [2, 4, 6, 8, 10]
"""
bags = [2, 4, 6, 8, 10]
bags.insert(2, 'itsource')
print(bags)     # 结果为 [2, 4, 'itsource', 6, 8, 10]
