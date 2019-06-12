# -*- coding: utf-8 -*-
# @Author  :  'zyx'
# @Email   : 458757014@qq.com
# @File    : operate_mysql.py
# @Software: PyCharm Community Edition

from mysql.connector import connect
from common.filepath import *
from common.read_config import ReadConfig

class OperateMysql:
    def __init__(self):
        #数据库链接配置
        #数据库连接
        db_config = ReadConfig(config_file).read_config('DB_CONFIG','config')
        self.cnn = connect(**eval(db_config))
        #建立游标
        self.cur = self.cnn.cursor()

    def read_mysql(self,sql_sentence):
        #根据输入的sql语句执行SQL
        self.cur.execute(sql_sentence)
        #获取执行SQL后的结果
        result = self.cur.fetchall()
        #关闭游标
        self.cur.close()
        #关闭数据库连接
        self.cnn.close()
        return result

if __name__ == '__main__':
    sql='select max(leaveamount) from  member'
    r = OperateMysql().read_mysql(sql)
    print(r)
