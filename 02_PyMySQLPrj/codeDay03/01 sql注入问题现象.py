# sql注入了解
# ● 什么是sql注入
# 用户提交带有恶意的数据与SQL语句进行字符串方式的拼接，从而影响了SQL语句的语义，最终产生数据泄露的现象。
# ● sql注入解决
#   ○ SQL语句中的参数使用%s来占位，此处不是python中的字符串格式化操作
#   ○ 将SQL语句中%s占位所需要的参数存在一个列表中，把参数列表传递给execute方法中第二个参数

import pymysql

conn = pymysql.connect(
    user='root', password='root', database='advanced', charset='utf8'
)

cursor = conn.cursor(pymysql.cursors.DictCursor)

title = input('输入标题进行查询：')
# 传入 ' or 1 = 1 or '  或者  " or 1 = 1 or "  会爆表，查询全部记录
sql = f"select * from company_news where title = '{title}'"
print(sql)
rows = cursor.execute(sql)

print(cursor.fetchall())

cursor.close()
conn.close()
