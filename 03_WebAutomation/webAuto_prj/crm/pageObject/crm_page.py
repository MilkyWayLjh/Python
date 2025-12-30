from crm.base.base import *
from crm.common.common_login import Login
from pprint import pprint
import copy


class CrmPage(Login):
    def select_condition(self, values='0'):
        self.base_get_select(('name', 'addTime'), 1, values)

    def click(self):
        self.base_click((By.CSS_SELECTOR, '#div1>table>tbody>tr:nth-child(1)>td:nth-child(2)>div>input[type=submit]'))

    # 获取条数
    def get_count(self):
        td_lists = self.base_find_elements((By.CSS_SELECTOR, 'td[colspan="1"]'))
        # print(len(td_lists))
        return int(len(td_lists) / 3)

    # 获取内容
    def get_text(self):
        td_lists = self.base_find_elements((By.CSS_SELECTOR, 'td[colspan="1"]'))
        # pprint(td_lists)
        count = int(len(td_lists) / 3)
        li, li1, li2 = [], [], []
        # for i in td_lists:
        #     li.append(i.text)
        # pprint(li)
        if count >= 1:
            for n in range(1, count+1):
                for i in range(3*n-3, 3*n-1+1):
                    text = td_lists[i].text[:19]
                    li1.append(text)
                    li2 = copy.deepcopy(li1)
                tup = tuple(li2)
                li.append(tup)
                li1.clear()
            tup1 = tuple(li)
            # pprint(tup1)
            return tup1
        else:
            return None

        # 1 0,1,2   n+(2n-1)=1+1  3n-3 ~ 3n-1
        # 2 3,4,5   2+3
        # 3 6,7,8
        # 4 9,10,11
        # 5 12,13,14
        # n...


if __name__ == '__main__':
    crm = CrmPage()
    crm.login()
    crm.driver.switch_to.frame('mainFrame')
    crm.select_condition('1')
    crm.click()
    crm.get_count()
    pprint(crm.get_text())

    crm.quit(2)

