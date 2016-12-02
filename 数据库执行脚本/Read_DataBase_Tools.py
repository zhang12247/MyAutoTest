# -*- coding: UTF-8 -*-

import pymysql
import configparser


def get_configparser():
    return configparser.ConfigParser()


def get_db():
    cf = get_configparser()
    cf.read('config.ini')
    return pymysql.connect(host=cf.get('db', 'db_host'), user=cf.get('db', 'db_user'), passwd=cf.get('db', 'db_pwd'),
                           db=cf.get('db', 'db_name'), port=cf.getint('db', 'db_port'), charset='utf8')

def get_db_mall():
    cf = get_configparser()
    cf.read('config.ini')
    return pymysql.connect(host=cf.get('db_mall', 'db_host'), user=cf.get('db_mall', 'db_user'), passwd=cf.get('db_mall', 'db_pwd'),
                           db=cf.get('db_mall', 'db_name'), port=cf.getint('db_mall', 'db_port'), charset='utf8')