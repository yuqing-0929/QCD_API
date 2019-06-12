# -*- coding: utf-8 -*-
# @Author  :  'zyx'
# @Email   : 458757014@qq.com
# @File    : run.py
# @Software: PyCharm Community Edition

import unittest
import time
from HTMLTestRunnerNew import HTMLTestRunner
from common.filepath import *
from test_case.test_api import TestApi

suite = unittest.TestSuite()
t = unittest.TestLoader()

suite.addTest(t.loadTestsFromTestCase(TestApi))

report_file = report_path + '/report_{0}.html'.format(time.strftime("%Y%m%d_%H%M%S"))
with open(report_file,'wb+') as file:
    runner = HTMLTestRunner(file,
                            title='API Test Report for QCD',
                            description='测试结果：',
                            tester='Crystal')
    runner.run(suite)