# -*- coding:utf-8 -*-
import os
import xlsxwriter
from iniUtil import IniUtil
import time

class ExcelUtil:

    #初始化
    def __init__(self):
        self.nowTile = time.strftime('%Y%m%d%H%M%S')
        self.nowPath = os.getcwd()
        self.configIniPath = self.nowPath + "/../config/tdk.ini"
        self.filePath = self.nowPath + "/../result/result_"+ self.nowTile+".xlsx"
        #创建并打开workbook
        self.workbook = xlsxwriter.Workbook(self.filePath)
        #从配置文件获取标签集合
        self.htmlLabel = self.getHtmlLabel()
        #self.htmlLabel = ['title','a','h1','h2','h3']
        #border：边框，align:对齐方式，bg_color：背景颜色，font_size：字体大小，bold：字体加粗
        self.top = self.workbook.add_format({'border':1,'align':'center','bg_color':'cccccc','font_size':15,'bold':True})
        #border：边框，align:对齐方式，bg_color：背景颜色，font_size：字体大小，bold：字体加粗
        self.content = self.workbook.add_format({'border':1,'align':'wrap on','bg_color':'#05FD4F','font_size':12,'bold':True})

    #从配置文件读取标题
    def getHtmlLabel(self):
        iniObj = IniUtil(self.configIniPath)
        sections = iniObj.getSections()
        list = []
        for sec in sections:
            tmpList = iniObj.getKeysBySection(sec)
            list.extend(tmpList)
        return list

    #关闭workbook
    def closeExcel(self):
        self.workbook.close()

    #增加sheet页
    def addSheet(self,sheetName):
        worksheet = self.workbook.add_worksheet(sheetName)
        return worksheet

    #写入第一行的title值
    def setKeys(self,worksheet):
        #设置第一行行高
        worksheet.set_row(0,30)
        len = self.htmlLabel.__len__()
        #设定其他列的宽度
        worksheet.set_column(0,len,20)
        #设定【a标签】列的宽度
        aColumn = self.htmlLabel.index('a')
        worksheet.set_column(aColumn,aColumn,40)
        column = 0
        #循环写入需要获取的html标签
        for key in self.htmlLabel:
            worksheet.write(0,column,key,self.top)
            column += 1

    #设置内容
    def setValue(self,worksheet,row,key,value):
        keyColumn = self.htmlLabel.index(key)
        worksheet.set_row(row,20)
        worksheet.write(row,keyColumn,value,self.content)


'''
a = excelUtil()
ws = a.addSheet(u'首页')
a.setKeys(ws)
a.setValue(ws,1,'title',value=u'科学育儿免费解答各种育儿问题,育儿知识,育儿常识,帮助宝宝们幸福快乐的成长')
a.closeExcel()
'''