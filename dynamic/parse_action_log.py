#!/usr/bin/env python
# -*- coding: utf-8 -*- 


import json
import uuid

from common.DataOperate import OperateMonitorInfor

class ParseActionLog():
    '''
    类功能：对生成的日志信息进行解析，并写入数据库
    '''
    
    def __init__(self):
        pass
    
    def ParseLogFile(self, filePath, fileMd5="0000"):
        '''
        函数功能：对指定的log文件进行解析
        参数：   filePath 日志文件的路径
                md5    被监控文件的md5值
        '''
        self.order= 0
        self.uuid = str(uuid.uuid1())
        fp = open(filePath,"r")    
        for line in fp:  
            print line
            self.ParseLogItem(line, fileMd5)
            
        fp.close()
        
    def ParseLogItem(self, lineData, fileMd5):
        '''
        函数功能：对一条日志信息进行解析
        参数：lineData 一条日志数据
            fileMd5 文件的md5值
        '''
        #2013-12-18 13:52:43,592 monitor.py[line:80]
        index = lineData.find("monitor")
        time = lineData[: index-1]
        index = lineData.find("DEBUG")
        actionData = lineData[index+6:]
        
        jsonData = json.loads(actionData)
        threadInfor = jsonData["thread"]
        index = threadInfor.find("(running suspended)")
        threadInfor = threadInfor[:index-1]
        functionInfor = jsonData["name"]
        argsInforJson = jsonData["args"]
        argsInfor = json.dumps(argsInforJson)
        isNativeInfor = jsonData["is_native"]
        
        
        
        monitorData={}
        monitorData["md5"] = fileMd5
        monitorData["action_id"] = self.uuid 
        monitorData["time"] = time
        monitorData["order"] = self.order
        monitorData["thread"] = threadInfor
        monitorData["function"] = functionInfor
        monitorData["args"] = argsInfor
        monitorData["isNative"] = isNativeInfor
        monitorData["ret"] = ""
        
        print "thread:" + threadInfor
        print "function:" + functionInfor
        print "argsInfor:" + argsInfor
        print "isNative:" + str(isNativeInfor)        
        print "time:" + time
        print "uuid:" + str(monitorData["action_id"] )

        OperateMonitorInfor.InsertMonitorInfor(monitorData)
        
        
        self.order +=1
            
def main():
        
 
    parseActionLog = ParseActionLog()
    parseActionLog.ParseLogFile("/home/anbc/workspace/diting/sample/3aff2a49c40db0ee3bb44a868d4ddc83/3aff2a49c40db0ee3bb44a868d4ddc83.log")
    
    print "game over"



if __name__ == '__main__':
    main()