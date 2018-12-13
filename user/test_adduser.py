# -*- coding: utf-8 -*-
# @Time    : 2018/9/18 0018 10:09
# @Author  : biubiubiu
# @FileName: test_adduser.py
# @Software: PyCharm


from code.login import Login
from time import  sleep
import unittest,os
from runner import url
from selenium import webdriver


class AddUser(unittest.TestCase):
    '''填加用户'''

    def login(self,un,pd):
        driver = webdriver.Firefox()
        driver.get(url[4])
        driver.find_element_by_id('userName').send_keys(un)
        driver.find_element_by_id('pwd').send_keys(pd)
        driver.find_element_by_id('btnLogin').click()
        sleep(1)
        text = driver.find_element_by_css_selector('.text.login-div-btn').text
        driver.quit()
        return text


    @classmethod
    def setUpClass(cls):
        cls.Login = Login()
        cls.Login.login()
        cls.driver = cls.Login.driver


    def setUp(self):
        self.driver.get(url[0] + 'app/user/manage')

    def test1(self):
        '创建一个新的用户'
        js = "document.getElementById('newUserButton').click();"
        self.driver.execute_script(js)
        sleep(0.5)
        self.driver.find_element_by_id('info_userName').clear()
        self.driver.find_element_by_id('info_userName').send_keys('123123@123.com')
        self.driver.find_element_by_id('info_pwd').clear()
        self.driver.find_element_by_id('info_pwd').send_keys('123456')
        self.driver.find_element_by_id('btnConfirm').click()
        text = self.login('123123@123.com','123456')
        self.assertIn('3',text,'创建一个新的用户失败')

    def test2(self):
        '批量导入用户'
        js = "document.getElementById('importUserButton').click();"
        self.driver.execute_script(js)
        sleep(0.5)
        self.driver.find_element_by_id('fileExcel').send_keys('%s\\user.xls' % os.getcwd())
        sleep(0.5)
        self.driver.find_element_by_id('btnImportNext').click()
        self.driver.find_element_by_id('btnCancel').click()
        sleep(0.5)
        text = self.login('123126@123.com', '123456')
        self.assertIn('6', text, '批量导入用户失败')



    def tearDown(self):
        self.driver.get(url[0] + 'app/user/manage')
        for i in range(1,10):
            text = self.driver.find_element_by_xpath('//*[@id="userList-table"]/tbody/tr['+str(i)+']/td[4]').text
            if '123' in text:
                self.driver.find_element_by_xpath('//*[@id="userList-table"]/tbody/tr['+str(i)+']/td[1]/span/i[3]').click()
                self.driver.find_element_by_css_selector('.btnconfirm.btn.small.right.red').click()
                sleep(1)
            else:
                pass


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()