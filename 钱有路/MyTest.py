import nose
import linecache
from 钱有路 import Post_tools
from nose.tools import *
import configparser
import os
from nose.core import TestProgram
from 钱有路 import Encrypt_tools
import threading


# 初始化，获取用户Token
def my_setup_function():
    global my_post
    my_post = Post_tools.MYPost(config_file_path='config.ini')
    global url
    url = my_post.get('posturl', 'url')
    global Usertoken
    Usertoken = get_token()


# /appfrontservice/app/token/getToke 获取Token
# @with_setup(my_setup_function)
def get_token():
    appgetToken = my_post.get('posturl', 'appgetToken')
    result = my_post.postdata({'secret': 'nami_token'}, url + appgetToken)
    Token = result['data']['token']
    return Token


@with_setup(my_setup_function)
def test_sendsms():
    appgetSms = my_post.get('posturl', 'appgetSms')
    result = my_post.postdata({'mobile': '13632545698', 'type': 'register'}, url + appgetSms, Usertoken)
    print(result)


# 获取一级目录 所有指标
def test_getDictData():
    for i in ['PROVINCE', 'SALARY', 'EDUCATION', 'CIVIL_STATE', 'P_TRADE']:
        yield getDictData, i


# 实现获取一级目录

def getDictData(codeNo):
    appgetDictData = my_post.get('posturl', 'appgetDictData')
    result = my_post.postdata({'codeNo': codeNo}, url + appgetDictData, Usertoken)
    print(result)


def test_getDictData_hasParentItemNo():
    for i in ['12', '13']:
        yield getDictData_hasParentItemNo, i


def getDictData_hasParentItemNo(parentItemNo):
    appgetDictData_hasParentItemNo = my_post.get('posturl', 'appgetDictData_hasParentItemNo')
    result = my_post.postdata({'codeNo': 'CITY', 'parentItemNo': parentItemNo}, url + appgetDictData_hasParentItemNo,
                              Usertoken)
    print(result)


@nottest
def test_register(phone, deviceid):
    appregister = my_post.get('posturl', 'appregister')
    result = my_post.postdata({'phone': phone, 'loginPassword': Encrypt_tools.actions('112233'),
                               'deviceId': deviceid, 'validateCode': '999999'},
                              url + appregister, Usertoken)
    print(result)


def test_login(phone, deviceid):
    applogin = my_post.get('posturl', 'applogin')
    result = my_post.postdata({'phone': phone, 'loginPassword': Encrypt_tools.actions('112233'),
                               'deviceId': deviceid, 'validateCode': '999999'}, url + applogin,
                              Usertoken)
    print(result)


@nottest
def test_logout():
    applogout = my_post.get('posturl', 'applogout')
    result = my_post.postdata({'uid': '100212114926319956198091474'}, url + applogout, Usertoken)
    print(Usertoken)
    print(result)


def test_queryUserInfo():
    appqueryUserInfo = my_post.get('posturl', 'appqueryUserInfo')
    result = my_post.postdata({'uid': '100212114926319956198091474'}, url + appqueryUserInfo, Usertoken)
    print(Usertoken)
    print(result)


def test_apppreRepayment():
    apppreRepayment = my_post.get('posturl', 'apppreRepayment')
    result = my_post.postdata(
        {'applyid': '1511211474896822613838943', 'phone': '13524000510', 'validateCode': '999999'},
        url + apppreRepayment, Usertoken)
    print(Usertoken)
    print(result)


def test_appdelayRepayment():
    appdelayRepayment = my_post.get('posturl', 'appdelayRepayment')
    result = my_post.postdata(
        {'applyid': '1511211474896822613838943', 'phone': '13524000510', 'validateCode': '999999'},
        url + appdelayRepayment, Usertoken)
    print(Usertoken)
    print(result)


