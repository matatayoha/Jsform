# -*- coding: utf-8 -*-
# @Time    : 2018/8/22 0022 16:55
# @Author  : biubiubiu
# @FileName: text.py
# @Software: PyCharm


from code.login import Login
from time import sleep
import unittest,random
from runner import url
from code.basicaction import BasicAction


class Set(unittest.TestCase):
    '''测试设置报表'''

    @classmethod
    def setUpClass(cls):
        cls.Login = Login()
        cls.Login.login()
        cls.driver = cls.Login.driver
        cls.driver.get(url[0] + 'app/formmain/add?groupid=')
        sleep(1)
        cls.driver.find_element_by_id('drag_text').click()
        cls.driver.find_element_by_id('nb').click()
        BasicAction.preview(cls.driver)
        for i in range(3):
            cls.driver.find_element_by_name("F2_number").send_keys(random.randint(1, 10))
            cls.driver.find_element_by_id("tmpid").send_keys(random.randint(1, 10))
            cls.driver.find_element_by_id('btnSubmit').click()
            cls.driver.refresh()
        cls.driver.close()



    def setUp(self):
        self.driver.switch_to.window(self.driver.window_handles[0])
        self.driver.get(url[0] + 'app/report/add?groupid=')
        sleep(1)

    def test1(self):
        '''修改名称'''
        self.driver.find_element_by_id('reportName').clear()
        self.driver.find_element_by_id('reportName').send_keys('报表名称')
        BasicAction.SaveReport(self.driver)
        self.assertEqual(self.driver.find_element_by_id('rptTitle').text, '报表名称', '报表改名失败')

    def test2(self):
        '''修改描述'''
        self.driver.find_element_by_id('reportDescription').clear()
        self.driver.find_element_by_id('reportDescription').send_keys('报表描述')
        BasicAction.SaveReport(self.driver)
        self.assertEqual(self.driver.find_element_by_id('rptDesc').text, '报表描述', '报表描述修改失败')

    def test3(self):
        '''允许用户导出'''
        self.driver.find_element_by_css_selector('[for="showExport"]').click()
        BasicAction.SaveReport(self.driver)
        self.assertEqual(self.driver.find_element_by_id('exportButton').text, '导出', '允许用户导出失败')

    def tearDown(self):
        self.driver.get(url[0]+'app/report/manage')
        BasicAction.delete(self.driver)
        self.driver.close()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
