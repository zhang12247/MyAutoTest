# encoding:utf-8

import base64
from Crypto.Cipher import AES
from 数据库执行脚本 import Read_DataBase_Tools as Dbtool
import linecache
import os

cf = Dbtool.get_configparser()
cf.read('config.ini')


class AES_tools:
    def __init__(self):
        self.key = cf.get('key', 'YFBHJ')
        self.mode = AES.MODE_CBC
        self.BS = AES.block_size
        self.pad = lambda s: s + (self.BS - len(s) % self.BS) * chr(self.BS - len(s) % self.BS)
        self.unpad = lambda s: s[0:-ord(s[-1])]
        self.aes_obj = AES.new(self.key, self.mode, self.key)

    def Encrypt_AES(self, text):
        # ciphertext = self.aes_obj.encrypt(self.pad(text))
        self.aes_obj.__init__(self.key, self.mode, self.key)
        ciphertext = self.aes_obj.encrypt(self.pad(text))
        return base64.encodebytes(ciphertext).decode('utf-8')

    def Decrypt_AES(self, Password):
        cryptor=AES.new(self.key, self.mode, self.key)
        plain_text=cryptor.decrypt(base64.b64decode(Password))

        # Password = base64.decodebytes(Password)
        # Password = base64.b64decode(Password)
        # ciphertext = self.aes_obj.decrypt(Password)
        print(type(plain_text))
        return plain_text.rstrip('\0')

    # def Decrypt_AES(self, Password):
    #     Password = Password.encode('utf-8')
    #     Password = base64.decodebytes(Password)
    #     ciphertext = self.aes_obj.decrypt(Password)
    #     return ciphertext


if __name__ == '__main__':
    aa=AES_tools()
    print(aa.Encrypt_AES('13524000510'))
    print(aa.Decrypt_AES('nd7T7+jyhrdukB28KwWAYQ=='))
    # f=open('C:\\数据.txt','a')
    # aa = AES_tools()
    # for i in range(0, 655):
    #     the_line = linecache.getline(os.path.abspath('.') + '\\phone.txt', i + 1)
    #     # content=the_line.split(',')
    #     f.write(aa.Encrypt_AES(the_line.strip('\n')))
    # f.close()
