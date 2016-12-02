# -*-coding:utf-8-*-

from  urllib import request
import json
import pymysql
import random
from 身份证号生成工具 import Create_Perinfo_tools
from 加解密工具 import Key_tools


class YkqjAciton():
    def __init__(self):
        self.aes = Key_tools.AES_tools()
        # self.excel = Excel.excel()
        self.url = 'http://192.168.100.215/mall/api'

        #  self.url = 'http://192.168.100.215/mall/api'

    def shuju(self, i):
        id = i
        create_UserName = shenfenzheng.create_UserName()  # 制造名字
        gennerator = shenfenzheng.gennerator()  # 制造身份证
        create_BankCard = shenfenzheng.create_BankCard()  # 制造银行卡
        create_Phone = shenfenzheng.create_Phone()  # 制造手机号码
        phone = create_Phone
        name = create_UserName
        idCard = gennerator  # 身份证号 传加密后信息
        cardNumber = create_BankCard  # 银行卡号 传加密信息
        education = 'E3'  # 教育水平   E1 博士 E2硕士 E3本科 E4大专 E5高职 E6中专 E7高中 E8高中以下
        marrayStatus = 'Y'  # 结婚  Y结婚 N没结婚
        inCome = 'A'  # 收入 A 10000以上 B 8000-10000 C 5000-8000 D 2000-5000 E 2000以下
        job = '6'  # 行业 1 金融 2 房地产 3 服务 4 教育 5 制造 6 文体娱乐 7 交通 8 民生 9科技信息 10 零售 11 建筑 12 其他
        shuju = {'id': id, 'phone': phone, 'name': name, 'idCard': idCard, "cardNumber": cardNumber,
                 'education': education, 'marrayStatus': marrayStatus, 'inCome': inCome, 'job': job}
        print(shuju)
        return shuju

    # 直接运行会

    def insert(self, id, cardNo, userName, userPhone, userCardNo):
        conn = pymysql.connect(host="139.196.242.115", user="base", passwd="base123", db="base", charset='utf8',
                               port=3307)
        cur = conn.cursor()
        sql = "INSERT INTO base.t_bank_simulator VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '1000.00','0000')"
        sql = sql.format(id, cardNo, userName, userPhone, userCardNo)
        print(sql)
        cur.execute(sql)
        conn.commit()
        cur.close()
        conn.close()

    def zhucetoken(self, excelNO, phone):
        url = self.url + self.excel.excelurl(excelNO)
        data = self.excel.cxceldata(excelNO)
        data['phone'] = self.aes.Encrypt_AES(phone)
        headers = {'Content-Type': 'application/json'}
        print(url)
        print(data)
        response = request.post(url, json.dumps(data), headers=headers)
        responseobject = response.json()
        token = responseobject['data']['accessToken']
        uid = responseobject['data']['uid']
        phone = responseobject['data']['phone']
        password = data['password']
        dict = {'token': token, 'uid': uid, 'phone': phone, 'password': password}
        return dict

    def addIdInfo(self, excelNO, uid, name, phone, idcard, token, education=None, marrayStatus=None):
        url = self.url + self.excel.excelurl(excelNO)
        data = self.excel.cxceldata(excelNO)
        if phone:
            data['phone'] = self.aes.Encrypt_AES(phone)
        if uid:
            data['uid'] = uid
        if idcard:
            data['idCard'] = self.aes.Encrypt_AES(idcard)
        if name:
            data['name'] = name
        if education:
            data['education'] = education
        if marrayStatus:
            data['marrayStatus'] = marrayStatus  # http://pan.baidu.com/share/link?shareid=2069073869&uk=2485561099
        print(data)
        headers = {'Content-Type': 'application/json', 'access-token': token}
        response = request.post(url, json.dumps(data), headers=headers)
        responseobject = response.json()
        dict = {'idcard': data['idCard'], 'name': data['name']}
        return dict

    def realName(self, excelNO, uid, bindMobile, cardNumber, token, bankUser, cardName):
        url = self.url + self.excel.excelurl(excelNO)
        data = self.excel.cxceldata(excelNO)
        if bindMobile:
            data['bindMobile'] = self.aes.Encrypt_AES(bindMobile)
        if uid:
            data['uid'] = uid
        if cardNumber:
            data['cardNumber'] = self.aes.Encrypt_AES(cardNumber)
        if bankUser:
            data['bankUser'] = bankUser
        if cardName:
            data['cardName'] = cardName
        print(data)
        headers = {'Content-Type': 'application/json', 'access-token': token}
        response = request.post(url, json.dumps(data), headers=headers)
        responseobject = response.json()
        return responseobject

    def riskWork(self, excelNO, token, uid, inCome=None, job=None):
        url = self.url + self.excel.excelurl(excelNO)
        data = self.excel.cxceldata(excelNO)
        if uid:
            data['uid'] = uid
        if inCome:
            data['inCome'] = inCome
        if job:
            data['job'] = job
        headers = {'Content-Type': 'application/json', 'access-token': token}
        response = request.post(url, json.dumps(data), headers=headers)
        responseobject = response.json()
        return responseobject

    def riskRevice(self, excelNO, token, uid, consignee, phone):
        url = self.url + self.excel.excelurl(excelNO)
        data = self.excel.cxceldata(excelNO)
        if uid:
            data['uid'] = uid
        if consignee:
            data['consignee'] = consignee
        if phone:
            data['phone'] = self.aes.Encrypt_AES(phone)
        data['blackBox'] = 124

        headers = {'Content-Type': 'application/json', 'access-token': token}
        response = requests.post(url, json.dumps(data), headers=headers)
        responseobject = response.json()
        return responseobject

    def queryIdentifyResult(self, excelNO, token):
        url = self.url + self.excel.excelurl(excelNO)
        data = self.excel.cxceldata(excelNO)

        headers = {'Content-Type': 'application/json', 'access-token': token}
        response = request.post(url, json.dumps(data), headers=headers)
        responseobject = response.json()
        print("查询实名结果：" + responseobject)
        return responseobject


