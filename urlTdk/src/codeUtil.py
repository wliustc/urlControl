# -*- coding:utf-8 -*-
from iniUtil import IniUtil

class CodeUtil:
    def __init__(self,filePath):
        self.iniObj = IniUtil(filePath)

    #设置code节点
    def codeStat(self):
        keyList = self.iniObj.getKeysBySection('result')
        for title in keyList:
            code_reason_Str = self.iniObj.getValue('result',title)
            codeStr = code_reason_Str.split(";")[0]
            code = codeStr.split(":")[1]
            self.setCode(code)

    #设置单个状态码数量
    def setCode(self,code):
        self.iniObj.addSection("code")
        flag = self.iniObj.getValue("code",code)
        #状态码存在
        if flag:
            num = int(flag) + 1
            self.iniObj.setValue("code",code,str(num))
        #状态码不存在，新增状态码key，初始值为1
        else:
            self.iniObj.setValue("code",code,"1")

#codeUtil = CodeUtil()
#codeUtil.codeStat()