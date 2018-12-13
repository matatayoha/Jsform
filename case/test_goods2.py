# -*- coding: utf-8 -*-
# @Time    : 2018/8/22 0022 16:55
# @Author  : biubiubiu
# @FileName: text.py
# @Software: PyCharm


from code.login import Login
from code.property import SettingOptUtils
from code.getdata import DataUtils
from time import  sleep
import unittest,os
from runner import url
from code.basicaction import BasicAction


class Goods2(unittest.TestCase):
    '''测试无图商品'''


    @classmethod
    def setUpClass(cls):
        cls.Login = Login()
        cls.Login.login()
        cls.driver = cls.Login.driver

    def setUp(self):
        self.driver.switch_to.window(self.driver.window_handles[0])
        self.driver.get(url[0]+'app/formmain/add?groupid=')
        sleep(1)
        self.driver.find_element_by_id('gd2').click()


    def test1(self):
        '''修改名称'''
        SettingOptUtils.element_name(self.driver)
        BasicAction.preview(self.driver)
        self.assertEqual(self.driver.find_element_by_xpath('//*[@id="fields"]/li/label').text,'组件改名','组件改名失败')

    def test2(self):
        '''商品列表'''
        self.driver.find_element_by_id("addNoImgGoods").click()
        self.driver.find_element_by_class_name('goods-name-view').click()
        SettingOptUtils.pgoods(self.driver)
        BasicAction.preview(self.driver)
        self.assertEqual('商品名称测试商品(剩余40)', self.driver.find_element_by_class_name('name').text, '商品名设置失败')
        self.assertIn('测试', self.driver.find_element_by_class_name('des').text, '商品描述设置失败')
        self.assertIn('2', self.driver.find_element_by_class_name('price').text, '商品价格设置失败')
        self.assertIn('2', self.driver.find_element_by_class_name('number').get_attribute('value'), '商品默认值数量设置失败')

    def test3(self):
        '''必须输入'''
        SettingOptUtils.popt_required(self.driver)
        BasicAction.preview(self.driver)
        self.assertEqual(self.driver.find_element_by_xpath('//*[@id="fields"]/li').get_attribute('reqd'), '1', '必须输入设置失败')

    def test4(self):
        '''登录用户可见'''
        SettingOptUtils.sec_pri(self.driver)
        BasicAction.preview(self.driver)
        self.assertIsNone(self.driver.find_element_by_xpath('//*[@id="fields"]/li').get_attribute('typ'),'登录用户可见设置失败')


    def test5(self):
        '''CSS名称'''
        SettingOptUtils.css(self.driver)
        BasicAction.preview(self.driver)
        self.assertIn('[class=desc]', self.driver.find_element_by_xpath('//*[@id="fields"]/li').get_attribute('class'),'CSS名称设置失败')

    def test6(self):
        '''提交数据'''
        self.driver.find_element_by_id("addNoImgGoods").click()
        self.driver.find_element_by_class_name('goods-name-view').click()
        SettingOptUtils.pgoods(self.driver)
        self.formid = BasicAction.preview(self.driver)
        self.driver.find_element_by_id('btnSubmit').click()
        sleep(1)
        self.assertEqual(2.0,DataUtils.verify_data(url, self.formid)['F1'],'提交数据失败')

    def tearDown(self):
        self.driver.get(url[2])
        BasicAction.delete(self.driver)
        self.driver.close()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()