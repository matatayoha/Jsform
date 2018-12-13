# -*- coding: utf-8 -*-
# @Time    : 2018/9/17 0017 16:43
# @Author  : biubiubiu
# @FileName: action.py
# @Software: PyCharm


from code.login import Login
from time import  sleep
import unittest
from runner import url
from code.basicaction import BasicAction

class Action(unittest.TestCase):
    '''数据单条操作'''

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

    def AddData(self):
        js = "$('#btnCreateNew').click()"
        self.driver.execute_script(js)
        self.driver.find_element_by_id('tmpid').send_keys(1234)
        self.driver.find_element_by_id('btnSave').click()
        sleep(0.5)



    def setUp(self):
        self.driver.switch_to.window(self.driver.window_handles[0])
        self.driver.get(url[0] + 'app/entries/' + self.formid)

    def test1(self):
        '修改'
        self.AddData()
        self.driver.find_element_by_xpath('//*[@id="entriesGrid"]/tbody/tr[1]/td[3]/span/a[1]').click()
        self.driver.find_element_by_id('tmpid').send_keys(5)
        self.driver.find_element_by_id('btnSave').click()
        text = self.driver.find_element_by_xpath('//*[@id="entriesGrid"]/tbody/tr[1]/td[5]').text
        self.assertNotEqual(text,'5','修改失败')

    def test2(self):
        '查看'
        self.AddData()
        self.driver.find_element_by_xpath('//*[@id="entriesGrid"]/tbody/tr[1]/td[3]/span/a[2]').click()
        self.assertEqual(self.driver.find_element_by_id('formHeader').get_attribute('class'),'info','查看失败')
        self.driver.find_element_by_xpath('//*[@id="lbContent"]/div[1]/a').click()

    def test3(self):
        '将此条数据通过邮件发送'
        self.AddData()
        self.driver.find_element_by_xpath('//*[@id="entriesGrid"]/tbody/tr[1]/td[3]/span/a[2]').click()
        self.driver.find_element_by_id('btnActema2').click()
        sleep(1)
        num = self.driver.find_element_by_id('mailremain').text
        self.driver.find_element_by_id('senddata-email').send_keys('798337031@qq.com')
        self.driver.find_element_by_id('sendmailbtn').click()
        sleep(2)
        num2 = self.driver.find_element_by_id('mailremain').text
        self.assertTrue(int(num) - int(num2) > 0, '将此条数据通过邮件发送失败')
        self.driver.find_element_by_id('cancelsendmail').click()

    def test4(self):
        '删除'
        self.AddData()
        id = self.driver.find_element_by_xpath('//*[@id="entriesGrid"]/tbody/tr[1]/td[4]').text
        self.driver.find_element_by_xpath('//*[@id="entriesGrid"]/tbody/tr[1]/td[3]/span/a[2]').click()
        self.driver.find_element_by_id('btnActDel2').click()
        self.driver.find_element_by_id('txtConfirmYes').send_keys('yes')
        self.driver.find_element_by_css_selector('.btnconfirm.btn.small.right.red').click()
        id2 = self.driver.find_element_by_xpath('//*[@id="entriesGrid"]/tbody/tr[1]/td[4]').text
        self.assertTrue(int(id)-int(id2)>0,'删除失败')

    def test5(self):
        '标星'
        self.AddData()
        self.driver.find_element_by_xpath('//*[@id="entriesGrid"]/tbody/tr[1]/td[3]/span/a[2]').click()
        self.driver.find_element_by_id('btnActNoStar2').click()
        self.driver.get(url[0] + 'app/entries/' + self.formid)
        sleep(1)
        status = self.driver.find_element_by_xpath('//*[@id="entriesGrid"]/tbody/tr[1]/td[3]/span/a[5]').get_attribute('class')
        self.assertIn('hide',status,'标星失败')

    def test6(self):
        '标记为已处理'
        self.AddData()
        self.driver.find_element_by_xpath('//*[@id="entriesGrid"]/tbody/tr[1]/td[3]/span/a[2]').click()
        self.driver.find_element_by_id('btnActNoProcessed2').click()
        self.driver.get(url[0] + 'app/entries/' + self.formid)
        sleep(1)
        status = self.driver.find_element_by_xpath('//*[@id="entriesGrid"]/tbody/tr[1]/td[3]/span/a[7]').get_attribute('class')
        self.assertIn('hide', status, '标记为已处理失败')

    def test7(self):
        '复制'
        self.AddData()
        id = self.driver.find_element_by_xpath('//*[@id="entriesGrid"]/tbody/tr[1]/td[4]').text
        self.driver.find_element_by_xpath('//*[@id="entriesGrid"]/tbody/tr[1]/td[3]/span/a[3]').click()
        self.driver.find_element_by_css_selector('.btnconfirm.btn.small.right.blue').click()
        sleep(0.5)
        id2 = self.driver.find_element_by_xpath('//*[@id="entriesGrid"]/tbody/tr[1]/td[4]').text
        self.assertTrue(int(id2) - int(id) > 0, '复制失败')


    @classmethod
    def tearDownClass(cls):
        cls.driver.get(url[2])
        BasicAction.delete(cls.driver)
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()
