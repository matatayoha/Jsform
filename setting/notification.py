# -*- coding: utf-8 -*-
# @Time    : 2018/8/29 0029 14:45
# @Author  : biubiubiu
# @FileName: notification.py
# @Software: PyCharm

from code.login import Login
from time import  sleep
import unittest
from runner import url
from code.basicaction import BasicAction


class Notification(unittest.TestCase):
    '''提醒'''

    @classmethod
    def setUpClass(cls):
        cls.Login = Login()
        cls.Login.login()
        cls.driver = cls.Login.driver
        cls.driver.get(url[0]+'app/formmain/add?groupid=')
        sleep(1)
        cls.driver.find_element_by_id('sl').click()
        cls.formid = BasicAction.preview(cls.driver)

    def setUp(self):
        self.driver.get(url[0] + 'app/formmain/' + self.formid + '?setstep=2')
        self.driver.find_element_by_css_selector('#setting_menu > li:nth-child(2) > h2').click()

    def test1(self):
        '微信提醒'
        self.driver.find_element_by_css_selector('[menuindex="m11"]').click()
        self.driver.switch_to_frame('settingform')
        self.driver.find_element_by_id('btnAddNoiti').click()
        self.driver.find_element_by_id('receiver').click()
        self.driver.find_element_by_xpath('//*[@id="divUsers"]/div/ul/li/div/div/label').click()
        self.driver.find_element_by_css_selector('.btn.confirm.blue').click()
        self.assertEqual('798337031@qq.com',self.driver.find_element_by_id('receiver').get_attribute('value'),
                         '微信提醒修改成功')

    def test2(self):
        '邮件提醒'
        self.driver.find_element_by_css_selector('[menuindex="m12"]').click()
        self.driver.switch_to_frame('settingform')
        self.driver.find_element_by_css_selector('.btn.blue.lg').click()
        self.driver.find_element_by_id('txtFix').send_keys('798337031@qq.com')
        self.assertEqual('798337031@qq.com',self.driver.find_element_by_id('txtFix').get_attribute('value'),
                         '邮件提醒修改成功')

    def test3(self):
        '短信提醒'
        self.driver.find_element_by_css_selector('[menuindex="m13"]').click()
        self.driver.switch_to_frame('settingform')
        self.driver.find_element_by_css_selector('.btn.blue.lg').click()
        self.driver.find_element_by_id('txtFix').send_keys('18017618707')
        self.assertEqual('18017618707',self.driver.find_element_by_id('txtFix').get_attribute('value'),
                         '短信提醒修改成功')
    def tearDown(self):
        self.driver.switch_to_default_content()

    @classmethod
    def tearDownClass(cls):
        cls.driver.get(url[2])
        BasicAction.delete(cls.driver)
        cls.driver.quit()