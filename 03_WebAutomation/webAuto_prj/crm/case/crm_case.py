import unittest
from crm.pageObject.crm_page import *
from crm.common.db import DB


class CrmTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.crm = CrmPage()
        cls.crm.login()
        cls.crm.driver.switch_to.frame('mainFrame')

    # 当天
    def test_crm_01(self):
        self.crm.select_condition()
        self.crm.click()
        self.crm.get_count()
        self.crm.get_text()
        # 数据库查询
        # CAST(a.care_nexttime AS CHAR) AS DATE 将数据库中的对象时间转化为字符串时间
        row, data = DB('crm', host='172.16.20.203', password='123456').read(
            "SELECT a.care_theme, CAST(a.care_nexttime AS CHAR) AS DATE, b.customer_name FROM customer_care a, customer_info b WHERE a.customer_id = b.customer_id AND a.is_used = '1' AND TO_DAYS( a.care_nexttime ) - TO_DAYS(now())=0"
        )
        self.assertEqual(self.crm.get_count(), row)
        self.assertEqual(self.crm.get_text(), data)

    # 一周内
    def test_crm_02(self):
        self.crm.select_condition('1')
        self.crm.click()
        count = self.crm.get_count()
        info = self.crm.get_text()
        pprint(count)
        pprint(info)
        # 数据库查询
        row, data = DB('crm', host='172.16.20.203', password='123456').read(
            "SELECT a.care_theme, a.care_nexttime, b.customer_name FROM customer_care a, customer_info b WHERE a.customer_id = b.customer_id AND a.is_used = '1' AND TO_DAYS( a.care_nexttime ) - TO_DAYS(now())>0 AND TO_DAYS( a.care_nexttime ) - TO_DAYS(now())<='7'"
        )
        print(row)
        # pprint(data)
        # pprint(str(data[0][1]))
        # 将数据库的数据重新转化一次(主要是对象时间转字符串时间)
        data1 = []
        for i in data:
            data1.append((i[0], str(i[1]), i[2]))
        data2 = tuple(data1)
        pprint(data2)
        self.assertEqual(count, row)
        self.assertEqual(info, data2)

    # 半月内
    def test_crm_03(self):
        self.crm.select_condition('2')
        self.crm.click()
        count = self.crm.get_count()
        info = self.crm.get_text()
        print(count)
        pprint(info)
        # 数据库查询
        # TODO CAST(a.care_nexttime AS CHAR) AS DATE 将数据库中的对象时间转化为字符串时间
        row, data = DB('crm', host='172.16.20.203', password='123456').read(
            "SELECT a.care_theme, CAST(a.care_nexttime AS CHAR) AS DATE, b.customer_name FROM customer_care a, customer_info b WHERE a.customer_id = b.customer_id AND a.is_used = '1' AND TO_DAYS( a.care_nexttime ) - TO_DAYS(now())>0 AND TO_DAYS( a.care_nexttime ) - TO_DAYS(now())<='7'"
        )
        print(row)
        pprint(data)
        self.assertEqual(count, row)
        self.assertEqual(info, data)

    # 一个月内
    def test_crm_04(self):
        self.crm.select_condition('3')
        self.crm.click()
        self.crm.get_count()
        self.crm.get_text()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.crm.quit(2)


if __name__ == '__main__':
    unittest.main()


