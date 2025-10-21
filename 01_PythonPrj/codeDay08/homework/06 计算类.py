# 新建一个文件，定义一个计算类，有两个属性，数字1，数字2，具有 加 减 乘 除 方法
class Calc:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    # 法一
    def operation(self, sign):
        if sign == '+':
            return self.num1 + self.num2
        elif sign == '-':
            return self.num1 - self.num2
        elif sign == '*':
            return self.num1 * self.num2
        elif sign == '/':
            return self.num1 / self.num2
        else:
            return '只允许输入[ + - * / ]4种运算符号!'

    # 法二
    # def add(self):
    #     # 加
    #     return self.num1 + self.num2
    #
    # def subtract(self):
    #     # 减
    #     return self.num1 - self.num2
    #
    # def multiplication(self):
    #     # 乘
    #     return self.num1 * self.num2
    #
    # def division(self):
    #     # 除
    #     return self.num1 / self.num2

    # 法三
    # def operation(self, sign):
    #     flag = {
    #         '+': self.add,
    #         '-': self.subtract,
    #         '*': self.multiplication,
    #         '/': self.division
    #     }
    #     if sign in flag.keys():
    #         flag[sign]()
    #     else:
    #         return '只允许输入[ + - * / ]4种运算符号!'

calc = Calc(20, 10)
# 法一
print(calc.operation('+'))
print(calc.operation('-'))
print(calc.operation('*'))
print(calc.operation('/'))
print(calc.operation('%'))

# 法二
# print(calc.add())
# print(calc.subtract())
# print(calc.multiplication())
# print(calc.division())

# 法三
# print(calc.operation('/'))
