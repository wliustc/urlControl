# -*- coding:utf-8 -*-


class LogUtil:

    def duplicateList(self,oldList):
        newList = []
        for str in oldList:
            if newList.__contains__(str):
                continue
            else:
                newList.append(str)
        return newList

    def setKeyLog(self,filePath,list):
        list = self.duplicateList(list)
        f = file(filePath,"w+")
        f.write('重复的key：')
        f.write('\n')
        for str in list:
            f.write(str)
            f.write('\n')
        f.close()

    def setUrlLog(self,filePath,list):
        list = self.duplicateList(list)
        f = file(filePath,"a+")
        f.write('不合法的Url：')
        f.write('\n')
        for str in list:
            f.write(str)
            f.write('\n')
        f.close()