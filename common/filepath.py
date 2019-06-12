# -*- coding: utf-8 -*-
# @Author  :  'zyx'
# @Email   : 458757014@qq.com
# @File    : filepath.py
# @Software: PyCharm Community Edition

import os

#项目根目录
#pro_path = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]
pro_path = os.path.dirname((os.path.dirname(os.path.abspath(__file__))))
print(pro_path)
#配置文件目录
config_path = os.path.join(pro_path,'config')
config_file = os.path.join(config_path,'config.ini')
#测试数据目录
data_path = os.path.join(pro_path,'test_data')
#print(data_path)
#日志目录
log_path = os.path.join(pro_path,'log')
#测试报告目录
report_path = os.path.join(pro_path,'test_report')
#公共文件目录
common_path = os.path.join(pro_path,'common')
#测试用例目录
case_path = os.path.join(pro_path,'test_case')