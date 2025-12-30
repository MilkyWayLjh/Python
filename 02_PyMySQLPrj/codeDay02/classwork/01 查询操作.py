# 1.导入pymysql
import pymysql

# 2.创建连接对象
#   host: 数据库的主机地址(ip地址), 默认值是 localhost == 127.0.0.1
#   port: 端口号,默认值是3306
#   user: 数据库的账号
#   password: 数据库的密码
#   database: 要操作的数据库
#   charset: 通信编码格式,一般都用utf8
conn = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='advanced', charset='utf8')

# 3.获取游标对象
#   作用：执行sql语句，获取查询结果集
#   pymysql.cursors.Cursor 元组结果集, 默认cursor
#   pymysql.cursors.DictCursor 字典结果集  [{key:value,key:value...},{},...]
cursor = conn.cursor()

# 4.执行sql语句
#   sql语句不需要分号
#   返回受影响行数
#   cursor.execute(sql语句, [val1, val2, ...])
sql = 'select * from student'
rows = cursor.execute(sql)
print(f'受影响行数是：{rows}')

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
