# -*- coding: UTF-8 -*-

import linecache
import datetime
import os
from 数据库执行脚本 import Read_DataBase_Tools as Dbtool

cf = Dbtool.get_configparser()
cf.read('config.ini')

try:
    mod = 1000
    start = 0
    total = 100000

    for i in range(start, total):
        the_line = linecache.getline(os.path.abspath('.') + '\\' + cf.get('filepath', 'filepath'), i + 1)
        content = the_line.split(',')
        f = open('C:\\phone.txt', 'a')
        f.write(content[1] + '\n')
        f.close()
except Exception as e:
    print('异常')
    print(e)
    f.close()
