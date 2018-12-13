#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@version: 1.0.0
@author: Administrator
@license: Apache Licence
@software: PyCharm
@file: property.py
@time: 2018/7/27 0027 10:38
"""
from time import sleep
import os

class SettingOptUtils:

    '''
    设置工具类
    '''


    @staticmethod
    def element_name(driver):  # 修改组件名称的方法

        driver.find_element_by_id('lbl').clear()
        driver.find_element_by_id('lbl').send_keys('组件改名')
        sleep(1)
        

    @staticmethod
    def element_format(driver, id):  # 修改所有设置为下拉菜单的
           
        js = '$("#' + id + '").next().find(".dk-select-options li").eq(1).click()'
        driver.execute_script(js)
         

    @staticmethod
    def popt_required(driver):  # 必填项
           
        driver.find_element_by_css_selector('[for="reqd"]').click()
         

    @staticmethod
    def popt_unique(driver):  # 不许重复
           
        driver.find_element_by_css_selector('[for="uniq"]').click()
         

    @staticmethod
    def popt_editable(driver):  # 不可编辑
           
        driver.find_element_by_xpath('//*[@id="popt_editable"]/label').click()
         

    @staticmethod
    def popt_qrinput(driver):  # 扫码输入
           
        driver.find_element_by_css_selector('[for="qrinput"]').click()
         

    @staticmethod
    def sec_pub(driver):  # 每个人可见
           
        driver.find_element_by_css_selector('[for="sec_pub"]').click()
         

    @staticmethod
    def sec_pri(driver):  # 仅登陆可见
           
        driver.find_element_by_css_selector('[for="sec_pri"]').click()
         

    @staticmethod
    def range(driver):  # 最大值最小值
           
        driver.find_element_by_id("min").send_keys("1")
        driver.find_element_by_id("max").send_keys("10")  # 都是1-10


    @staticmethod
    def daterange(driver):  # 日期最大值最小值
           
        driver.find_element_by_id('dtmin').send_keys('2018-08-01')
        driver.find_element_by_id('dtmax').send_keys('2018-08-31')


    @staticmethod
    def defval_text(driver, id, text):  # 默认值
           
        driver.find_element_by_id(id).send_keys(text)
         

    @staticmethod
    def instruct(driver):  # 字段说明
        driver.find_element_by_id('instruct').clear()
        driver.find_element_by_id('instruct').send_keys('字段说明')
        sleep(1)

         

    @staticmethod
    def css(driver):  # css格式
        driver.find_element_by_xpath('//*[@id="topActions"]/div[2]/span[4]/span').click()
        driver.find_element_by_id('pbody').click()
        driver.find_element_by_xpath('//*[@id="advCssContainer"]/span[3]').click()
        driver.find_element_by_id('advanceCss').send_keys('[class=desc]{color:red;}')
        driver.find_element_by_xpath('//*[@id="topActions"]/div[2]/span[2]/span').click()
        js = "$('#css').val('[class=desc]').change()"
        driver.execute_script(js)


    @staticmethod
    def pitems_radio(driver):  # 对单选框做一些基础设置
           
        # driver.find_element_by_css_selector("[for='isPhotoItem']").click() #图片
        driver.find_element_by_id("btnItemsPredefine").click()  # 批量编辑（）
        driver.find_element_by_xpath("//*[@id='choiceMenu']/li[1]/a").click()  # 选了男女
        driver.find_element_by_xpath("//*[@id='btnConfirm']").click()
        # driver.find_element_by_css_selector('[class="item-upload"]').send_keys("D:\\pypicture\\1.jpg") #传图片   这个还未实现！！！！！！！！！！！！！！！！！！！！！！！！！
        sleep(1)
        driver.find_element_by_xpath("//*[@id='itemList']/li[1]/label").click()  # 选一个默认值默认为第一个
        # 加一个选项 改为男男 删一个选项
        js = "$('.icononly-add').eq(0).click();$('.sl').eq(1).val('男男').change().keyup();$('.icononly-del').eq(2).click()"
        driver.execute_script(js)
        driver.find_element_by_xpath('//*[@id="itemList"]/li[2]/a[4]').click()
        driver.find_element_by_xpath('//*[@id="lmt1"]/input').send_keys(1)  # 每天提交数为1
         

    @staticmethod
    def random(driver):  # 单选框的随机
           
        driver.find_element_by_css_selector('[for="random"]').click()


    @staticmethod
    def allowOther(driver):  # 单选框允许其他值

        driver.find_element_by_css_selector('[for="allowOther"]').click()
         

    @staticmethod
    def pitems_checkboxes(driver):  # 对多选框做一些基础设置
           
        # driver.find_element_by_css_selector("[for='isPhotoItem']").click() #图片
        driver.find_element_by_id("btnItemsBatch").click()  # 批量编辑（）
        driver.find_element_by_id('prepop').clear()
        driver.find_element_by_id('prepop').send_keys('男\n女')  # 选了男女
        driver.find_element_by_xpath("//*[@id='btnConfirm']").click()
        # driver.find_element_by_css_selector('[class="item-upload"]').send_keys("D:\\pypicture\\1.jpg") #传图片   这个还未实现！！！！！！！！！！！！！！！！！！！！！！！！！
        sleep(1)
        driver.find_element_by_xpath("//*[@id='itemList']/li[1]/label").click()  # 选一个默认值默认为第一个
        # 加一个选项 改为男男 删一个选项
        js = "$('.icononly-add').eq(0).click();$('.sl').eq(1).val('男男').change().keyup();$('.icononly-del').eq(2).click()"
        driver.execute_script(js)
        driver.find_element_by_xpath('//*[@id="itemList"]/li[2]/a[4]').click()
        driver.find_element_by_xpath('//*[@id="lmt1"]/input').send_keys(1)  # 每天提交数为1
         

    @staticmethod
    def dd2(driver):  # 修改多级下拉的层级
        driver.find_element_by_id('btnItemsBatch').click()
        sleep(1)
        js = "$('.icon-bianji1.edit').eq(0).click();$('.update').eq(0).val('男男').change();$('.icon-bianji1.edit').eq(2).click();$('.update').eq(2).val('男男').change()"
        driver.execute_script(js)
        driver.find_element_by_id('btnConfirm').click()
        driver.find_element_by_css_selector('[for="itemList_0"]').click()  # 选一个默认值默认为第一个
         

    @staticmethod
    def lk(driver):   # 修改组合单选的各种设置
           
        js = "$('.xl').eq(0).val('第一行').keyup();$('.icononly-add').eq(0).click();$('.icononly-del').eq(3).click();$('.icononly-del').eq(2).click();"  # 增一个标签，减两个标签，把标签的名字改为第一行
        driver.execute_script(js)
        driver.find_element_by_id('btnLikertPredefine').click()
        driver.find_element_by_xpath('//*[@id="choiceMenu"]/li[1]/a').click()
        driver.find_element_by_id('btnConfirm').click()
        js = "$('.icononly-add').eq(2).click();$('.icononly-del').eq(3).click();$('.icononly-del').eq(2).click();"  # 增一个列标签，减两个列标签
        driver.execute_script(js)
        driver.find_element_by_xpath('//*[@id="popt_hidenum"]/label').click()  # 组合单选中有个隐藏数字的选项
        driver.find_element_by_xpath('//*[@id="likertCols"]/li[1]/label').click()
         

    @staticmethod
    def wangEditor_txt(driver, id):  # 设置分隔符和描述文字的本文
           
        js = "$('#" + id + "').val('测试').keyup()"
        driver.execute_script(js)
         

    @staticmethod
    def pmaxsize(driver):  # 设置文件最大和数量
           
        driver.find_element_by_xpath("//*[@id='maxsize']").send_keys("1")
        driver.find_element_by_xpath("//*[@id='numsize']").send_keys("1")


    @staticmethod
    def hidenum(driver):  # 隐藏数字

        driver.find_element_by_css_selector('[for="hidenum"]').click()

    @staticmethod
    def uploadImage(driver):  # 上传图片展示图片
           
        driver.find_element_by_xpath("//*[@id='uploadImage']").send_keys('%s\\2.jpg'%os.getcwd())
        sleep(1)
         

    @staticmethod
    def pvedio(driver):  # 设置视频展示视频
           
        js = 'document.getElementById("pvdsrc").value="https://imgcache.qq.com/tencentvideo_v1/playerv3/TPout.swf?max_age=86400&v=20161117&vid=b0664ucwaca&auto=0";$("#pvdsrc").change()'
        driver.execute_script(js)
         

    @staticmethod
    def internal(driver):  # 手机的启动国际手机
           
        driver.find_element_by_css_selector('[for="internal"]').click()

    @staticmethod
    def authcode(driver):  # 手机验证码

        driver.find_element_by_css_selector('[for="authcode"]').click()

    @staticmethod
    def detail(driver):  # 设置地址的隐藏详细地址
           
        driver.find_element_by_xpath("//*[@id='popt_detail']/label").click()


    @staticmethod
    def pdefval_addr(driver):  # 设置地址默认值

        driver.find_element_by_xpath("//*[@id='pdefval_addr']/div[1]/div").click()
        driver.find_element_by_xpath("//*[@id='pdefval_addr']/div[1]/ul/li[2]").click()  # 北京市
        driver.find_element_by_xpath("//*[@id='pdefval_addr']/div[2]/div").click()
        driver.find_element_by_xpath("//*[@id='pdefval_addr']/div[2]/ul/li[2]").click()  # 北京市
        driver.find_element_by_xpath("//*[@id='pdefval_addr']/div[3]/div").click()
        driver.find_element_by_xpath("//*[@id='pdefval_addr']/div[3]/ul/li[2]").click()  # 朝阳区


    @staticmethod
    def pgoods(driver):  # 商品的设置
        driver.find_element_by_css_selector('[value="商品名称"]').send_keys("测试商品")
        driver.find_element_by_name("PRC").send_keys("2")
        driver.find_element_by_name("UNT").send_keys("个")
        driver.find_element_by_name("DEF").send_keys("2")
        driver.find_element_by_name("AMOUNTLMT").send_keys("40")
        driver.find_element_by_id('goodsItemDes').send_keys('测试商品描述')


    @staticmethod
    def grade(driver):  # 评分设置10星
           
        driver.find_element_by_css_selector('[for="start_length_10"]').click()
         

