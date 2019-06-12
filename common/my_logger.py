# -*- coding: utf-8 -*-
# @Author  :  'zyx'
# @Email   : 458757014@qq.com
# @File    : my_logger.py
# @Software: PyCharm Community Edition
import logging
import time
from logging.handlers import RotatingFileHandler
from common.filepath import log_path

class Logger:
    def logger(self,filename):
        #指定日志的输出格式(日志时间，日志级别，文件名，function名，当前日志的行号，日志信息)
        fmt = " %(asctime)s  %(levelname)s %(filename)s %(funcName)s [ line:%(lineno)d ] %(message)s"
        #日期格式化：星期名称，月，天，年  时：分：秒
        datefmt =  '%a, %d %b %Y %H:%M:%S'

        #指定输出渠道
        handler_1 = logging.StreamHandler() #输出到控制台

        curTime=time.strftime('%Y-%m-%d %H%M%S',time.localtime())
        handler_2 = RotatingFileHandler(filename+'/test_{0}.log'.format(curTime),encoding='utf-8')  #输出到文件

        #设置输出形式和输出渠道
        logging.basicConfig(format=fmt,datefmt=datefmt,level=logging.INFO,handlers=[handler_1,handler_2])
        return logging


logger = Logger().logger(log_path)