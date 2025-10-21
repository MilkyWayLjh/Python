"""
定义一个模块
模块里面具有 三个类：
    厨师: 炒菜方法
    服务员: 接待客人方法  送走客人方法
    收银员: 收钱方法
客人来-->服务员接待-->客人点菜-->厨师炒菜-->客人吃完了-->收银员收钱-->服务员送客
"""


class Cook:
    @staticmethod
    def cook():
        return '厨师开始炒菜'


class Waiter:
    @staticmethod
    def reception():
        return '服务员接待'

    @staticmethod
    def send():
        return '服务员送客'


class Cashier:
    @staticmethod
    def collect_money():
        return '收银员收钱'


print(f'客人来-->{Waiter.reception()}-->客人点菜-->{Cook.cook()}-->客人吃完了-->{Cashier.collect_money()}-->{Waiter.send()}')
