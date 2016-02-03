# -*- coding:utf-8 -*-
import re

class LabelUtil:

    def __init__(self,content):
        self.content = content

    #获取标题
    def getTitle(self):
        #得到标题的正则表达式
        pattern = re.compile('<title>(.*?)</title>',re.S)
        result = re.search(pattern,self.content)
        if result:
            #print result.group(1).strip()
            return result.group(1).strip()
        else:
            return False

    #获取keywords
    def getKeywords(self):
        #得到keywords的正则表达式
        pattern = re.compile("<meta name=\"keywords\" content=\"(.*?)\".*?/>",re.S)
        result = re.search(pattern,self.content)
        if result:
            #print result.group(1).strip()
            return result.group(1).strip()
        else:
            return False

    #获取description
    def getDescription(self):
        #得到description的正则表达式
        pattern = re.compile("<meta name=\"description\" content=\"(.*?)\".*?/>",re.S)
        result = re.search(pattern,self.content)
        if result:
            #print result.group(1).strip()
            return result.group(1).strip()
        else:
            return False

    #获取a标签
    def getLabel_a(self):
        #得到a的正则表达式
        pattern = re.compile("<a.*?>(.*?)</a>",re.S)
        result = re.findall(pattern,self.content)
        if result:
            for item in result:
                print item
            #return result
        else:
            print 'a'
            #return False

    #获取h1标签
    def getLabel_h1(self):
        #得到h1的正则表达式
        pattern = re.compile("<h1.*?>(.*?)</h1>",re.S)
        result = re.findall(pattern,self.content)
        if result:
            return result
        else:
            return False

    #获取h2标签
    def getLabel_h2(self):
        #得到h2的正则表达式
        pattern = re.compile("<h2.*?>(.*?)</h2>",re.S)
        result = re.findall(pattern,self.content)
        if result:
            return result
        else:
            return False
