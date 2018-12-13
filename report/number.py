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


class Number(unittest.TestCase):
    '''测试数字'''


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
        self.driver.find_element_by_id('number').click()
        self.driver.find_element_by_xpath('//*[@id="z1"]/div').click()
        self.driver.find_element_by_xpath('//*[@id="nS"]/ul[1]/li/span[3]/div/div').click()
        self.driver.find_element_by_xpath('//*[@id="nS"]/ul[1]/li/span[3]/div/ul/li[2]').click()
        sleep(1)

    def test1(self):
        '''标题'''
        self.driver.find_element_by_id('numberName').clear()
        self.driver.find_element_by_id('numberName').send_keys('数字')
        BasicAction.SaveReport(self.driver)
        self.assertEqual(self.driver.find_element_by_xpath('//*[@id="w0_0"]/strong').text, '数字', '数字改名失败')

    def test2(self):
        '''描述'''
        self.driver.find_element_by_id('numberDescription').clear()
        self.driver.find_element_by_id('numberDescription').send_keys('描述')
        BasicAction.SaveReport(self.driver)
        self.assertEqual(self.driver.find_element_by_xpath('//*[@id="w0_0"]/em').text, '描述', '描述修改失败')

    def test3(self):
        '''统计类型'''
        self.driver.find_element_by_xpath('//*[@id="nS"]/ul[2]/li/span[1]/div/div').click()
        self.driver.find_element_by_xpath('//*[@id="nS"]/ul[2]/li/span[1]/div/ul/li[2]').click()
        BasicAction.SaveReport(self.driver)
        self.assertTrue(self.driver.find_element_by_xpath('//*[@id="w0_0"]/var').text,'统计类型更改失败')

    def test4(self):
        '''数字格式'''
        self.driver.find_element_by_xpath('//*[@id="nS"]/ul[2]/li/span[2]/div/div').click()
        self.driver.find_element_by_xpath('//*[@id="nS"]/ul[2]/li/span[2]/div/ul/li[4]').click()
        BasicAction.SaveReport(self.driver)
        self.assertIn('0',
            self.driver.find_element_by_xpath('//*[@id="w0_0"]/var').text,
            '数字格式更改失败')

    def test5(self):
        '''颜色'''
        self.driver.find_element_by_xpath('//*[@id="numberColorDiv"]/a[2]').click()
        BasicAction.SaveReport(self.driver)
        self.assertIn('2',
            self.driver.find_element_by_xpath('//*[@id="w0_0"]/var').get_attribute('class'),
            '颜色更改失败')

    def tearDown(self):
        self.driver.get(url[0]+'app/report/manage')
        BasicAction.delete(self.driver)
        self.driver.close()


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()




