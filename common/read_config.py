# -*- coding: utf-8 -*-
# @Author  :  'zyx'
# @Email   : 458757014@qq.com
# @File    : read_config.py
# @Software: PyCharm Community Edition

from configparser import ConfigParser
from common.filepath import *

class ReadConfig:
    def __init__(self,filename):
        self.filename=filename

    def read_config(self,section,option):
        config = ConfigParser()
        config.read(self.filename,encoding='UTF-8')
        value = config.get(section,option)
        return value


if __name__ == '__main__':
    # a=ReadConfig(config_path+r'\config.ini')
    # v=a.read_config('DB_CONFIG','config')
    # print(v)

    a=ReadConfig(config_path+r'\config.ini')
    v=a.read_config('URI','uri')
    print(v)