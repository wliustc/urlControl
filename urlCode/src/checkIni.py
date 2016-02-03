# -*- coding:utf-8 -*-

from iniUtil import IniUtil
import re
import os

class Check:

    def __init__(self):
        self.falseUrl = []
        self.nowPath = os.getcwd()
        self.iniPath = self.nowPath + '/../config/url.ini'

    def checkIniUrl(self):
        iniObj = IniUtil(self.iniPath)
        keys = iniObj.getKeysBySection('url')
        for key in keys:
            url = iniObj.getValue('url',key)
            if self.checkUrl(url) == False:
                self.falseUrl.append(url)
        return self.falseUrl

    #校验URL合理
    def checkUrl(self,url):
        regex = re.compile(
        r'^(?:http)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
        result = re.match(regex, url) != None
        return result

    #校验key不重复
    def checkIniKeys(self):
        listKey = []
        file = open(self.iniPath)
        while 1:
            line = file.readline()
            if not line:
                break
            else:
                key = line.split("=")[0].strip()
                if key.__contains__('[') == False:
                    listKey.append(key)
        return self.checkKey(listKey)

    def checkKey(self,listKey):
        resultKey = []
        for key in listKey:
            num = 0
            for keyTmp in listKey:
                if key == keyTmp:
                    num += 1
            if num > 1:
                resultKey.append(key)
        return resultKey
'''
check = Check()
a = check.checkIniKeys()
f=file("hello.txt","w+")
f.write('重复的key：：')
for b in a:
    f.write(b)
f.close()
'''