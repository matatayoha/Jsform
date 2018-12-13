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


class Chart(unittest.TestCase):
    '''测试统计'''


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
        self.driver.find_element_by_id('chart').click()
        self.driver.find_element_by_xpath('//*[@id="z1"]/div').click()
        self.driver.find_element_by_xpath('//*[@id="cS"]/ul/li/span[2]/div/div').click()
        self.driver.find_element_by_xpath('//*[@id="cS"]/ul/li/span[2]/div/ul/li[2]').click()
        sleep(1)

    def test1(self):
        '''标题'''
        self.driver.find_element_by_id('chartName').clear()
        self.driver.find_element_by_id('chartName').send_keys('统计')
        BasicAction.SaveReport(self.driver)
        self.assertEqual(self.driver.find_element_by_xpath('//*[@id="z1"]/div/table/caption/h4').text, '统计', '统计改名失败')

    def test2(self):
        '''列选项'''
        self.driver.find_element_by_xpath('//*[@id="fieldChartDetailDiv"]/div/div').click()
        self.driver.find_element_by_xpath('//*[@id="fieldChartDetailDiv"]/div/ul/li[2]').click()
        BasicAction.SaveReport(self.driver)
        self.assertEqual(self.driver.find_element_by_xpath('//*[@id="z1"]/div/table/thead/tr/th[3]').get_attribute('style'),'display: none;', '列选项更改失败')

    def test3(self):
        '''排列方式'''
        self.driver.find_element_by_xpath('//*[@id="cS"]/ul/li/span[4]/div/div').click()
        self.driver.find_element_by_xpath('//*[@id="cS"]/ul/li/span[4]/div/ul/li[2]').click()
        BasicAction.SaveReport(self.driver)
        self.assertGreater(
            self.driver.find_elements_by_css_selector('th div')[1].text,
            self.driver.find_elements_by_css_selector('th div')[0].text,
            '排列方式更改失败')

    def tearDown(self):
        self.driver.get(url[0]+'app/report/manage')
        BasicAction.delete(self.driver)
        self.driver.close()


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()



