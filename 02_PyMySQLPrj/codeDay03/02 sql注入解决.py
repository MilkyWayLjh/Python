import pymysql

conn = pymysql.connect(
    user='root', password='root', database='advanced', charset='utf8'
)

cursor = conn.cursor(pymysql.cursors.DictCursor)

title = input('输入标题进行查询：')
author = input('输入标题进行查询：')

# ○ SQL语句中的参数使用%s来占位，此处不是python中的字符串格式化操作
# ○ 将SQL语句中%s占位所需要的参数存在一个列表中，把参数列表传递给execute方法中第二个参数
sql = f"select * from company_news where title = %s or author = %s"
print(sql)
rows = cursor.execute(sql, [title, author])

print(cursor.fetchall())

cursor.close()
conn.close()
