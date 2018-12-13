# -*- coding: utf-8 -*-
# @Time    : 2018/8/23 0023 09:12
# @Author  : biubiubiu
# @FileName: runner.py
# @Software: PyCharm


from HTMLTestRunner import HTMLTestRunner
import os,unittest


online_url = ['https://www.jsform.com/', 'https://www.bangboss.com/auth/loginx',
              'https://www.jsform.com/app/form/manage', 'https://www.jsform.com/app/entries/getgriddata',
              'https://www.bangboss.com/auth/login?_app=leap-portal',
              {"username": "18017618707", "password": "123456",
               "_cb": "https://www.bangboss.com/app/portal/usercenter/apps", "_app": "leap-portal"}]

test_url = ["http://jsform.tt.com/",'http://portal.t.com/auth/loginx','http://jsform.tt.com/app/form/manage',
            'http://jsform.tt.com/app/entries/getgriddata','http://portal.t.com/auth/login?_app=leap-portal',
            {"username":"18017618707","password":"123456","_cb":"http://jsform.tt.com","_app":"jsform"}]

url = test_url

if __name__ == '__main__':
    # path = os.getcwd()
    # fp = open(path + "/Form.html", "wb")
    # runner = HTMLTestRunner(stream = fp,title = '表单测试报告')
    # discover = unittest.defaultTestLoader.discover('./case', pattern='test_*.py')
    # runner.run(discover)

    # path = os.getcwd()
    # fp = open(path + "/Setting.html", "wb")
    # runner = HTMLTestRunner(stream=fp, title='设置测试报告')
    # discover = unittest.defaultTestLoader.discover('./setting', pattern='*.py')
    # runner.run(discover)

    # path = os.getcwd()
    # fp = open(path + "/Data.html", "wb")
    # runner = HTMLTestRunner(stream=fp, title='数据页测试报告')
    # discover = unittest.defaultTestLoader.discover('./entries', pattern='*.py')
    # runner.run(discover)

    path = os.getcwd()
    fp = open(path + "/Report.html", "wb")
    runner = HTMLTestRunner(stream=fp, title='报表测试报告')
    discover = unittest.defaultTestLoader.discover('./report', pattern='*.py')
    runner.run(discover)

    # path = os.getcwd()
    # fp = open(path + "/TestReport.html", "wb")
    # runner = HTMLTestRunner(stream=fp, title='测试报告')
    # discover = unittest.defaultTestLoader.discover('./', pattern='*.py')
    # runner.run(discover)
