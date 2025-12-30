import pymysql

conn = pymysql.connect(host='127.0.0.1', port=3306,
                       user='root', password='root',
                       database='advanced', charset='utf8')

cursor = conn.cursor()

# sql = "INSERT INTO student VALUES (8, 'itsrc_015', '菜只因', '男', 26, 2)"
# sql = "INSERT INTO student VALUES (9, 'itsrc_016', '菜鲲', '男', 27, 1)"

# sql = "UPDATE student SET stu_name = '蔡只因' WHERE stu_id = 8"

sql = "DELETE FROM student WHERE stu_id = 9"

# python操作mysql默认开启了事务，所以执行过的sql语句。只是在内存中生效，如果要持久化元，需要提交操作或者有问题需要回滚。
# 注意：提交和回滚使用的是 数据库连接对象 conn
try:
    rows = cursor.execute(sql)
    print(f'Affected rows：{rows}')
except Exception as e:
    # 回滚
    conn.rollback()
    print(e)
else:
    # 提交
    conn.commit()

cursor.close()
conn.close()
