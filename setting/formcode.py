# -*- coding: utf-8 -*-
# @Time    : 2018/8/28 0028 17:53
# @Author  : biubiubiu
# @FileName: formcode.py
# @Software: PyCharm

from code.login import Login
from time import  sleep
import unittest
from runner import url
from code.basicaction import BasicAction


class FormCode(unittest.TestCase):
    '''发布页面'''

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
        self.driver.get(url[0]+'app/formmain/'+self.formid+'?setstep=2')
        self.driver.find_element_by_xpath('//*[@id="topActions"]/div[2]/span[8]/span').click()

    def test1(self):
        '凭密码才能访问'
        self.driver.find_element_by_css_selector('#divPublic > table > tbody > tr > td:nth-child(1) > div > div').click()
        self.driver.find_element_by_css_selector('#divPublic > table > tbody > tr > td:nth-child(1) > div > ul > li:nth-child(2)').click()
        self.driver.find_element_by_css_selector('[name="PWD"]').clear()
        self.driver.find_element_by_css_selector('[name="PWD"]').send_keys('123')
        BasicAction.view(self.driver, self.formid, url)
        self.assertIsNotNone(self.driver.find_element_by_xpath('//*[@id="form1"]/label[2]'),'凭密码才能访问修改失败')

    @classmethod
    def tearDownClass(cls):
        cls.driver.get(url[2])
        BasicAction.delete(cls.driver)
        cls.driver.quit()



if __name__ == '__main__':
    unittest.main()