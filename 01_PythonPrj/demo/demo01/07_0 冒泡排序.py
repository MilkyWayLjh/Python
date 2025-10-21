# 从小到大，冒泡排序
def sort_fun(li):
    for i in range(len(li)-1):  # 这个循环负责设置冒泡排序进行的次数
        for j in range(len(li)-1-i):      # 确定相邻两个元素之间的位置, j为列表下标
            if li[j] > li[j + 1]:  # 通过判断比较相邻两个元素的大小
                # temp = li[j]   # 将比较的最大的值赋值给中间量
                # li[j] = li[j + 1]   # 将比较的最小的值赋值给li[j];
                # li[j + 1] = temp    # 最大的那个中间值再赋值给li[j+1]
                li[j], li[j+1] = li[j+1], li[j]
    print(li)


# 从大到小，冒泡排序
def sort_fun1(li):
    for i in range(len(li)-1):
        for j in range(len(li)-1-i):      # 确定相邻两个元素之间的位置
            if li[j] < li[j + 1]:  # 通过判断比较相邻两个元素的大小
                li[j], li[j+1] = li[j+1], li[j]
    print(li)


li1 = [23, 45, 22, 67, 12, 45, 35, 78, 93, 17, 54, 36, 56, 64, 4, 1, 7, 60]
sort_fun(li1)
sort_fun1(li1)
