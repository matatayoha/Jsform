# -*- coding: utf-8 -*-
# @Time    : 2018/8/22 0022 16:55
# @Author  : biubiubiu
# @FileName: text.py
# @Software: PyCharm


from code.login import Login
from code.property import SettingOptUtils
from code.getdata import DataUtils
from time import sleep
import unittest,os
from runner import url
from code.basicaction import BasicAction


class Skin(unittest.TestCase):
    '''测试皮肤'''

    @classmethod
    def setUpClass(cls):
        cls.Login = Login()
        cls.Login.login()
        cls.driver = cls.Login.driver

    def setUp(self):
        self.driver.switch_to.window(self.driver.window_handles[0])
        self.driver.get(url[0] + 'app/formmain/add?groupid=')
        sleep(1)
        self.driver.find_element_by_id('sl').click()
        self.driver.find_element_by_xpath('//*[@id="topActions"]/div[2]/span[4]').click()

    def test1(self):
        '''默认风格'''
        self.driver.find_element_by_xpath('//*[@id="defUlStyles"]/li[2]/a/div').click()
        BasicAction.preview(self.driver)
        js = "return $('.wallpaper').css('background-color')"
        color = self.driver.execute_script(js)
        self.assertEqual(color, 'rgb(34, 34, 34)', '默认风格修改失败')

    def test2(self):
        '''表头设置'''
        self.driver.find_element_by_id('phead').click()
        self.driver.find_element_by_xpath('//*[@id="pheadContainer"]/div[1]/div/div').click()
        self.driver.find_element_by_xpath('//*[@id="pheadContainer"]/div[1]/div/ul/li[1]').click()
        self.driver.find_element_by_xpath("//*[@id='fileCustomLogo']").send_keys('%s\\2.jpg'%os.getcwd())
        sleep(1)
        BasicAction.preview(self.driver)
        js = "return $('.logo a').css('background-image')"
        url = self.driver.execute_script(js)
        self.assertIn('url', url, '表头设置修改失败')

    def test3(self):
        '''表体设置-背景色'''
        self.driver.find_element_by_id('pbody').click()
        self.driver.find_element_by_id('bgContainer').click()
        self.driver.find_element_by_xpath('//*[@id="backgroudgraphy"]/div/div').click()
        self.driver.find_element_by_xpath('//*[@id="backgroudgraphy"]/div/ul/li[2]').click()
        self.driver.find_element_by_id('bgcolorSel').click()
        self.driver.find_element_by_xpath('//*[@id="bgcolorPre"]/div/div[2]/span/div/ul/li[1]').click()
        BasicAction.preview(self.driver)
        js = "return $('.input').css('background-color')"
        color = self.driver.execute_script(js)
        self.assertEqual(color, 'rgb(250, 221, 209)', '表体设置-背景色修改失败')

    def test4(self):
        '''表体设置-文字'''
        self.driver.find_element_by_id('pbody').click()
        self.driver.find_element_by_id('fontContainer').click()
        self.driver.find_element_by_xpath('//*[@id="typography"]/div/div').click()
        self.driver.find_element_by_xpath('//*[@id="typography"]/div/ul/li[3]').click()
        self.driver.find_element_by_id('colorSel').click()
        self.driver.find_element_by_xpath('//*[@id="colorPre"]/div/div[2]/span/div/ul/li[1]').click()
        BasicAction.preview(self.driver)
        js = "return $('.desc').css('color')"
        color = self.driver.execute_script(js)
        self.assertEqual(color, 'rgb(250, 221, 209)', '表体设置-文字修改失败')

    def test5(self):
        '''表体设置-按钮'''
        self.driver.find_element_by_id('pbody').click()
        self.driver.find_element_by_id('buttonContainer').click()
        # self.driver.find_element_by_xpath('//*[@id="buttonText"]/input').clear()
        # self.driver.find_element_by_xpath('//*[@id="buttonText"]/input').send_keys('按钮')
        self.driver.find_element_by_id('buttoncolorSel').click()
        self.driver.find_element_by_xpath('//*[@id="buttoncolorPre"]/div/div[2]/span/div/ul/li[1]').click()
        BasicAction.preview(self.driver)
        js = "return $('.btn-submit').css('color')"
        color = self.driver.execute_script(js)
        self.assertEqual(color, 'rgb(250, 221, 209)', '表体设置-按钮修改失败')

    # def test6(self):
    #     '''表体设置-边框'''
    #     self.driver.find_element_by_id('pbody').click()
    #     self.driver.find_element_by_id('borderContainer').click()
    #     self.driver.find_element_by_xpath('//*[@id="bordersMenu"]/div/div').click()
    #     self.driver.find_element_by_xpath('//*[@id="bordersMenu"]/div/ul/li[4]').click()
    #     self.driver.find_element_by_xpath('//*[@id="styleMenu"]/div/div').click()
    #     self.driver.find_element_by_xpath('//*[@id="styleMenu"]/div/ul/li[4]').click()
    #     BasicAction.preview(self.driver)
    #     js = "return $('.btn-submit').css('border-style')"
    #     style = self.driver.execute_script(js)
    #     self.assertEqual(style, 'double', '表体设置-边框修改失败')

    def tearDown(self):
        self.driver.get(url[2])
        BasicAction.delete(self.driver)
        self.driver.close()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
