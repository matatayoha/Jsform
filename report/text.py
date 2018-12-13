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


class Text(unittest.TestCase):
    '''测试文本'''


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
        self.driver.find_element_by_id('text').click()
        self.driver.find_element_by_xpath('//*[@id="z1"]/div').click()
        sleep(1)

    def test1(self):
        '''标题'''
        self.driver.find_element_by_id('textDescription').clear()
        self.driver.find_element_by_id('textDescription').send_keys('文本')
        BasicAction.SaveReport(self.driver)
        self.assertEqual(self.driver.find_element_by_xpath('//*[@id="z1"]/div/div').text, '文本', '文本修改失败')

    def tearDown(self):
        self.driver.get(url[0]+'app/report/manage')
        BasicAction.delete(self.driver)
        self.driver.close()


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()




