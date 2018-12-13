# -*- coding: utf-8 -*-
# @Time    : 2018/9/12 0012 17:42
# @Author  : biubiubiu
# @FileName: relation.py
# @Software: PyCharm

from code.login import Login
from time import  sleep
import unittest
from runner import url
from code.basicaction import BasicAction

class Relation(unittest.TestCase):
    '''关联'''

    @classmethod
    def setUpClass(cls):
        cls.Login = Login()
        cls.Login.login()
        cls.driver = cls.Login.driver
        cls.driver.get(url[0]+'app/formmain/add?groupid=')
        sleep(0.5)
        cls.driver.find_element_by_id("formName").clear()
        cls.driver.find_element_by_id("formName").send_keys("测试表单关联1")
        cls.driver.find_element_by_id('sl').click()
        cls.formid = BasicAction.preview(cls.driver)
        cls.driver.find_element_by_css_selector('[name="F1"]').send_keys(10)
        cls.driver.find_element_by_id('btnSubmit').click()
        cls.driver.close()
        cls.driver.switch_to.window(cls.driver.window_handles[0])
        cls.driver.get(url[0]+'app/formmain/add?groupid=')
        sleep(0.5)
        cls.driver.find_element_by_id("formName").clear()
        cls.driver.find_element_by_id("formName").send_keys("测试表单关联2")
        cls.driver.find_element_by_id('sl').click()
        cls.formid = BasicAction.preview(cls.driver)
        sleep(0.5)
        cls.driver.find_element_by_id('btnSubmit').click()



    def setUp(self):
        self.driver.switch_to.window(self.driver.window_handles[0])
        self.driver.get(url[0] + 'app/formmain/' + self.formid + '?setstep=2')
        self.driver.find_element_by_css_selector('#setting_menu > li:nth-child(4) > h2').click()


    def test1(self):
        '数据查看关联'
        self.driver.find_element_by_css_selector('[menuindex="m31"]').click()
        self.driver.switch_to_frame('settingform')
        self.driver.find_element_by_id('btnCreate').click()
        self.driver.find_element_by_xpath('//*[@id="dsUL"]/li/div[4]/div').click()
        self.driver.find_element_by_xpath('//*[@id="dsUL"]/li/div[4]/ul/li[3]').click()
        self.driver.find_element_by_id('btnSaveFieldsRule').click()
        self.driver.get(url[0]+'app/entries/'+self.formid)
        self.driver.find_element_by_xpath('//*[@id="entriesGrid"]/tbody/tr[1]/td[4]').click()
        self.driver.find_element_by_xpath('//*[@id="relationforms"]/li').click()
        self.assertEqual(self.driver.find_element_by_css_selector('tr.even td').text,'1','数据查看关联失败')

    def test2(self):
        '数据填写关联'
        self.driver.find_element_by_css_selector('[menuindex="m32"]').click()
        self.driver.switch_to_frame('settingform')
        self.driver.find_element_by_id('btnCreateRelation').click()
        self.driver.find_element_by_xpath('//span[1]/div/div').click()
        self.driver.find_element_by_xpath('//span[1]/div/ul/li[2]').click()
        self.driver.find_element_by_xpath('//span[3]/div/div').click()
        self.driver.find_element_by_xpath('//span[3]/div/ul/li[2]').click()
        self.driver.find_element_by_xpath('//span[5]/div/div').click()
        self.driver.find_element_by_xpath('//span[5]/div/ul/li[2]').click()
        self.driver.find_element_by_css_selector('.btn.blue.save-relation-a').click()
        self.driver.get(url[0] + 'web/formview/' + self.formid)
        self.driver.find_element_by_css_selector('[name="F1"]').send_keys(1)
        sleep(1)
        js = 'return $(".content").html()'
        self.assertIn('matul',self.driver.execute_script(js),'数据填写关联失败')





    @classmethod
    def tearDownClass(cls):
        cls.driver.get(url[2])
        BasicAction.delete(cls.driver)
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()