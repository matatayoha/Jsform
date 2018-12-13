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

class Verify(unittest.TestCase):
    '''扩展应用'''

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
        self.driver.find_element_by_css_selector('#setting_menu > li:nth-child(6) > h2').click()


    def test1(self):
        '设置核销码'
        self.driver.find_element_by_css_selector('[menuindex="m62"]').click()
        self.driver.switch_to_frame('settingform')
        self.driver.find_element_by_css_selector('[for="verify"]').click()
        self.driver.find_element_by_name('VERIFYTEXT').send_keys('测试核销码')
        self.driver.find_element_by_id('expdateType').click()
        self.driver.find_element_by_css_selector('[value="dynamicDate"]').click()
        self.driver.find_element_by_id('dynamicDays').send_keys(2)
        self.formid = BasicAction.preview(self.driver)
        self.driver.find_element_by_id('btnSubmit').click()
        self.assertIsNotNone(self.driver.find_element_by_id('p1'),'核销码设置成功')



    @classmethod
    def tearDownClass(cls):
        cls.driver.get(url[2])
        BasicAction.delete(cls.driver)
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()