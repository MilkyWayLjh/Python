import pymysql
import random
import time
from datetime import datetime


class CompanyNews:
    def __init__(self):
        self.conn = pymysql.connect(host='localhost', port=3306, user='root', password='root',
                                    database='advanced', charset='utf8')
        self.cursor = self.conn.cursor()

    def add(self, num):
        # conn, cursor = self.db_conn()
        try:
            for i in range(1, num+1):
                ran_count = random.randint(0, 9999)
                # dt_str = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                # sql = f"INSERT INTO company_news VALUES (default, '新闻标题{i}', '作者{i}', '新闻内容{i}', '{dt_str}', {ran_count})"
                sql = f"INSERT INTO company_news VALUES (default, '新闻标题{i}', '作者{i}', '新闻内容{i}', '{datetime.now()}', {ran_count})"
                print(sql)
                rows = self.cursor.execute(sql)
                print(f'Affected rows：{rows}')
                time.sleep(1)
        except Exception as e:
            self.conn.rollback()
            print(e)
        else:
            self.conn.commit()

    def delete(self, title):
        select_sql = f"SELECT * FROM company_news WHERE title = '{title}'"
        rows = self.cursor.execute(select_sql)
        # print(f'查询到{rows}行存在')
        # all_result = self.cursor.fetchall()
        # print(all_result)
        if rows:
            try:
                sql = f"DELETE FROM company_news WHERE title = '{title}'"
                rows = self.cursor.execute(sql)
                print(f'Affected rows：{rows}')
            except Exception as e:
                self.conn.rollback()
                print(e)
            else:
                self.conn.commit()
                print('删除成功!')
        else:
            print('标题不存在!')

    def __del__(self):
        self.cursor.close()
        self.conn.close()


if __name__ == '__main__':
    # CompanyNews().add(1)
    # CompanyNews().add(5)
    CompanyNews().delete('新闻标题1')

