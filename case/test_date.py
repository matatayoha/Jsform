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


class Date(unittest.TestCase):
    '''测试日期'''


    @classmethod
    def setUpClass(cls):
        cls.Login = Login()
        cls.Login.login()
        cls.driver = cls.Login.driver

    def setUp(self):
        self.driver.switch_to.window(self.driver.window_handles[0])
        self.driver.get(url[0]+'app/formmain/add?groupid=')
        sleep(1)
        self.driver.find_element_by_id('dt').click()


    def test1(self):
        '''修改名称'''
        SettingOptUtils.element_name(self.driver)
        BasicAction.preview(self.driver)
        self.assertEqual(self.driver.find_element_by_xpath('//*[@id="fields"]/li/label').text,'组件改名','组件改名失败')

    def test2(self):
        '''日期格式'''
        SettingOptUtils.element_format(self.driver, 'dateformat')
        BasicAction.preview(self.driver)
        self.assertIn('MM', self.driver.find_element_by_xpath('//*[@id="fields"]/li/div/span[1]/label').text,'日期格式设置失败')

    def test3(self):
        '''必须输入'''
        SettingOptUtils.popt_required(self.driver)
        BasicAction.preview(self.driver)
        self.assertEqual(self.driver.find_element_by_xpath('//*[@id="fields"]/li').get_attribute('reqd'), '1', '必须输入设置失败')

    def test4(self):
        '''不许重复'''
        SettingOptUtils.popt_unique(self.driver)
        BasicAction.preview(self.driver)
        self.assertEqual(self.driver.find_element_by_xpath('//*[@id="fields"]/li').get_attribute('uniq'), '1', '不许重复设置失败')

    def test5(self):
        '''登录用户可见'''
        SettingOptUtils.sec_pri(self.driver)
        BasicAction.preview(self.driver)
        self.assertIsNone(self.driver.find_element_by_xpath('//*[@id="fields"]/li').get_attribute('typ'),'登录用户可见设置失败')

    def test6(self):
        '''范围'''
        SettingOptUtils.daterange(self.driver)
        BasicAction.preview(self.driver)
        self.assertEqual(self.driver.find_element_by_css_selector('[typ="date"]').get_attribute("dtmin"), '2018-08-01','最小值设置失败')
        self.assertEqual(self.driver.find_element_by_css_selector('[typ="date"]').get_attribute("dtmax"), '2018-08-31', '最大值设置失败')

    def test7(self):
        '''默认值'''
        SettingOptUtils.defval_text(self.driver, 'defval_date', '2018-08-23')
        BasicAction.preview(self.driver)
        self.assertEqual(self.driver.find_element_by_xpath('//*[@id="fields"]/li').get_attribute('def'),'2018-08-23','默认值设置失败')

    def test8(self):
        '''字段说明'''
        SettingOptUtils.instruct(self.driver)
        BasicAction.preview(self.driver)
        self.assertEqual(self.driver.find_element_by_xpath('//*[@id="p0"]').text,'字段说明','字段说明设置失败')

    def test9(self):
        '''字段宽度'''
        SettingOptUtils.element_format(self.driver, 'selLayout')
        BasicAction.preview(self.driver)
        self.assertIn('leftHalf', self.driver.find_element_by_xpath('//*[@id="fields"]/li').get_attribute('class'),'字段宽度设置失败')

    def test10(self):
        '''CSS名称'''
        SettingOptUtils.css(self.driver)
        BasicAction.preview(self.driver)
        self.assertIn('[class=desc]', self.driver.find_element_by_xpath('//*[@id="fields"]/li').get_attribute('class'),'CSS名称设置失败')

    def test11(self):
        '''提交数据'''
        self.formid = BasicAction.preview(self.driver)
        self.driver.find_element_by_css_selector('[class="yyyy input fld"]').send_keys('2018')
        self.driver.find_element_by_css_selector('[class="mm input fld"]').send_keys('08')
        self.driver.find_element_by_css_selector('[class="dd input fld"]').send_keys('20')
        self.driver.find_element_by_id('btnSubmit').click()
        sleep(1)
        self.assertEqual('2018-08-20',DataUtils.verify_data(url, self.formid)['F1'],'提交数据失败')

    def tearDown(self):
        self.driver.get(url[2])
        BasicAction.delete(self.driver)
        self.driver.close()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()