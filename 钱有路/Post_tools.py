import urllib.request as urllib2
import json
import configparser


class MYPost:
    def __init__(self, config_file_path):
        self.path = config_file_path
        self.cf = configparser.ConfigParser()
        self.cf.read('config.ini')

    def get(self, field, key):
        result = ''
        try:
            result = self.cf.get(field, key)
        except Exception as e:
            print(e)
            result = ''
        return result

    def sendjson(url, jdata):
        headers = {'Host': 'www.gtoyg.com',
                   'Connection': 'keep-alive',
                   'Cache-Control': 'no-cache',
                   'Accept': 'application/json, text/javascript, */*; q=0.01',
                   'X-Requested-With': 'XMLHttpRequest',
                   'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; .NET4.0C; .NET4.0E)',
                   'Referer': 'http://www.gtoyg.com/appfrontservice/money/index.html',
                   'Accept-Encoding': 'gzip, deflate',
                   'Accept-Language': 'zh-cn',
                   'Content-Type': 'application/json',
                   }
        maxTryNum = 10
        for tries in range(maxTryNum):
            try:
                jsdata = json.dumps(jdata).encode('UTF8')
                req = urllib2.Request(url, jsdata, headers)
                response = urllib2.urlopen(req, timeout=60)
                result = response.read().decode('UTF8')
                break
            except:
                if (tries < (maxTryNum - 1)):
                    continue
        return result

    def postdata(self, senddata, url):
        sendurl = MYPost.sendjson(url,
                                  senddata)
        dictdata = json.loads(sendurl)
        return dictdata
