# 定义一个函数,实现对字典的浅拷贝和深拷贝
import copy

dict1 = {
    'name': '马sir',
    'age': '70',
    'skill': {
        'Q': '闪电五连鞭',
        'W': '耗子尾汁',
        'E': '不讲武德偷袭',
        'R': '太极形意拳'
    }
}


# 方法一
def _copy(dic, mode):
    if mode == 'shallow':
        return copy.copy(dic)
    elif mode == 'deep':
        return copy.deepcopy(dic)
    else:
        return False


# 方法二
def my_copy(dic):
    return copy.copy(dic), copy.deepcopy(dic)   # 返回多个值为 元组


if __name__ == '__main__':
    # dict2 = _copy(dict1, 'shallow')
    # dict3 = _copy(dict1, 'deep')
    dict2 = my_copy(dict1)[0]  # 浅拷贝方法
    dict3 = my_copy(dict1)[1]  # 深拷贝方法

    print(dict1, id(dict1), id(dict1['skill']))     # id(dict1['skill']) -> 28670448
    print(dict2, id(dict2), id(dict2['skill']))     # id(dict2['skill']) -> 28670448
    print('===' * 40)
    print(dict1, id(dict1), id(dict1['skill']))     # id(dict1['skill']) -> 28670448
    print(dict3, id(dict3), id(dict3['skill']))     # id(dict3['skill']) -> 34133552
    print('===' * 40)
    dict1['skill']['Q'] = '技能被修改了'
    print(dict1, dict2, dict3, sep='\n')    # dict1 / dict2改变. dict3不改变
