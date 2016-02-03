# -*- coding:utf-8 -*-
import urllib2
from iniUtil import IniUtil
from cookieUtil import CookieUtil
from codeUtil import CodeUtil
from checkIni import Check
from logUtil import LogUtil
from creatHtml import CreateHtml
from exceiUtil import ExcelUtil
from labelUtil import LabelUtil
import time
import os

class RunCode:

    def __init__(self):
        self.cookieObj = CookieUtil()
        self.nowTile = time.strftime('%Y%m%d%H%M%S')
        self.nowPath = os.getcwd()
        if os.path.exists(self.nowPath + "/../log") == False:
            os.mkdir(self.nowPath + "/../log")
        if os.path.exists(self.nowPath + "/../result") == False:
            os.mkdir(self.nowPath + "/../result")
        self.resultIniPath = self.nowPath + "/../log/result_"+ self.nowTile+".ini"
        self.errorLogPath = self.nowPath + "/../log/result_"+ self.nowTile+"_error.ini"
        self.htmlPath = self.nowPath + "/../result/result_"+ self.nowTile+".html"
        self.check = Check()
        self.logUtil = LogUtil()

    def run(self):
        checkKeyResult = self.check.checkIniKeys()
        #key重复性校验失败
        if checkKeyResult:
            self.logUtil.setKeyLog(self.errorLogPath,checkKeyResult)
        #校验成功
        else:
            checkUrlResult = self.check.checkIniUrl()
            #url合法性校验失败
            if checkUrlResult:
                self.logUtil.setUrlLog(self.errorLogPath,checkUrlResult)
            #校验成功
            else:
                self.iniObj = IniUtil(self.nowPath + '/../config/url.ini')
                self.iniObjResult = IniUtil(self.resultIniPath)
                cookie = self.getCookie()
                #解析内容
                self.getContent(cookie)
                #self.doPost(cookie)
                #self.setCode()
                #self.setHtml()
        print '执行完毕！！'

    def getCookie(self):
        cookie = self.cookieObj.getLoginCookie()
        return cookie

    def getContent(self,cookie):
        #获取配置文件的url
        keysList = []
        urlDict = {}
        keysList = self.iniObj.getKeysBySection('url')
        num = 1
        excelUtilObj = ExcelUtil()
        for key in keysList:
            url = self.iniObj.getValue('url',key)
            urlDict.setdefault(key,url)
            try:
                #创建请求的request
                req = urllib2.Request(url)
                handler = urllib2.HTTPCookieProcessor(cookie)
                #利用urllib2的build_opener方法创建一个opener
                openner = urllib2.build_opener(handler)
                response = openner.open(req)

                content = response.read()
                htmlLabel = excelUtilObj.htmlLabel
                worksheet = excelUtilObj.addSheet(key)
                excelUtilObj.setKeys(worksheet)
                self.setExcel(worksheet,num,excelUtilObj,content,htmlLabel)
                num += 1
            except urllib2.URLError,e:
                reason = e.reason
                pageCode = u'状态码:' + str(e.code) + u';错误原因:' + reason
                self.logUtil.setPostErrorLog(self.errorLogPath,url,pageCode)
        excelUtilObj.closeExcel()

    def setExcel(self,worksheet,num,excelUtilObj,content,htmlLabel):
        labelUtil = LabelUtil(content)
        title = labelUtil.getTitle()
        keywords = labelUtil.getKeywords()
        description = labelUtil.getDescription()
        if htmlLabel.__contains__('title'):
            excelUtilObj.setValue(worksheet,num,'title',title)
        if htmlLabel.__contains__('keywords'):
            excelUtilObj.setValue(worksheet,num,'keywords',keywords)
        if htmlLabel.__contains__('description'):
            excelUtilObj.setValue(worksheet,num,'description',description)
        '''
        a = labelUtil.getLabel_a()
        h1 = labelUtil.getLabel_h1()
        h2 = labelUtil.getLabel_h2()
        '''

    def doPost(self,cookie):
        #获取配置文件的url
        keysList = []
        urlDict = {}
        keysList = self.iniObj.getKeysBySection('url')
        for key in keysList:
            pageCode = ''
            url = ''
            url = self.iniObj.getValue('url',key)
            urlDict.setdefault(key,url)
            #url = "http://kxyesit.cnsuning.com/"
            try:
                #创建请求的request
                req = urllib2.Request(url)
                handler = urllib2.HTTPCookieProcessor(cookie)
                #利用urllib2的build_opener方法创建一个opener
                openner = urllib2.build_opener(handler)
                responseCode = openner.open(req).getcode()
                pageCode = u'状态码:' + str(responseCode)
                self.iniObjResult.setValue(section='result',key=key,value=pageCode)
            except urllib2.URLError,e:
                reason = e.reason
                pageCode = u'状态码:' + str(e.code) + u';错误原因:' + reason
                self.iniObjResult.setValue(section='result',key=key,value=pageCode)

    def setCode(self):
        #设置code节点
        codeUtil = CodeUtil(self.resultIniPath)
        codeUtil.codeStat()

    def setHtml(self):
        #设置html并打开
        createHtml = CreateHtml(self.resultIniPath,self.htmlPath)



runCode = RunCode()
runCode.run()


