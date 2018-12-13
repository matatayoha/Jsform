# -*- coding: utf-8 -*-
# @Time    : 2018/8/22 0022 16:55
# @Author  : biubiubiu
# @FileName: text.py
# @Software: PyCharm


from code.login import Login
from code.property import SettingOptUtils
from time import  sleep
import unittest
from runner import url
from code.basicaction import BasicAction


class Section(unittest.TestCase):
    '''测试分隔符'''


    @classmethod
    def setUpClass(cls):
        cls.Login = Login()
        cls.Login.login()
        cls.driver = cls.Login.driver

    def setUp(self):
        self.driver.switch_to.window(self.driver.window_handles[0])
        self.driver.get(url[0]+'app/formmain/add?groupid=')
        sleep(1)
        self.driver.find_element_by_id('sb').click()


    def test1(self):
        '''修改名称'''
        SettingOptUtils.element_name(self.driver)
        BasicAction.preview(self.driver)
        self.assertEqual(self.driver.find_element_by_xpath('//*[@id="fields"]/li/div/label').text,'组件改名','组件改名失败')

    def test2(self):
        '''分隔描述'''
        SettingOptUtils.wangEditor_txt(self.driver,'secdesc')
        BasicAction.preview(self.driver)
        self.assertEqual('测试', self.driver.find_element_by_css_selector('label + div').text,'分隔描述设置失败')

    def test3(self):
        '''登录用户可见'''
        SettingOptUtils.sec_pri(self.driver)
        BasicAction.preview(self.driver)
        self.assertIsNone(self.driver.find_element_by_xpath('//*[@id="fields"]/li').get_attribute('typ'),'登录用户可见设置失败')

    def test4(self):
        '''字段宽度'''
        SettingOptUtils.element_format(self.driver, 'selLayout')
        BasicAction.preview(self.driver)
        self.assertIn('leftHalf', self.driver.find_element_by_xpath('//*[@id="fields"]/li').get_attribute('class'),'字段宽度设置失败')

    def test5(self):
        '''CSS名称'''
        SettingOptUtils.css(self.driver)
        BasicAction.preview(self.driver)
        self.assertIn('[class=desc]', self.driver.find_element_by_xpath('//*[@id="fields"]/li').get_attribute('class'),'CSS名称设置失败')

    def tearDown(self):
        self.driver.get(url[2])
        BasicAction.delete(self.driver)
        self.driver.close()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()