if __name__ == "__main__":
    YkqjAciton_ob = YkqjAciton()
    for i in range(80004, 80009):
        if i < 80005:
            shuju = YkqjAciton_ob.shuju(i)
            # shuju = {'phone':phone,'name':name,'idCard':idCard,"cardNumber":cardNumber,'education':education,'marrayStatus':marrayStatus,'inCome':inCome,'job':job}
            #        sql = sql.format(id, cardNo, userName, userPhone, userCardNo)
            YkqjAciton_ob.insert(shuju['id'], shuju['cardNumber'], shuju['name'], shuju['phone'], shuju['idCard'])
            data = YkqjAciton_ob.zhucetoken(22, shuju['phone'])
            addIdInfodata = YkqjAciton_ob.addIdInfo(23, uid=data['uid'], name=shuju['name'], phone=shuju['phone'],
                                                    token=data['token'], idcard=shuju['idCard'],
                                                    education=shuju['education'], marrayStatus=shuju['marrayStatus'])
            realName = YkqjAciton_ob.realName(24, uid=data['uid'], bindMobile=shuju['phone'], token=data['token'],
                                              cardNumber=shuju['cardNumber'], bankUser=shuju['name'], cardName='平安银行')
            riskWork = YkqjAciton_ob.riskWork(25, token=data['token'], uid=data['uid'], job=shuju['job'],
                                              inCome=shuju['inCome'])
            riskRevice = YkqjAciton_ob.riskRevice(26, token=data['token'], uid=data['uid'], consignee=shuju['name'],
                                                  phone=shuju['phone'])
            #   queryIdentifyResult = YkqjAciton_ob.queryIdentifyResult(28,token=data['token'])
            if riskRevice['message'] == '执行成功':
                f1 = open('phone.txt', 'a+')
                f1.write(dict['phone'] + ',' + dict['password'])
                f1.write('\n')
                f1.close()
            else:
                continue

        else:
            break
