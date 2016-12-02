# -*- coding: UTF-8 -*-

import pymysql
import datetime
import linecache
import configparser
import os
from 数据库执行脚本 import Read_DataBase_Tools as Dbtool

cf = Dbtool.get_configparser()
cf.read('config.ini')
try:
    # 打开数据库连接 -- 配置文件
    db = Dbtool.get_db()
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # 生成数据
    mod = 1000
    start = 1000
    total = 80000
    # 格式化成2016-03-20 11:45:39形式
    print(datetime.datetime.now(), '>>>>>>>>>>>开始生成数据')
    for i in range(start, total):
        the_line = linecache.getline(os.path.abspath('.') + '\\' + cf.get('filepath', 'filepath'), i + 1)
        content = the_line.split(',')
        # print(content[3], content[0], content[1], content[2])
        sql = "INSERT INTO base.t_bank_simulator VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '1000.00','0000')"
        sql = sql.format(i, content[3].strip('\n'), content[0], content[1], content[2])
        cursor.execute(sql)
        if ((i + 1) % mod == 0):
            db.commit()
            print(datetime.datetime.now(), '执行进度，已完成{0}笔'.format(i + 1))
    print(datetime.datetime.now(), '>>>>>>>>完成，共%d笔' % total)
except Exception as e:
    print('异常')
    print(e)
    # Rollback in case there is any error
    db.rollback()  # 关闭数据库连接
db.close()
