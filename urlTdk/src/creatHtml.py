# -*- coding:utf-8 -*-
import sys
from iniUtil import IniUtil
from selenium import webdriver
import os
reload(sys)
sys.setdefaultencoding('utf-8')

class CreateHtml:

    def __init__(self,resultIniPath,htmlPath):
        html = open(htmlPath, 'w+')
        #iniObj = IniUtil('../log/result.ini')
        iniObj = IniUtil(resultIniPath)
        strFirst = '''
        <html>
         <head>
          <meta charset="utf-8" />
          <title>状态码</title>
         </head>
         <body>
          <table align="center" width="80%" border="1">
           <tbody>
            <tr>
             <td colspan="3" align="center">
              <!-- 为ECharts准备一个具备大小（宽高）的Dom -->
              <div id="codeImg" style="height:300px;width:400px;"></div> </td>
            </tr>
            <tr>
             <td colspan="3" align="center">
              <table width="100%" border="1" cellspacing="0" cellpadding="0" class="sp-order-table">
               <thead>
                <tr bgcolor="#CECEFF">
                 <td>标题</td>
                 <td>URL</td>
                 <td>状态码</td>
                 <td>结果</td>
                </tr>
               </thead>
        '''
        colorRed = "style='color:#FF0000'"
        colorGreen = "style='color:#00FF7F'"
        titleList = iniObj.getKeysBySection('result')
        strTbody = '<tbody>'
        codeStr = ''
        code = ''
        reasonStr = ''
        reason = ''
        colorFlag = ''
        for title in titleList:
            codeStr = ''
            reasonStr = ''
            code_reason_Str = iniObj.getValue('result',title)
            if ";" in code_reason_Str:
                codeStr = code_reason_Str.split(";")[0]
                #code = codeStr.split(":")[1]
                reasonStr = code_reason_Str.split(";")[1]
               #reason = reasonStr.split(":")[1]
                colorFlag = colorRed
            else:
                reasonStr = '通过'
                codeStr = code_reason_Str.split(";")[0]
                #code = codeStr.split(":")[1]
                colorFlag = colorGreen
            strTbody += "<tr>"
            strTbody += "<td>"+title+"</td>"
            strTbody += "<td>"+iniObj.getValue('result',title)+"</td>"
            strTbody += "<td>"+codeStr+"</td>"
            strTbody += "<td "+colorFlag+">"+reasonStr+"</td>"
            strTbody += "</tr>"
        strTbody +='</tbody>'
        strSecond='''
              </table>
              </td>
            </tr>
           </tbody>
          </table>
          <!-- ECharts单文件引入 -->
          <script src="../config/echarts.common.min.js"></script>
          <style>
            body{ text-align:center}
            .sp-order-table {
                clear: both;
                border: 1px solid #ebebeb;
                margin-top: 20px;
            }
          </style>
          <script type="text/javascript">
            // 基于准备好的dom，初始化echarts图表
            var myChart = echarts.init(document.getElementById('codeImg'));
            var option = {
            //标题
            title : {
                text: '状态码',
                //subtext: '纯属虚构',
                x:'center'
            },
        '''
        dataName = '['
        data = ''
        strThird = ''
        codeList = iniObj.getKeysBySection('code')
        for codeName in codeList:
            dataName += "'" + codeName + "',"
            num = iniObj.getValue('code',codeName)
            data += "{value:"+num+", name:'"+codeName+"'},"
        dataName = dataName[:-1] + ']'
        strThird = '''
            //左侧竖直列
            legend: {
                orient : 'vertical',
                x : 'left',
                data:'''+dataName+'''
            },
            //饼图值
            series : [
                {
                    name:'状态码',
                    type:'pie',
                    radius : '55%',
                    center: ['50%', '60%'],
                    data:['''+data[:-1]+'''
                    ]
                }
            ]
        };
        '''
        strFour = '''
            // 为echarts对象加载数据
            myChart.setOption(option);
          </script>
         </body>
        </html>
        '''
        strHtml = strFirst+strTbody+strSecond+strThird+strFour
        html.write(strHtml)
        html.close()

    #打开报告html
    def openHtml(self):
        nowPath = sys.path[0]
        htmlPath = os.path.dirname(nowPath) + "/config/index.html"
        driver = webdriver.open(htmlPath)

#nowPath = sys.path[0]
#htmlPath = os.path.dirname(nowPath) + "/config/index.html"
#print htmlPath
#os.system(htmlPath)