# -*- coding: utf-8 -*-
# @Time    : 2018/8/27 0027 17:59
# @Author  : biubiubiu
# @FileName: basicsetting.py
# @Software: PyCharm

from code.login import Login
from code.getdata import DataUtils
from time import  sleep
import unittest
from runner import url
from code.basicaction import BasicAction


class BasicSetting(unittest.TestCase):
    '''基础设置'''


    def set(self):

        self.driver.find_element_by_name('SCHACT').send_keys('测试访问时间限制')
        self.driver.find_element_by_name('MAXENTRIESLIMIT').send_keys('测试限制提交数量')
        self.driver.find_element_by_name('WEIXINLMT').send_keys('测试每个微信只能提交一次')
        self.driver.find_element_by_name('IPLMT').send_keys('测试每IP只允许提交一次')
        self.driver.find_element_by_name('UNIQ').send_keys('测试不许重复')
        self.driver.find_element_by_name('DTLMT').send_keys('测试每天每电脑/手机提交次数限制')
        self.driver.switch_to_default_content()
        self.driver.find_element_by_xpath('//*[@id="topActions"]/div[3]/a[2]').click()


    @classmethod
    def setUpClass(cls):
        cls.Login = Login()
        cls.Login.login()
        cls.driver = cls.Login.driver
        cls.driver.get(url[0]+'app/formmain/add?groupid=')
        sleep(1)
        cls.driver.find_element_by_id('sl').click()
        cls.formid = BasicAction.preview(cls.driver)
        cls.driver.get(url[0]+'app/formmain/'+cls.formid+'?setstep=2')
        cls.driver.find_element_by_css_selector('[menuindex="m04"]').click()
        cls.driver.switch_to_frame('settingform')
        cls.set(cls)



    def setUp(self):
        self.driver.get(url[0]+'app/formmain/'+self.formid+'?setstep=2')
        self.driver.find_element_by_css_selector('[menuindex="m01"]').click()
        self.driver.switch_to_frame('settingform')
        BasicAction.clear(self.driver)

    def test1(self):
        '只能在微信中填写'
        self.driver.find_element_by_css_selector('[for="chkonlywx"]').click()
        BasicAction.view(self.driver,self.formid,url)
        self.assertIn('微信',self.driver.find_element_by_xpath('/html/body/div/div[1]/div/p').text,'只能在微信中填写修改失败')

    def test2(self):
        '每个IP只允许提交一次'
        self.driver.find_element_by_css_selector('[for="onePerIp"]').click()
        BasicAction.view(self.driver, self.formid,url)
        self.driver.find_element_by_id('btnSubmit').click()
        self.driver.refresh()
        self.driver.find_element_by_id('btnSubmit').click()
        self.assertIn('测试',self.driver.find_element_by_css_selector('[class="error-content"]').text,'每个IP只允许提交一次修改失败')

    def test3(self):
        '自动填充上次填写数据'
        self.driver.find_element_by_css_selector('[for="chkAutoFill"]').click()
        BasicAction.view(self.driver, self.formid, url)
        self.driver.find_element_by_id('tmpid').send_keys('1')
        self.driver.find_element_by_id('btnSubmit').click()
        self.driver.refresh()
        js = "return $('input[name=F1]').val();"
        self.assertIn('1', self.driver.execute_script(js), '自动填充上次填写数据修改失败')

    def test4(self):
        '表单只允许在规定的时间范围内访问'
        self.driver.find_element_by_css_selector('[for="schActive"]').click()
        self.driver.find_element_by_css_selector('[for="dailyrange"]').click()
        self.driver.find_element_by_xpath('//*[@id="startTime"]/span[5]/div/div').click()
        self.driver.find_element_by_xpath('//*[@id="startTime"]/span[5]/div/ul/li[2]').click()
        self.driver.find_element_by_xpath('//*[@id="startTime"]/span[6]/div/div').click()
        self.driver.find_element_by_xpath('//*[@id="startTime"]/span[6]/div/ul/li[2]').click()
        self.driver.find_element_by_xpath('//*[@id="endTime"]/span[5]/div/div').click()
        self.driver.find_element_by_xpath('//*[@id="endTime"]/span[5]/div/ul/li[3]').click()
        self.driver.find_element_by_xpath('//*[@id="endTime"]/span[6]/div/div').click()
        self.driver.find_element_by_xpath('//*[@id="endTime"]/span[6]/div/ul/li[3]').click()
        BasicAction.view(self.driver, self.formid, url)
        self.assertIn('测试',self.driver.find_element_by_css_selector('[class="error-content"]').text,'表单只允许在规定的时间范围内访问修改失败')

    def test5(self):
        '收集条数据量后关闭表单'
        self.driver.find_element_by_css_selector('[for="collect"]').click()
        self.driver.find_element_by_css_selector('[id="entriesLimit"]').send_keys('1')
        BasicAction.view(self.driver, self.formid, url)
        self.driver.find_element_by_id('btnSubmit').click()
        self.assertIn('测试', self.driver.find_element_by_css_selector('[class="error-content"]').text,
                      '收集条数据量后关闭表单修改失败')

    def test6(self):
        '每天每台电脑/手机限填'
        self.driver.find_element_by_css_selector('[id="entriesLimit"]').clear()
        self.driver.find_element_by_css_selector('[for="dailytime"]').click()
        self.driver.find_element_by_css_selector('[id="dailytimelimit"]').send_keys('1')
        BasicAction.view(self.driver, self.formid, url)
        self.driver.find_element_by_id('btnSubmit').click()
        self.driver.refresh()
        self.driver.find_element_by_id('btnSubmit').click()
        self.assertIn('测试',self.driver.find_element_by_css_selector('[class="msg"]').text,'每天每台电脑/手机限填修改失败')

    def test7(self):
        '启用IP黑名单'
        self.driver.find_element_by_css_selector('[id="dailytimelimit"]').clear()
        self.driver.find_element_by_css_selector('[for="chkIPcontrol"]').click()
        self.driver.find_element_by_css_selector('[name="IPBLACKLIST"]').send_keys(DataUtils.verify_data(url, self.formid)['IP'])
        BasicAction.view(self.driver, self.formid, url)
        self.driver.find_element_by_id('btnSubmit').click()
        self.assertIn('禁止', self.driver.find_element_by_css_selector('[class="error-content"]').text,
                      '启用IP黑名单修改失败')

    def test8(self):
        '表单别名'
        self.driver.find_element_by_id('alias').send_keys('表单别名')
        self.driver.switch_to_default_content()
        self.driver.find_element_by_xpath('//*[@id="topActions"]/div[3]/a[2]').click()
        self.driver.get(url[2])
        self.assertEqual(self.driver.find_element_by_xpath('//*[@id="' + self.formid + '"]/div[2]/h4/a/span').text,'表单别名',
                         '表单别名修改失败')

    def test9(self):
        '语言'
        self.driver.find_element_by_id('en').click()
        BasicAction.view(self.driver, self.formid, url)
        self.assertEqual('Submit',self.driver.find_element_by_id('btnSubmit').get_attribute("value"),'语言')

    def test99(self):
        '验证码'
        self.driver.find_element_by_xpath('//*[@id="form1"]/fieldset[3]/div[2]/div').click()
        self.driver.find_element_by_xpath('//*[@id="form1"]/fieldset[3]/div[2]/div/ul/li[2]').click()
        BasicAction.view(self.driver, self.formid, url)
        self.assertIn(' ',self.driver.find_element_by_xpath('//*[@id="liCaptcha"]/div/small').text,
                      '验证码')


    @classmethod
    def tearDownClass(cls):
        cls.driver.get(url[2])
        BasicAction.delete(cls.driver)
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()



