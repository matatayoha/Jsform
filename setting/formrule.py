# -*- coding: utf-8 -*-
# @Time    : 2018/9/4 0004 14:08
# @Author  : biubiubiu
# @FileName: formrule.py
# @Software: PyCharm

from code.login import Login
from time import  sleep
import unittest
from runner import url
from code.basicaction import BasicAction


class FormRule(unittest.TestCase):
    '''逻辑'''

    @classmethod
    def setUpClass(cls):
        cls.Login = Login()
        cls.Login.login()
        cls.driver = cls.Login.driver
        cls.driver.get(url[0]+'app/formmain/add?groupid=')
        sleep(1)
        cls.driver.find_element_by_id('nb').click()
        cls.driver.find_element_by_id('f0').click()
        cls.driver.find_element_by_id('lbl').send_keys('1')
        cls.driver.find_element_by_id('nb').click()
        cls.driver.find_element_by_id('f1').click()
        cls.driver.find_element_by_id('lbl').send_keys('2')
        cls.formid = BasicAction.preview(cls.driver)



    def setUp(self):
        self.driver.get(url[0] + 'app/formmain/' + self.formid + '?setstep=2')
        self.driver.find_element_by_xpath('//*[@id="setting_menu"]/li[3]/h2').click()



    def test1(self):
        '字段显示逻辑'
        self.driver.find_element_by_xpath('//*[@id="setting_menu"]/li[3]/ol/li[1]/a').click()
        self.driver.switch_to_frame('settingform')
        self.driver.find_element_by_id('btnCreateFieldRule').click()
        self.driver.find_element_by_xpath('//*[@id="rule0"]/td/div[2]/ul/li[1]/span[2]/div/div').click()
        self.driver.find_element_by_css_selector('[data-value="F1"]').click()
        self.driver.find_element_by_css_selector('[name="VAL"]').send_keys(2)
        self.driver.find_element_by_xpath('//*[@id="rule0"]/td/div[2]/ul/li[2]/span[2]/div/input').click()
        self.driver.find_element_by_css_selector('[title="数字框2"]').click()
        self.driver.find_element_by_css_selector('.btn.blue.save-rule-a').click()
        self.driver.get(url[0]+'web/formview/'+self.formid)
        self.driver.find_element_by_css_selector('[name="F1_number"]').send_keys(2)
        self.driver.find_element_by_css_selector('h2').click()
        self.assertNotEqual('hide',self.driver.find_element_by_xpath('//*[@id="fields"]/li[2]'),'字段显示逻辑修改失败')

    def test2(self):
        '表单提交逻辑'
        self.driver.find_element_by_xpath('//*[@id="setting_menu"]/li[3]/ol/li[2]/a').click()
        self.driver.switch_to_frame('settingform')
        self.driver.find_element_by_id('btnCreateCommitRule').click()
        self.driver.find_element_by_xpath('//*[@id="commitRulesTop"]/ul/li/table/tbody/tr/td/div[2]/ul/li[1]/span[2]/div/div').click()
        self.driver.find_element_by_css_selector('[data-value="F1"]').click()
        self.driver.find_element_by_css_selector('[name="VAL"]').send_keys(3)
        self.driver.find_element_by_css_selector('[name="MSG"]').send_keys('表单提交逻辑')
        self.driver.find_element_by_css_selector('.btn.blue.save-form-rule-a').click()
        self.driver.get(url[0] + 'web/formview/' + self.formid)
        self.driver.find_element_by_css_selector('[name="F1_number"]').send_keys(3)
        self.driver.find_element_by_id('btnSubmit').click()
        self.assertIn('逻辑',self.driver.find_element_by_css_selector('h2').text,'表单提交逻辑修改失败')

    def test3(self):
        '字段运算逻辑'
        self.driver.find_element_by_xpath('//*[@id="setting_menu"]/li[3]/ol/li[3]/a').click()
        self.driver.switch_to_frame('settingform')
        self.driver.find_element_by_id('btnCreateFun').click()
        self.driver.find_element_by_xpath('//*[@id="formula"]/div[1]/ul/li[2]').click()
        self.driver.find_element_by_xpath('//*[@id="formula"]/div[1]/ul/li[1]').click()
        self.driver.find_element_by_css_selector('[type="number"]').send_keys(2)
        self.driver.find_element_by_css_selector('[class="add-btn"]').click()
        self.driver.find_element_by_css_selector('[data-value="+"]').click()
        self.driver.find_element_by_css_selector('[data-value="2"]').click()
        self.driver.find_element_by_css_selector('.formula-save').click()
        self.driver.get(url[0] + 'web/formview/' + self.formid)
        self.driver.find_element_by_css_selector('[name="F1_number"]').send_keys(2)
        self.driver.find_element_by_css_selector('h2').click()
        self.assertEqual('4', self.driver.find_element_by_xpath('//*[@id="fields"]/li[2]/div/input').get_attribute('value'), '字段运算逻辑修改失败')




    @classmethod
    def tearDownClass(cls):
        cls.driver.get(url[2])
        BasicAction.delete(cls.driver)
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()