# -*- coding:utf-8 -*-
import os
from configobj import ConfigObj

class IniUtil:

    def __init__(self,configIni):
        self.config = ConfigObj(configIni,encoding='UTF8')


    #获取所有的section
    def getSections(self):
        section = self.config.keys()
        return section

    #获取section下所有的key
    def getKeysBySection(self,section):
        if self.config.sections.__contains__(section):
            sectionKeys = self.config[section]
            if sectionKeys!=None:
                return sectionKeys.keys()
            else:
                return ""
        else:
            return ""

    #根据section和key获取值
    def getValue(self,section,key):
        if self.config.sections.__contains__(section):
            sec = self.config[section]
            if sec.__contains__(key):
                value =  self.config[section][key]
                if value != None:
                    return value
                else:
                    return False
            else:
                return False
        else:
            return False
    #添加section
    def addSection(self,section):
        if self.config.sections.__contains__(section):
            sect = self.config[section]
        else:
            self.config[section] = {}
            self.config.write()

    #修改值
    def setValue(self,section,key,value):
        if self.config.sections.__contains__(section):
            self.config[section][key] = value
        else:
            self.config[section] = {}
            self.config[section][key] = value
        self.config.write()

    #删除key-value
    def delKey_Value(self,section,key):
        if self.config.sections.__contains__(section):
            del self.config[section][key]
        self.config.write()

#iniObj = IniUtil('../config/url.ini')
#iniObj.setValue(section=u'状态码',key='1',value='')