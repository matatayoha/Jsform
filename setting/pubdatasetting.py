# -*- coding: utf-8 -*-
# @Time    : 2018/8/29 0029 14:04
# @Author  : biubiubiu
# @FileName: pubdatasetting.py
# @Software: PyCharm
from code.login import Login
from time import  sleep
import unittest
from runner import url
from code.basicaction import BasicAction


class PubdataSetting(unittest.TestCase):
    '''公开查询'''

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
        self.driver.switch_to.window(self.driver.window_handles[0])
        self.driver.get(url[0] + 'app/formmain/' + self.formid + '?setstep=2')
        self.driver.find_element_by_css_selector('[menuindex="m03"]').click()
        self.driver.switch_to_frame('settingform')
        sleep(0.5)
        self.driver.find_element_by_css_selector('[for="chkPublicData"]').click()
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="fdSetting"]/div[3]/span').click()
        self.driver.find_element_by_css_selector('.dk-selected').click()
        self.driver.find_element_by_css_selector('[data-value="ID"]').click()

    def test1(self):
        '地址'
        BasicAction.search(self.driver)
        self.assertIn('查询',self.driver.find_element_by_css_selector('h2').text,'地址跳转失败')

    def test2(self):
        '查询文案'
        self.driver.find_element_by_xpath('//*[@id="fdSetting"]/div[2]/span').click()
        self.driver.find_element_by_id('txtTitle').clear()
        self.driver.find_element_by_id('txtTitle').send_keys('测试查询')
        BasicAction.search(self.driver)
        self.assertIn('测试', self.driver.find_element_by_css_selector('h2').text, '查询文案修改失败')


    def tearDown(self):

        self.driver.get(url[0] + 'app/formmain/' + self.formid + '?setstep=2')
        self.driver.find_element_by_css_selector('[menuindex="m03"]').click()
        self.driver.switch_to_frame('settingform')
        sleep(0.5)
        self.driver.find_element_by_css_selector('[for="chkPublicData"]').click()
        sleep(1)

    @classmethod
    def tearDownClass(cls):
        cls.driver.get(url[2])
        BasicAction.delete(cls.driver)
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()