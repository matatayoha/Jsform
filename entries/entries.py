# -*- coding: utf-8 -*-
# @Time    : 2018/9/13 0013 16:51
# @Author  : biubiubiu
# @FileName: entries.py
# @Software: PyCharm


from code.login import Login
from time import  sleep
import unittest
from runner import url
from code.basicaction import BasicAction
import os,requests,json
from selenium.webdriver.support.ui import Select
from http.cookiejar import CookieJar



class Entries(unittest.TestCase):
    '''数据批量操作'''
    def download(self,url):
        requests.packages.urllib3.disable_warnings()
        session = requests.session()  # 保持会话
        session.cookies = CookieJar()  # 设置存cookie的地方   这里能接受setcookie中的cookie
        # Headers信息
        head = {
            'Connection': 'keep-alive',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
            'Content-Type': 'application/json; charset=UTF-8',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9'
        }

        # 登陆Form_Data信息获得门户里面的cookies存在session.cookies中
        session.post(url[1], data=json.dumps(url[5]), headers=head, verify=False)
        # 登陆Form_Data信息获得表单大师里面的cookies存在session.cookies中
        session.get(url[2], cookies=session.cookies, headers=head, verify=False)
        data = {'FILETYPE': 'tab',
                'FRMID': self.formid,
                'MCHTYP': 'and',
                'CONDITIONSSTR': '[]'}
        head = {
            'Connection': 'keep-alive',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
            'Content-Type': 'multipart/form-data',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Accept': 'text / html, application / xhtml + xml, application / xml;q = 0.9, image / webp, image / apng, * / *;q = 0.8'
        }
        a = session.post(url[3], cookies=session.cookies, headers=head, data=data, verify=False)
        # print(a.status_code)
        # print(a.headers)
        fp = open('表单名称.txt', 'wb')
        fp.write(a.content)
        fp.close()
        return

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




    def setUp(self):
        self.driver.switch_to.window(self.driver.window_handles[0])
        self.driver.get(url[0] + 'app/entries/' + self.formid)


    def test1(self):
        '添加数据'
        js = "$('#btnCreateNew').click()"
        self.driver.execute_script(js)
        self.driver.find_element_by_id('tmpid').send_keys(1234)
        self.driver.find_element_by_css_selector('[fmt="mobile"]').send_keys(18017618707)
        self.driver.find_element_by_css_selector('[name="F4"]').send_keys('798337031@qq.com')
        self.driver.find_element_by_id('btnSave').click()
        self.assertEqual('1',self.driver.find_element_by_xpath('//*[@id="entriesGrid"]/tbody/tr[1]/td[4]').text,'添加数据失败')


    def test2(self):
        '导出生成Excel文件'

        # profile = webdriver.FirefoxProfile()
        # profile.set_preference('browser.download.dir', os.getcwd())
        # profile.set_preference('browser.download.folderList', 2)
        # profile.set_preference('browser.download.manager.showWhenStarting', False)
        # profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'application/x-www-form-urlencoded,application/octet-stream;charset=GB2312;')
        #
        # driver = webdriver.Firefox(firefox_profile=profile)
        # driver.get(url[2])
        # driver.find_element_by_id('userName').send_keys('18017618707')
        # driver.find_element_by_id('pwd').send_keys('123456')
        # driver.find_element_by_id('btnLogin').click()
        #
        # driver.get(url[0] + 'app/entries/' + self.formid)
        # js = "$('#btnExport').click();$('#tabexport').click()"
        # driver.execute_script(js)
        # sleep(2)
        # driver.quit()
        self.driver.get(url[0]+'web/formview/'+self.formid)
        self.driver.find_element_by_id("tmpid").send_keys('tmpid')
        self.driver.find_element_by_id('btnSubmit').click()
        self.download(url)
        self.assertTrue(os.path.exists("表单名称.txt"),'导出生成Excel文件失败')


    def test3(self):
        '通过Excel导入数据'
        js = "$('#btnImport').click();"
        self.driver.execute_script(js)
        sleep(1)
        self.driver.find_element_by_id('fileExcel').send_keys('%s\导入表.xls'% os.getcwd())
        sleep(0.5)
        self.driver.find_element_by_id('btnImportNext').click()
        sleep(0.5)
        self.driver.find_element_by_id('btnImportNext').click()
        sleep(0.5)
        self.driver.find_element_by_id('btnImportNext').click()
        sleep(0.5)
        self.driver.find_element_by_id('btnCancel').click()
        sleep(2)
        self.assertTrue(int(self.driver.find_element_by_xpath('//*[@id="entriesGrid"]/tbody/tr[1]/td[4]').text)-1>0,'通过Excel导入数据失败')

    def test4(self):
        '发送短信'
        js = "$('#btnCreateNew').click()"
        self.driver.execute_script(js)
        self.driver.find_element_by_css_selector('[fmt="mobile"]').send_keys(15671557393)
        self.driver.find_element_by_id('btnSave').click()
        self.driver.find_element_by_xpath('//*[@id="entriesGrid"]/tbody/tr[1]/td[1]').click()
        js = "$('#btnsmssend').click()"
        self.driver.execute_script(js)
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="smsmask"]/div/div/div[2]/div[2]/div[1]/div[1]/div[1]/div').click()
        self.driver.find_element_by_xpath('//*[@id="smsmask"]/div/div/div[2]/div[2]/div[1]/div[1]/div[1]/ul/li[2]').click()
        self.driver.find_element_by_xpath('//*[@id="smsmask"]/div/div/div[2]/div[2]/div[1]/div[2]/div[1]/div/div').click()
        self.driver.find_element_by_xpath('//*[@id="smsmask"]/div/div/div[2]/div[2]/div[1]/div[2]/div[1]/div/ul/li[2]').click()

        #判断占位符是否存在
        num = self.driver.find_element_by_id('smsremain').text
        status = self.driver.find_element_by_xpath('//*[@id="phsrtable"]/..').get_attribute('class')
        if 'hide' in status:
            pass
        else:
            self.driver.find_element_by_xpath('//*[@id="phsrtable"]/tbody/tr/td[2]/div/div').click()
            self.driver.find_element_by_xpath('//*[@id="phsrtable"]/tbody/tr/td[2]/div/ul/li[2]').click()
        self.driver.find_element_by_id('sendsmsbtn').click()
        sleep(1)
        num2 = self.driver.find_element_by_id('smsremain').text
        self.assertTrue(int(num)-int(num2)>0,'发送短信失败')
        self.driver.find_element_by_id('cancelsendsms').click()

    def test5(self):
        '发送邮件'
        js = "$('#btnCreateNew').click()"
        self.driver.execute_script(js)
        self.driver.find_element_by_css_selector('[name="F4"]').send_keys('798337031@qq.com')
        self.driver.find_element_by_id('btnSave').click()
        self.driver.find_element_by_xpath('//*[@id="entriesGrid"]/tbody/tr[1]/td[1]').click()
        js = "$('#btnmailsend').click()"
        self.driver.execute_script(js)
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="mailmask"]/div/div/div[2]/div[1]/label[2]').click()
        num = self.driver.find_element_by_id('mailremain').text
        self.driver.find_element_by_id('senddata-email').send_keys('798337031@qq.com')
        self.driver.find_element_by_id('sendmailbtn').click()
        sleep(1)
        num2 = self.driver.find_element_by_id('mailremain').text
        self.assertTrue(int(num) - int(num2) > 0, '发送邮件失败')
        self.driver.find_element_by_id('cancelsendmail').click()

    def test6(self):
        '批量修改'
        js = "$('#btnCreateNew').click()"
        self.driver.execute_script(js)
        self.driver.find_element_by_id('tmpid').send_keys(1234)
        self.driver.find_element_by_id('btnSave').click()
        self.driver.find_element_by_xpath('//*[@id="entriesGrid"]/tbody/tr[1]/td[1]').click()
        js = "$('#btnBatchEdit').click()"
        self.driver.execute_script(js)
        sleep(1)
        select = Select(self.driver.find_element_by_id('batchEditFld'))
        select.select_by_value("F1")
        self.driver.find_element_by_id('inputText').send_keys('123')
        self.driver.find_element_by_id('btnConfirm').click()
        text = self.driver.find_element_by_xpath('//*[@id="entriesGrid"]/tbody/tr[1]/td[5]').text
        self.assertIn(text,'123','批量修改失败')

    def test7(self):
        '批量删除'
        js = "$('#btnCreateNew').click()"
        self.driver.execute_script(js)
        self.driver.find_element_by_id('tmpid').send_keys(1234)
        self.driver.find_element_by_id('btnSave').click()
        id = self.driver.find_element_by_xpath('//*[@id="entriesGrid"]/tbody/tr[1]/td[4]').text
        self.driver.find_element_by_xpath('//*[@id="entriesGrid"]/tbody/tr[1]/td[1]').click()
        js = "$('#btnDeleteSelected').click()"
        self.driver.execute_script(js)
        sleep(1)
        self.driver.find_element_by_id('txtConfirmYes').send_keys('yes')
        self.driver.find_element_by_css_selector('.btnconfirm.btn.small.right.red').click()
        id2 = self.driver.find_element_by_xpath('//*[@id="entriesGrid"]/tbody/tr[1]/td[4]').text
        self.assertTrue(int(id)-int(id2)>0,'批量删除失败')


    @classmethod
    def tearDownClass(cls):
        cls.driver.get(url[2])
        BasicAction.delete(cls.driver)
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()