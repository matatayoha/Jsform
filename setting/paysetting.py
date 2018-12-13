# -*- coding: utf-8 -*-
# @Time    : 2018/9/13 0013 15:16
# @Author  : biubiubiu
# @FileName: paysetting.py
# @Software: PyCharm


from code.login import Login
from time import  sleep
import unittest
from runner import url
from code.basicaction import BasicAction
from code.property import SettingOptUtils

class PaySetting(unittest.TestCase):
    '''支付'''

    @classmethod
    def setUpClass(cls):
        cls.Login = Login()
        cls.Login.login()
        cls.driver = cls.Login.driver
        cls.driver.get(url[0]+'app/formmain/add?groupid=')
        sleep(1)
        cls.driver.find_element_by_id('gd2').click()
        cls.driver.find_element_by_id("addNoImgGoods").click()
        cls.driver.find_element_by_class_name('goods-name-view').click()
        SettingOptUtils.pgoods(cls.driver)
        cls.formid = BasicAction.preview(cls.driver)



    def setUp(self):
        self.driver.switch_to.window(self.driver.window_handles[0])
        self.driver.get(url[0] + 'app/formmain/' + self.formid + '?setstep=2')
        self.driver.find_element_by_css_selector('#setting_menu > li:nth-child(5) > h2').click()


    def test1(self):
        '支付参数'
        self.driver.find_element_by_css_selector('[menuindex="m41"]').click()
        self.driver.switch_to_frame('settingform')
        self.driver.find_element_by_css_selector('[for="sale"]').click()
        self.driver.find_element_by_id('salem').send_keys(4)
        self.driver.find_element_by_id('salej').send_keys(2)
        BasicAction.view(self.driver, self.formid, url)
        self.assertIn('折',self.driver.find_element_by_css_selector('.discount-container label').text,'支付参数失败')



    @classmethod
    def tearDownClass(cls):
        cls.driver.get(url[2])
        BasicAction.delete(cls.driver)
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()