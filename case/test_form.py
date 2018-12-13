# -*- coding: utf-8 -*-
# @Time    : 2018/8/22 0022 16:55
# @Author  : biubiubiu
# @FileName: text.py
# @Software: PyCharm

from code.login import Login
from time import  sleep
import unittest
from runner import url
from code.basicaction import BasicAction


class Form(unittest.TestCase):
    '''测试表单属性'''


    @classmethod
    def setUpClass(cls):
        cls.Login = Login()
        cls.Login.login()
        cls.driver = cls.Login.driver

    def setUp(self):
        self.driver.switch_to.window(self.driver.window_handles[0])
        self.driver.get(url[0]+'app/formmain/add?groupid=')
        sleep(1)
        self.driver.find_element_by_id('sl').click()
        self.driver.find_element_by_id('fTitle').click()

    def test1(self):
        '''表单名称'''
        self.driver.find_element_by_id("formName").clear()
        self.driver.find_element_by_id("formName").send_keys("测试表单名称")
        BasicAction.preview(self.driver)
        self.assertEqual(self.driver.find_element_by_xpath('//*[@id="formHeader"]/h2').text,'测试表单名称','修改表单名称失败')

    def test2(self):
        '''表单描述'''
        js = "$('#desc').val('测试表单描述').keyup()"
        self.driver.execute_script(js)
        BasicAction.preview(self.driver)
        self.assertEqual(self.driver.find_element_by_xpath('//*[@id="formHeader"]/div').text, "测试表单描述", '表单描述设置失败')

    def test3(self):
        '''网页跳转'''
        self.driver.find_element_by_css_selector('[for="confirmType_url"]').click()
        self.driver.find_element_by_id('confirmMsg_url').send_keys('https://www.baidu.com/')
        BasicAction.preview(self.driver)
        self.driver.find_element_by_id('btnSubmit').click()
        self.assertEqual(self.driver.current_url, 'https://www.baidu.com/', '网页跳转设置失败')

    def tearDown(self):
        self.driver.get(url[2])
        BasicAction.delete(self.driver)
        self.driver.close()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()