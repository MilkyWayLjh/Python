"""
try:
    可能发生异常的代码
except Exception as result:
    print(result)

只有语法错误 SyntaaxError ，不会抛出。在python中语法错误很特殊，执行机制是先整体检查一遍语法是否通过，不行就会直接抛出错误。
"""
# 捕获所有异常
# 第一种方式
try:
    num = int(input('数字：'))
    result = 1 / num
    print(result)
except Exception as e:
    print(e)
    # print('输入的数字不合法')

# 第二种方式
try:
    num = int(input('数字：'))
    result = 1 / num
    print(result)
# except Exception:
except:
    print('输入的数字不合法')
