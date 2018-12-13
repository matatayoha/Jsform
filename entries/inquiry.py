# -*- coding: utf-8 -*-
# @Time    : 2018/9/17 0017 15:17
# @Author  : biubiubiu
# @FileName: inquiry.py
# @Software: PyCharm


from code.login import Login
from time import  sleep
import unittest
from runner import url
from code.basicaction import BasicAction

class Inquiry(unittest.TestCase):
    '''数据查询显示'''

    @classmethod
    def setUpClass(cls):
        cls.Login = Login()
        cls.Login.login()
        cls.driver = cls.Login.driver
        cls.driver.get(url[0]+'app/formmain/add?groupid=')
        sleep(1)
        cls.driver.find_element_by_id('sl').click()
        cls.driver.find_element_by_id('nb').click()
        cls.driver.find_element_by_id('ph').click()
        cls.driver.find_element_by_id('em').click()
        cls.formid = BasicAction.preview(cls.driver)
        cls.driver.close()




    def setUp(self):
        self.driver.switch_to.window(self.driver.window_handles[0])
        self.driver.get(url[0] + 'app/entries/' + self.formid)

    def test1(self):
        '关键字查询'
        js = "$('#btnCreateNew').click()"
        self.driver.execute_script(js)
        self.driver.find_element_by_css_selector('[name="F4"]').send_keys('798337031@qq.com')
        self.driver.find_element_by_id('btnSave').click()
        js = "$('#btnSearchController').click();$('#txtSearch').val(4).change()"
        self.driver.execute_script(js)
        self.driver.find_element_by_id('dash').click()
        text = self.driver.find_element_by_xpath('//*[@id="entriesGrid"]/tbody/tr[1]/td[4]').text
        self.assertNotEqual(text,'1','关键字查询失败')

    def test2(self):
        '显示或者隐藏查询方案'
        js = "$('#btnCreateNew').click()"
        self.driver.execute_script(js)
        self.driver.find_element_by_id('tmpid').send_keys(1234)
        self.driver.find_element_by_id('btnSave').click()
        js = "$('#btnAdvanceFilter').click()"
        self.driver.execute_script(js)
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="dsUL"]/li[2]/span[1]/div/div').click()
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="dsUL"]/li[2]/span[1]/div/ul/li[2]').click()
        sleep(1)
        self.driver.find_element_by_css_selector('.text.conditionValue').send_keys(2)
        self.driver.find_element_by_id('btnQuery').click()
        text = self.driver.find_element_by_xpath('//*[@id="entriesGrid"]/tbody/tr[1]/td[4]').text
        self.assertNotEqual(text, '1', '显示或者隐藏查询方案')

    def test3(self):
        '显示表单字段'
        js = "$('#plus').click()"
        self.driver.execute_script(js)
        self.driver.find_element_by_xpath('//*[@id="dash"]/table[1]/tbody/tr/td[3]/ul/li[5]/a').click()
        text = self.driver.find_element_by_css_selector('[field="F3"]').get_attribute('class')
        self.assertNotIn('hide',text,'显示表单字段失败')




    @classmethod
    def tearDownClass(cls):
        cls.driver.get(url[2])
        BasicAction.delete(cls.driver)
        cls.driver.quit()