# {"industry":"7","bankCardNo":"6217001210060938000","deviceId":"e9fcb228710f2e1b866693020565441","idcard":"310108198607120857","econtactPhone1":"13262976760","orgName":"田林居委会","blackBox":"eyJvcyI6IkFuZHJvaWQiLCJ2ZXJzaW9uIjoiMi4wLjQiLCJzZXNzaW9uX2lkIjoibmFtaWJhbms0YjNhNmVkOWVmZjFkZTJhYWVkYmQ5YjdkYzhhYmE5ZCIsImRldmljZV9pZCI6InNOeTkzclhxaU9lZlwvY2l0bXY3SnFwT25rXC9MQ3A4T2l3S2FmK3N5cG1LcWRxWjJ1blwvbWRyNWc9IiwiZGF0YSI6InBkQzgwSTdRdHRlN3lLM3pyZlhIbDZMMnhcL0xIOThEd3dQREU4OGFZeHFqZHNkM3huK3FHNnBicWhQR2Q4YVwveHlmXC9KXC84YjF4ZmZIOHNUeHhmSEFuc0N1MjdmYmhkdnEwK0hQXC9zanczdVwvZjc4SHl4dnpFXC9NVDhvdnlIK29iNnN1V2k4TEh2c2ZtczdiclwvdHBiUmc4THZ1XC9mSDk2bjNzT0tqanRxV3BwYklsdDZMeXAzWWtiSDJwT1hJbk5EZzBJN1FtTTJNMjU3WGlkZVF3b091K3JhR3R1aTIzcmVFc29HMDZyVGFyOE92OGErZnJaZW5sNjJkclplbmw2MmRyWmVubCt1WDhzdXR6cXllckpTamtxTEU5cE9pd0x6QThkM3Z3XC9EYzZNVDkwZURRXC9NMzgwT0hSNGRIanpcLzdINjk3eXlwVEsrOHY3cGZ1ZFwvSkRqaGc9PSJ9","econtactName1":"陈锋","orgAddr":"31|3101||咯KKK","econtactPhone2":"13917853641",
# "terminalType":"nami_android","econtactName2":"陈如锦","position":"恐惧","jobState":1,"incomeLv":"A","headUrl":"/appfront/image/2016/11/10/1a0bc4c1-94cc-48e8-9212-b1bc5afb0dcc.jpg","civilState":"N","name":"李根","qq":"172555588","education":"E3","idCardUrl":"/appfront/image/2016/11/10/b7991af2-f644-4f4b-a80e-cc31bb882af8.jpg","bankId":"1479"}

def test_submitUserInfo(deviceid, idcard, bankCardNo, name):
    appsubmitUserInfo = my_post.get('posturl', 'appsubmitUserInfo')
    result = my_post.postdata(
        {'industry': '7', 'bankCardNo': bankCardNo, 'deviceId': deviceid,
         'idcard': idcard, 'econtactPhone1': '13262976760', 'orgName': '田林居委会',
         'blackBox': 'eyJvcyI6IkFuZHJvaWQiLCJ2ZXJzaW9uIjoiMi4wLjQiLCJzZXNzaW9uX2lkIjoibmFtaWJhbms0YjNhNmVkOWVmZjFkZTJhYWVkYmQ5YjdkYzhhYmE5ZCIsImRldmljZV9pZCI6InNOeTkzclhxaU9lZlwvY2l0bXY3SnFwT25rXC9MQ3A4T2l3S2FmK3N5cG1LcWRxWjJ1blwvbWRyNWc9IiwiZGF0YSI6InBkQzgwSTdRdHRlN3lLM3pyZlhIbDZMMnhcL0xIOThEd3dQREU4OGFZeHFqZHNkM3huK3FHNnBicWhQR2Q4YVwveHlmXC9KXC84YjF4ZmZIOHNUeHhmSEFuc0N1MjdmYmhkdnEwK0hQXC9zanczdVwvZjc4SHl4dnpFXC9NVDhvdnlIK29iNnN1V2k4TEh2c2ZtczdiclwvdHBiUmc4THZ1XC9mSDk2bjNzT0tqanRxV3BwYklsdDZMeXAzWWtiSDJwT1hJbk5EZzBJN1FtTTJNMjU3WGlkZVF3b091K3JhR3R1aTIzcmVFc29HMDZyVGFyOE92OGErZnJaZW5sNjJkclplbmw2MmRyWmVubCt1WDhzdXR6cXllckpTamtxTEU5cE9pd0x6QThkM3Z3XC9EYzZNVDkwZURRXC9NMzgwT0hSNGRIanpcLzdINjk3eXlwVEsrOHY3cGZ1ZFwvSkRqaGc9PSJ9',
         'econtactName1': '陈锋', 'orgAddr': '31|3101||咯KKK', 'econtactPhone2': '13917853641',
         'terminalType': 'nami_android', 'econtactName2': '陈如锦', 'position': '恐惧', 'jobState': '1', 'incomeLv': 'A',
         'headUrl': 'namiossqyl20161201164232244000143.jpg', 'civilState': 'N',
         'name': name, 'qq': '172555588', 'education': 'E3',
         'idCardUrl': 'namiossqyl20161201164151458000547.jpg', 'bankId': '1474'},
        url + appsubmitUserInfo, Usertoken)
    print(Usertoken)
    print(result)


def test_appconfirmApply4App(deviceid):
    appconfirmApply4App = my_post.get('posturl', 'appconfirmApply4App')
    result = my_post.postdata(
        {'applyAmount': '1000', 'periods': '1', 'deviceId': deviceid,
         'applyCity': '上海'},
        url + appconfirmApply4App, Usertoken)
    print(result)


if __name__ == '__main__':
    for i in range(1001, 1100):
        the_line = linecache.getline(os.path.abspath('.') + '\\10W_data.txt', i + 1)
        content = the_line.split(',')
        my_setup_function()
        deviceid = 'fffe249e81d29fc3a0000055ec' + str(i)
        test_register(phone=content[1], deviceid=deviceid)
        test_login(phone=content[1], deviceid=deviceid)
        # test_submitUserInfo(deviceid=deviceid, idcard=content[2],
        #                     bankCardNo=content[3].strip('\n'), name=content[0])
        test_appconfirmApply4App(deviceid=deviceid)
