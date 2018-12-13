# -*- coding: utf-8 -*-
# @Time    : 2018/8/27 0027 16:12
# @Author  : biubiubiu
# @FileName: basicaction.py
# @Software: PyCharm


from time import sleep
import os

class BasicAction:

    '''
    基础操作
    '''


    @staticmethod
    def delete(driver):
        try:
            driver.find_element_by_css_selector(".btnconfirm.btn.small.right.blue").click()
        except Exception:
            pass
        a = 0
        lists = len(driver.find_elements_by_css_selector("#groupList li.listItem"))
        while a < lists:
            js = "$('.del').eq(0).click();$('#txtConfirmYes').val('yes');$('.btnconfirm.btn.small.right.red').click();"
            driver.execute_script(js)
            sleep(2)
            a += 1

    @staticmethod
    def preview(driver):
        driver.switch_to_default_content()
        driver.find_element_by_css_selector('.btn.blue.save').click()
        sleep(1)
        driver.find_element_by_css_selector('.btn.blue.preview').click()
        sleep(2)
        driver.switch_to.window(driver.window_handles[1])
        formid = driver.current_url.split('/')[-1]
        return formid

    @staticmethod
    def clear(driver):
        '清除所有已选项'
        js = '$("input[type=checkbox]").attr("checked",false);'
        driver.execute_script(js)

    @staticmethod
    def view(driver,formid,url):
        '查看表单'
        driver.switch_to_default_content()
        driver.find_element_by_xpath('//*[@id="topActions"]/div[3]/a[2]').click()
        driver.get(url[0] + 'web/formview/' + formid)

    @staticmethod
    def search(driver):
        '查看查询'
        url = driver.find_element_by_id('txtPubDataUrl').get_attribute('value')
        driver.switch_to_default_content()
        driver.find_element_by_xpath('//*[@id="topActions"]/div[3]/a[2]').click()
        driver.get(url)

    @staticmethod
    def SaveReport(driver):
        driver.find_element_by_id('saveReport').click()
        sleep(1)
        driver.find_element_by_id('hdControls').click()
        sleep(1)
        driver.switch_to.window(driver.window_handles[1])
        return