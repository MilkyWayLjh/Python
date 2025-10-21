# 新建一个文件，定义一个花类，创建一个花对象，调用上面的属性和方法
class Flower:
    def __init__(self, color, variety):
        self.color = color
        self.variety = variety

    def __str__(self):
        return 'this is 🌼'

    def status(self, status):
        print(f'{self.variety}{status}')

flower = Flower('red', '🌹')
print(flower)
print(flower.color, flower.variety)
flower.status('盛开着')

