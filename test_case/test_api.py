# -*- coding: utf-8 -*-
# @Author  :  'zyx'
# @Email   : 458757014@qq.com
# @File    : test_api.py
# @Software: PyCharm Community Edition

import unittest
from ddt import ddt,data
from common.my_logger import logger
from common.filepath import *
from common.read_config import ReadConfig
from common.operate_excel import OperateExcel
from common.http_request import HttpRequests

excel_obj=OperateExcel(data_path+r'\test_datas.xlsx','test_data')
test_datas=excel_obj.read_data()
uri = ReadConfig(config_path+r'\config.ini').read_config('URI','uri')

COOKIES={}#未进行登陆之前，cookie值是未知的，而且每一次登录成功时都会产生一个cookie

@ddt
class TestApi(unittest.TestCase):
    @data(*test_datas)
    def test_api(self,args):

        global COOKIES#声明全局变量

        logger.info('正在执行第{0}条用例'.format(args['case_id']))
        logger.info('测试参数：{0}'.format(args))
        url = uri+args['apiName']
        #发起HTTP请求
        res = HttpRequests().http_request(url,args['method'],eval(args['param']),COOKIES)
        logger.info('返回结果：{0}'.format(res.json()))
        logger.info(type(args['case_id']))
        logger.info(COOKIES)
        #每一个登录请求之后都会产生一个cookies
        if res.cookies!={}:
            COOKIES=res.cookies#如果cookies不为空，就对全局变量进行修改

        #断言，比对结果
        try:
            self.assertEqual(eval(res.json()['code']),args['expected'])
            test_result='pass'
        except Exception as e:
            logger.exception('断言出错啦，期望结果为：{0}，实际结果为：{1}'.format(args['expected'],res.json()['code']))
            test_result='fail'
            raise e
        finally:
            excel_obj.write_back(args['case_id']+1,8,res.text)
            excel_obj.write_back(args['case_id']+1,9,test_result)
