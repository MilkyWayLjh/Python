# 1.导入pymysql
import pymysql

# 2.创建连接对象
conn = pymysql.connect(host='127.0.0.1', port=3306,
                       user='root', password='root',
                       database='advanced', charset='utf8')

# 3.获取游标对象
#   作用：执行sql语句，获取查询结果集
#   pymysql.cursors.Cursor 元组结果集, 默认cursor
#   元组游标，默认值。   多条数据: 元组套元组
#   cursor = conn.cursor(cursor=pymysql.cursors.Cursor)
#   cursor = conn.cursor()
#
#   pymysql.cursors.DictCursor 字典结果集  [{key:value,key:value...},{},...]
#   字典游标，字段名：字段值。   多条数据: 列表套字典
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)


# 4.执行sql语句
rows = cursor.execute('select * from student')
print(rows)

# 5.获取查询结果集
#   注意：游标对象中的结果集数据，只能获取一次。获取过后，就不能再获取，游标后移。
#   获取一条记录
one = cursor.fetchone()
print(one)
#   获取指定行数, 参数是指定获取的记录条数
many = cursor.fetchmany(2)
print(many)
#   获取所有结果集
_all = cursor.fetchall()
print(_all)

# 6.关闭游标对象
cursor.close()

# 7.关闭连接对象
conn.close()
