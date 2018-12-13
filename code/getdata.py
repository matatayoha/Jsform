# -*- coding: utf-8 -*-
# @Time    : 2018/7/30 0030 17:28
# @Author  : biubiubiu
# @FileName: data.py
# @Software: PyCharm


import random
from time import sleep
from selenium.webdriver.support.ui import Select
import requests
from http.cookiejar import CookieJar
import json
import os


class DataUtils:
    '''
    对数据页面上的操作和校验
    '''

    # @staticmethod# 添加一条新数据
    # def verifyCreateNew(driver, content):
    #     try:
    #         driver.find_element_by_id('btnCreateNew').click()  # 添加一条新数据
    #         text = random.randint(0, 1000)  # 用随机数添加，确保
    #         driver.find_element_by_id('tmpid').send_keys(text)
    #         driver.find_element_by_id('btnSave').click()
    #         sleep(1)
    #         number = driver.find_element_by_xpath('//*[@id="entriesGrid"]/tbody/tr[1]/td[5]').text
    #         assertfunc(number,str(text),'新增一条数据', content)
    #
    #     except Exception as e:
    #         logger.exception(e)
    #         pass
    #
    # # 导出生成excel  太麻烦了先不写
    #
    # @staticmethod# 导入Excel数据
    # def verifyImport(driver,content):
    #     try:
    #         ID = driver.find_element_by_xpath('//*[@id="entriesGrid"]/tbody/tr[1]/td[4]').text
    #         driver.find_element_by_id('btnImport').click()
    #         driver.find_element_by_id('fileExcel').send_keys('%s\自动测试数据相关-不可删除.xls'%os.getcwd())
    #         sleep(1)
    #         driver.find_element_by_id('btnImportNext').click()
    #         sleep(1)
    #         driver.find_element_by_id('btnImportNext').click()
    #         sleep(1)
    #         driver.find_element_by_id('btnImportNext').click()
    #         sleep(1)
    #         driver.find_element_by_id('btnCancel').click()
    #         sleep(1)
    #         IDafter = driver.find_element_by_xpath('//*[@id="entriesGrid"]/tbody/tr[1]/td[4]').text
    #         if IDafter > ID:
    #             result = {'title': '导入Excel数据', 'result': 'Pass'}
    #             content.append(result)
    #             logger.info('导入Excel数据成功\n')
    #         else:
    #             result = {'title': '导入Excel数据', 'result': 'Fail'}
    #             content.append(result)
    #             logger.warning('导入Excel数据失败\n')
    #     except Exception as e:
    #         logger.exception(e)
    #         pass
    #
    # @staticmethod    # 复制数据
    # def verifyActDup(driver,content):
    #     try:
    #         ID = driver.find_element_by_xpath('//*[@id="entriesGrid"]/tbody/tr[1]/td[4]').text
    #         driver.find_element_by_xpath('/html/body/div[2]/div[3]/div[2]/div/table/tbody/tr[1]/td[1]').click()
    #         driver.find_element_by_id('btnActDup').click()
    #         IDafter = driver.find_element_by_xpath('//*[@id="entriesGrid"]/tbody/tr[1]/td[4]').text
    #         if IDafter > ID:
    #             result = {'title': '复制数据', 'result': 'Pass'}
    #             content.append(result)
    #             logger.info('复制数据成功\n')
    #         else:
    #             result = {'title': '复制数据', 'result': 'Fail'}
    #             content.append(result)
    #             logger.warning('复制数据失败\n')
    #     except Exception as e:
    #         logger.exception(e)
    #         pass
    #
    # @staticmethod    # 批量修改
    # def verifyBatchEdit(driver,content):
    #     try:
    #         driver.find_element_by_xpath('/html/body/div[2]/div[3]/div[2]/div/table/tbody/tr[1]/td[1]').click()
    #         driver.find_element_by_id('btnBatchEdit').click()
    #         select = Select(driver.find_element_by_id('batchEditFld'))
    #         select.select_by_value("F1")
    #         driver.find_element_by_id('inputNumber').send_keys('123')
    #         driver.find_element_by_id('btnConfirm').click()
    #         text = driver.find_element_by_xpath('//*[@id="entriesGrid"]/tbody/tr[1]/td[5]').text
    #         assertfunc('3', text, '批量修改', content)
    #
    #     except Exception as e:
    #         logger.exception(e)
    #         pass
    #
    #
    # @staticmethod    # 批量删除
    # def verifyDeleteSelected(driver,content):
    #     try:
    #         ID = driver.find_element_by_xpath('//*[@id="entriesGrid"]/tbody/tr[1]/td[4]').text
    #         driver.find_element_by_xpath('/html/body/div[2]/div[3]/div[2]/div/table/tbody/tr[1]/td[1]').click()
    #         driver.find_element_by_id('btnDeleteSelected').click()
    #         driver.find_element_by_id('txtConfirmYes').send_keys('yes')
    #         driver.find_element_by_css_selector('[class="btnconfirm btn small right red"]').click()
    #         IDafter = driver.find_element_by_xpath('//*[@id="entriesGrid"]/tbody/tr[1]/td[5]').text
    #         if IDafter != ID:
    #             result = {'title': '批量删除', 'result': 'Pass'}
    #             content.append(result)
    #             logger.info('批量删除成功\n')
    #         else:
    #             result = {'title': '批量删除', 'result': 'Fail'}
    #             content.append(result)
    #             logger.warning('批量删除失败\n')
    #     except Exception as e:
    #         logger.exception(e)
    #         pass
    #
    # @staticmethod    # 数据查看
    # def verifiyview(driver,content):
    #     try:
    #         driver.find_element_by_xpath('//*[@id="entriesGrid"]/tbody/tr[1]/td[3]/span/a[1]').click()
    #         driver.find_element_by_id('commentBody').send_keys('评论测试')
    #         driver.find_element_by_id('btnSaveComment').click()
    #
    #         if driver.find_element_by_css_selector('[title="删除此评论"]'):
    #             result = {'title': '数据查看', 'result': 'Pass'}
    #             content.append(result)
    #             logger.info('数据查看成功\n')
    #         else:
    #             result = {'title': '数据查看', 'result': 'Fail'}
    #             content.append(result)
    #             logger.warning('数据查看失败\n')
    #         driver.find_element_by_css_selector('[class="iconfont close"]').click()
    #     except Exception as e:
    #         logger.exception(e)
    #         pass
    #
    # @staticmethod    # 标星
    # def verifyasterisk(driver,content):
    #     try:
    #         driver.find_element_by_xpath('//*[@id="entriesGrid"]/tbody/tr[1]/td[3]/span/a[4]').click()
    #         text = driver.find_element_by_xpath('//*[@id="entriesGrid"]/tbody/tr[1]/td[3]/span/a[3]').get_attribute(
    #             'class')
    #         if 'hide' not in text:
    #             result = {'title': '标星', 'result': 'Pass'}
    #             content.append(result)
    #             logger.info('标星成功\n')
    #         else:
    #             result = {'title': '标星', 'result': 'Fail'}
    #             content.append(result)
    #             logger.warning('标星失败\n')
    #     except Exception as e:
    #         logger.exception(e)
    #         pass
    #
    # @staticmethod    # 标记为已处理
    # def verifyprocessed(driver,content):
    #     try:
    #         driver.find_element_by_xpath('//*[@id="entriesGrid"]/tbody/tr[1]/td[3]/span/a[6]').click()
    #         text = driver.find_element_by_xpath('//*[@id="entriesGrid"]/tbody/tr[1]/td[3]/span/a[5]').get_attribute(
    #             'class')
    #         if 'hide' not in text:
    #             result = {'title': '已处理', 'result': 'Pass'}
    #             content.append(result)
    #             logger.info('已处理成功\n')
    #         else:
    #             result = {'title': '已处理', 'result': 'Fail'}
    #             content.append(result)
    #             logger.warning('已处理失败\n')
    #     except Exception as e:
    #         logger.exception(e)
    #         pass

    @staticmethod   #用爬虫的方法去抓数据页面的值
    def verify_data(url,formid):
        requests.packages.urllib3.disable_warnings()
        session = requests.session()  # 保持会话
        session.cookies = CookieJar()  # 设置存cookie的地方   这里能接受setcookie中的cookie
        # Headers信息
        head = {
            'Connection': 'keep-alive',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
            'Content-Type': 'application/json; charset=UTF-8'
        }

        # 登陆Form_Data信息获得门户里面的cookies存在session.cookies中
        session.post(url[1], data=json.dumps(url[5]), headers=head, verify=False)
        # 登陆Form_Data信息获得表单大师里面的cookies存在session.cookies中
        session.get(url[2], cookies=session.cookies, headers=head, verify=False)
        data = {"FRMID":str(formid),"MCHTYP":"and","CONS":[],"SORT":[{"ID":"-1"}],"PAGESIZE":1000,
                "PAGEINFO":{"FIRST":{},"LAST":{}}}
        a = session.post(url[3], cookies=session.cookies, headers=head, data=json.dumps(data), verify=False)
        # print(a.text)
        result = json.loads(a.text)
        alldata = result.get('rows')[0]  # 拿到所有提交的数据
        return alldata



