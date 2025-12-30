from selenium import webdriver
from time import sleep
import csv

path = './data/login_data.csv'
data = csv.reader(open(path, 'r'))

# csv读取文件返回一个迭代器对象，数据用过一次，就不能继续读了
print(list(data))
print(tuple(data))  # 没有数据，已经读完了
