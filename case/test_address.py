# -*- coding: utf-8 -*-
# @Time    : 2018/8/22 0022 16:55
# @Author  : biubiubiu
# @FileName: text.py
# @Software: PyCharm


from code.login import Login
from code.property import SettingOptUtils
from code.getdata import DataUtils
from time import  sleep
import unittest
from runner import url
from code.basicaction import BasicAction


class Address(unittest.TestCase):
    '''测试地址'''

    @classmethod
    def setUpClass(cls):
        cls.Login = Login()
        cls.Login.login()
        cls.driver = cls.Login.driver

    def setUp(self):
        self.driver.switch_to.window(self.driver.window_handles[0])
        self.driver.get(url[0]+'app/formmain/add?groupid=')
        sleep(1)
        self.driver.find_element_by_id('ad').click()
        

    def test1(self):
        '''修改名称'''
        SettingOptUtils.element_name(self.driver)
        BasicAction.preview(self.driver)
        self.assertEqual(self.driver.find_element_by_xpath('//*[@id="fields"]/li/label').text,'组件改名','组件改名失败')

    def test2(self):
        '''隐藏详细地址'''
        SettingOptUtils.detail(self.driver)
        BasicAction.preview(self.driver)
        self.assertIn('hide', self.driver.find_element_by_xpath('//*[@id="fields"]/li/div/span[4]').get_attribute('class'),'隐藏详细地址设置失败')

    def test3(self):
        '''必须输入'''
        SettingOptUtils.popt_required(self.driver)
        BasicAction.preview(self.driver)
        self.assertEqual(self.driver.find_element_by_xpath('//*[@id="fields"]/li').get_attribute('reqd'), '1', '必须输入设置失败')

    def test4(self):
        '''登录用户可见'''
        SettingOptUtils.sec_pri(self.driver)
        BasicAction.preview(self.driver)
        self.assertIsNone(self.driver.find_element_by_xpath('//*[@id="fields"]/li').get_attribute('typ'),'登录用户可见设置失败')

    def test5(self):
        '''默认值'''
        SettingOptUtils.pdefval_addr(self.driver)
        BasicAction.preview(self.driver)
        self.assertEqual(self.driver.find_element_by_xpath('//*[@id="fields"]/li').get_attribute('def'),'北京市-北京市-朝阳区','默认值设置失败')

    def test6(self):
        '''字段说明'''
        SettingOptUtils.instruct(self.driver)
        BasicAction.preview(self.driver)
        self.assertEqual(self.driver.find_element_by_xpath('//*[@id="p0"]').text,'字段说明','字段说明设置失败')

    def test7(self):
        '''字段宽度'''
        SettingOptUtils.element_format(self.driver, 'selLayout')
        BasicAction.preview(self.driver)
        self.assertIn('leftHalf', self.driver.find_element_by_xpath('//*[@id="fields"]/li').get_attribute('class'),'字段宽度设置失败')

    def test8(self):
        '''CSS名称'''
        SettingOptUtils.css(self.driver)
        BasicAction.preview(self.driver)
        self.assertIn('[class=desc]', self.driver.find_element_by_xpath('//*[@id="fields"]/li').get_attribute('class'),'CSS名称设置失败')

    def test9(self):
        '''提交数据'''
        self.formid = BasicAction.preview(self.driver)
        self.driver.find_element_by_css_selector('[class="xxl province input fld"]').click()
        self.driver.find_element_by_xpath('//*[@id="fields"]/li/div/span[1]/select/option[2]').click()
        self.driver.find_element_by_id('btnSubmit').click()
        sleep(1)
        self.assertEqual('北京市',DataUtils.verify_data(url, self.formid)['F2'],'提交数据失败')

    def tearDown(self):
        self.driver.get(url[2])
        BasicAction.delete(self.driver)
        self.driver.close()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()



if __name__ == '__main__':
    unittest.main()
