# -*- coding: UTF-8 -*-

import linecache
import datetime
import os
from 数据库执行脚本 import Read_DataBase_Tools as Dbtool

cf = Dbtool.get_configparser()
cf.read('config.ini')

try:
    # 打开数据库连接 -- 配置文件
    db = Dbtool.get_db()
    db_mall = Dbtool.get_db_mall()
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    cursor_mall = db_mall.cursor()

    # 删除数据
    mod = 1000
    start = 0
    total = 100000

    # 格式化成2016-03-20 11:45:39形式
    print(datetime.datetime.now(), '>>>>>>>>>>>开始删除数据')
    sql = "Select uid from base.t_user_user WHERE phone in ({0})"
    condition = ''
    for i in range(start, total):
        the_line = linecache.getline(os.path.abspath('.') + '\\' + cf.get('filepath', 'filepath'), i + 1)
        content = the_line.split(',')
        condition = condition + "'{0}',"
        condition = condition.format(content[1])
        if ((i + 1) % mod == 0):
            condition = condition[:-1]
            SelSql = sql.format(condition)
            if cursor.execute(SelSql) > 0:
                # 获取User表
                record = cursor.fetchall()
                delsql = "delete from t_user_user WHERE uid in ({0})"
                dellogsql = "delete from t_user_registry_log WHERE user_id in ({0})"
                delmallsql = "Delete from mall.xx_member WHERE attribute_value9 in ({0})"
                delcondition = ''
                for line in range(0, len(record)):
                    linecont = record[line][0]
                    delcondition = delcondition + "'{0}',"
                    delcondition = delcondition.format(linecont)
                delcondition = delcondition[:-1]
                delsql = delsql.format(delcondition)
                dellogsql = dellogsql.format(delcondition)
                delmallsql = delmallsql.format(delcondition)
                # 执行删除user表
                cursor.execute(delsql)
                # 执行删除user_log表
                cursor.execute(dellogsql)
                # 执行删除mall——member表
                cursor_mall.execute(delmallsql)
            condition = ''
            db.commit()
            db_mall.commit()
            print(datetime.datetime.now(), '执行进度，已完成{0}笔'.format(i + 1))
    print(datetime.datetime.now(), '>>>>>>>>完成，共%d笔' % total)
except Exception as e:
    print('异常')
    print(e)
    # Rollback in case there is any error
#     db.rollback()  # 关闭数据库连接
#     db_mall.rollback()  # 关闭mall数据库连接
# db.close()
