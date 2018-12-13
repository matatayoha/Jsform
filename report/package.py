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


class Package(unittest.TestCase):
    '''测试添加组件'''


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
        self.driver.find_element_by_xpath('//*[@id="step3"]/h2/a').click()
        sleep(1)

    def test1(self):
        '''图表'''
        self.driver.find_element_by_id('graph').click()
        self.driver.find_element_by_xpath('//*[@id="z1"]/div').click()
        self.driver.find_element_by_xpath('//*[@id="spanGraphFieldList"]/div/div').click()
        self.driver.find_element_by_xpath('//*[@id="spanGraphFieldList"]/div/ul/li[2]').click()
        BasicAction.SaveReport(self.driver)
        self.assertEqual(self.driver.find_element_by_xpath('//*[@id="z1"]/div').get_attribute('class'), 'widget wgt_graph', '图表添加失败')

    def test2(self):
        '''统计'''
        self.driver.find_element_by_id('chart').click()
        self.driver.find_element_by_xpath('//*[@id="z1"]/div').click()
        self.driver.find_element_by_xpath('//*[@id="cS"]/ul/li/span[2]/div/div').click()
        self.driver.find_element_by_xpath('//*[@id="cS"]/ul/li/span[2]/div/ul/li[2]').click()
        BasicAction.SaveReport(self.driver)
        self.assertEqual(self.driver.find_element_by_xpath('//*[@id="z1"]/div').get_attribute('class'),
                         'widget wgt_chart noFloat', '统计添加失败')

    def test3(self):
        '''数字'''
        self.driver.find_element_by_id('number').click()
        self.driver.find_element_by_xpath('//*[@id="z1"]/div').click()
        self.driver.find_element_by_xpath('//*[@id="nS"]/ul[1]/li/span[3]/div/div').click()
        self.driver.find_element_by_xpath('//*[@id="nS"]/ul[1]/li/span[3]/div/ul/li[2]').click()
        BasicAction.SaveReport(self.driver)
        self.assertEqual(self.driver.find_element_by_xpath('//*[@id="z1"]/div').get_attribute('class'),
                         'widget wgt_number', '数字添加失败')
    def test4(self):
        '''文本'''
        self.driver.find_element_by_id('text').click()
        BasicAction.SaveReport(self.driver)
        self.assertEqual(self.driver.find_element_by_xpath('//*[@id="z1"]/div').get_attribute('class'),
                         'widget wgt_text', '文本添加失败')

    def test5(self):
        '''表格'''
        self.driver.find_element_by_id('grid').click()
        self.driver.find_element_by_xpath('//*[@id="z1"]/div').click()
        self.driver.find_element_by_xpath('//*[@id="dS"]/div[2]/span[2]/div/div').click()
        self.driver.find_element_by_xpath('//*[@id="dS"]/div[2]/span[2]/div/ul/li[2]').click()
        BasicAction.SaveReport(self.driver)
        self.assertEqual(self.driver.find_element_by_xpath('//*[@id="z1"]/div').get_attribute('class'),
                         'widget wgt_grid noFloat', '表格添加失败')

    def test6(self):
        '''布局方式'''
        self.driver.find_element_by_css_selector('[for="layout2"]').click()
        BasicAction.SaveReport(self.driver)
        self.assertEqual(self.driver.find_element_by_id('stage').get_attribute('class'),
                         'layout2', '布局方式修改失败')
    def tearDown(self):
        self.driver.get(url[0]+'app/report/manage')
        BasicAction.delete(self.driver)
        self.driver.close()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()

