import pymysql
from pprint import pprint


class DB:
    def __init__(self, database, host='localhost', port=3306, user='root', password='root',
                 cursor=pymysql.cursors.Cursor):
        self.conn = pymysql.connect(
            host=host, port=port,
            user=user, password=password,
            database=database, charset='utf8'
        )
        self.cursor = self.conn.cursor(cursor=cursor)
        self.cursor_type = () if cursor == pymysql.cursors.Cursor else []

    def read(self, sql, args=None):
        try:
            rows = self.cursor.execute(sql, args)
        except Exception as e:
            print(e)
            return 0, self.cursor_type
        else:
            all_data = self.cursor.fetchall()
            # return rows, all_data
            return rows, all_data if all_data else self.cursor_type

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
    # row, data = DB('advanced').read('select * from company_news where title = "新闻标题1"')
    # row, data = DB('advanced', cursor=pymysql.cursors.DictCursor).read(
    #     'select * from company_news where title = %s', ['新闻标题1'])
    # print(row)
    # print(data)
    # print(DB('advanced').write('delete from company_news where title = %s', ['新闻标题5']))

    row, data = DB('crm', host='172.16.20.203', password='123456').read(
        """
        SELECT
	a.*,
	b.customer_name 
FROM
	customer_care a,
	customer_info b 
WHERE
	a.customer_id = b.customer_id 
	AND a.is_used = '1' 
	AND TO_DAYS( a.care_nexttime ) - TO_DAYS(
	now())>0
	AND TO_DAYS( a.care_nexttime ) - TO_DAYS(
	now())<='7'
        """
    )
    print(row)
    pprint(data)


