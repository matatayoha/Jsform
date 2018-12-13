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


class Grid(unittest.TestCase):
    '''测试表格'''


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
        self.driver.find_element_by_id('grid').click()
        self.driver.find_element_by_xpath('//*[@id="z1"]/div').click()
        self.driver.find_element_by_xpath('//*[@id="dS"]/div[2]/span[2]/div/div').click()
        self.driver.find_element_by_xpath('//*[@id="dS"]/div[2]/span[2]/div/ul/li[2]').click()
        sleep(1)

    def test1(self):
        '''分页大小'''
        self.driver.find_element_by_xpath('//*[@id="dS"]/div[1]/div/div').click()
        self.driver.find_element_by_xpath('//*[@id="dS"]/div[1]/div/ul/li[3]').click()
        BasicAction.SaveReport(self.driver)
        self.assertTrue(self.driver.find_element_by_xpath(
            '//*[@id="z1"]/div/table[2]/tbody/tr/td[3]/select/option[2]').get_attribute('selected'), '分页大小更改失败')

    def test2(self):
        '''排序方式'''
        self.driver.find_element_by_xpath('//*[@id="dS"]/div[2]/span[3]/div/div').click()
        self.driver.find_element_by_xpath('//*[@id="dS"]/div[2]/span[3]/div/ul/li[2]').click()
        BasicAction.SaveReport(self.driver)
        self.assertGreater(
            self.driver.find_element_by_xpath('//*[@id="g0_0"]/tbody/tr[1]/td[1]').text,
            self.driver.find_element_by_xpath('//*[@id="g0_0"]/tbody/tr[2]/td[1]').text,
            '排序方式更改失败')

    def test3(self):
        '''显示字段'''
        self.driver.find_element_by_css_selector('[for="showAllFields"]').click()
        BasicAction.SaveReport(self.driver)
        self.assertEqual(self.driver.find_element_by_xpath('//*[@id="g0_0"]/thead/tr/td[1]/div').text,'ID','显示字段更改失败')

    def tearDown(self):
        self.driver.get(url[0]+'app/report/manage')
        BasicAction.delete(self.driver)
        self.driver.close()


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()




