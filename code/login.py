# -*- coding: utf-8 -*-
# @Time    : 2018/8/22 0022 16:41
# @Author  : biubiubiu
# @FileName: login.py.py
# @Software: PyCharm


from selenium import webdriver
from runner import url

class Login():

    def __init__(self):
        self.driver = webdriver.Firefox()
        self.username = 18017618707
        self.password = 123456

    def login_page(self):
        self.driver.get(url[4])

    def login_action(self):
        self.driver.find_element_by_id('userName').send_keys(self.username)
        self.driver.find_element_by_id('pwd').send_keys(self.password)
        self.driver.find_element_by_id('btnLogin').click()

    def login(self):
        self.login_page()
        self.login_action()


