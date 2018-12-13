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


class Graph(unittest.TestCase):
    '''测试图表'''


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
        self.driver.find_element_by_id('graph').click()
        self.driver.find_element_by_xpath('//*[@id="z1"]/div').click()
        self.driver.find_element_by_xpath('//*[@id="spanGraphFieldList"]/div/div').click()
        self.driver.find_element_by_xpath('//*[@id="spanGraphFieldList"]/div/ul/li[2]').click()
        sleep(1)

    def test1(self):
        '''标题'''
        self.driver.find_element_by_id('graphName').clear()
        self.driver.find_element_by_id('graphName').send_keys('图表')
        BasicAction.SaveReport(self.driver)
        self.assertEqual(self.driver.find_element_by_xpath('//*[@id="z1"]/div/div[1]/h4').text, '图表', '图表改名失败')
        self.driver.close()

    def test2(self):
        '''图表类型-饼状图'''
        self.assertIn('smallpie',self.driver.find_element_by_xpath('//*[@id="z1"]/div/div[2]/img').get_attribute('src'), '饼状图更改失败')

    def test3(self):
        '''图表类型-柱状图'''
        self.driver.find_element_by_xpath('//*[@id="graphSettingsDiv"]/span[2]/div/div').click()
        self.driver.find_element_by_xpath('//*[@id="graphSettingsDiv"]/span[2]/div/ul/li[2]').click()
        self.assertIn('smallcol',self.driver.find_element_by_xpath('//*[@id="z1"]/div/div[2]/img').get_attribute('src'), '柱状图更改失败')

    def test4(self):
        '''图表类型-线性'''
        self.driver.find_element_by_xpath('//*[@id="graphSettingsDiv"]/span[2]/div/div').click()
        self.driver.find_element_by_xpath('//*[@id="graphSettingsDiv"]/span[2]/div/ul/li[3]').click()
        self.assertIn('smallline',self.driver.find_element_by_xpath('//*[@id="z1"]/div/div[2]/img').get_attribute('src'), '线性图更改失败')

    def test5(self):
        '''大小'''
        self.driver.find_element_by_xpath('//*[@id="graphSettingsDiv"]/span[5]/div/div').click()
        self.driver.find_element_by_xpath('//*[@id="graphSettingsDiv"]/span[5]/div/ul/li[3]').click()
        self.assertIn('largepie',self.driver.find_element_by_xpath('//*[@id="z1"]/div/div[2]/img').get_attribute('src'), '线性图更改失败')

    def tearDown(self):
        self.driver.switch_to.window(self.driver.window_handles[0])
        self.driver.get(url[0]+'app/report/manage')
        BasicAction.delete(self.driver)


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()


