import sqlite3


class SQLiteDB:
    def __init__(self, database):
        # 创建数据库连接
        self.conn = sqlite3.connect(database=database)
        # 创建游标对象
        self.cursor = self.conn.cursor()

    def read(self, sql, args=None):
        try:
            rows = self.cursor.execute(sql, args)
        except Exception as e:
            print(e)
            return 0
        else:
            all_data = self.cursor.fetchall()
            return rows, all_data if all_data else ()

    def write(self, sql, args=None):
        try:
            rows = self.cursor.execute(sql, args)
        except Exception as e:
            print(e)
            self.conn.rollback()
            return 0
        else:
            self.conn.commit()
            return rows

    def __del__(self):
        self.cursor.close()
        self.conn.close()


if __name__ == '__main__':
    pass
    # row = SQLiteDB('test.db').write("""
    #      create table company(
    #         id int primary key not null,
    #         name text not null,
    #         age int not null,
    #         address char(50),
    #         salary real);""")
    # print(row)
    # rows, data = SQLiteDB('./plate.db').read('')
    # print(rows, data)
