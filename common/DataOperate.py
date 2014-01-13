#! /usr/bin/env python
#coding=utf-8


import logging, json

import data
import config
import datetime


class OperateAppStaticInfor:
    '''
    类功能：通过操作audit_static_infor数据，实现apk静态信息的保存
    '''

    @staticmethod
    def SearchFileInforFromTaskTable(fileMd5):    
        '''
        函数功能：以文件的md5值为关键字，是否有该apk文件
        参数：fileMd5 apk文件的md5值
        返回值：找到了返回True，并返回查到的结果， 如果没找返回false和空结果
        注：以文件的md5为关键字查询
        '''
        sql = 'select * from app_static_infor where file_md5=%s'

        values =[fileMd5]

        rcds = data.iquery(config.g_curDatabaseName,sql, values)
        if len(rcds)>0:
            return True, rcds
        else:
            return False, rcds


    @staticmethod
    def InsertAppStaticInfor(manifestInfor, apkInfor):
        '''
        函数功能：将静态数据插入表中
        参数：manifestInfor manifest文件中的静态数据
        注：改为多个检测引擎，多条扫描任务
        '''

 
        sql = ("INSERT INTO app_static_infor (file_md5, package_name, launcher_activity, uses_permission_infor,"
               "activity_infor, service_infor, receiver_infor, provider_infor, metaDataDict)"
            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)")

                             
        values = []
        values.append(apkInfor["md5"])
        values.append(manifestInfor.packageName)
        values.append(manifestInfor.launcherActivity)
        
        usesPermissionJsonInfor =  json.dumps(manifestInfor.usesPermission)
        values.append(usesPermissionJsonInfor)
        
        activityJsonInfor = json.dumps(manifestInfor.activityInfor)
        values.append(activityJsonInfor)
        
        serviceJsonInfor = json.dumps(manifestInfor.serviceInfor)
        values.append(serviceJsonInfor)
        
        reveiverJsonInfor = json.dumps(manifestInfor.receiverInfor)
        values.append(reveiverJsonInfor)
        
        providerJsonInfor = json.dumps(manifestInfor.providerInfor)
        values.append(providerJsonInfor)
        
        metaDataDictJsonInfor = json.dumps(manifestInfor.metaDataDict)
        values.append(metaDataDictJsonInfor )        
        

        
        #adJsonInfor = json.dumps(manifestInfor.adInfor) #广告信息
        #values.append("")
        
        data.iexecute(config.g_curDatabaseName, sql, values)
        

'''
app_dynamic_monitor_action
+-----------+-------------+------+-----+---------+----------------+
| Field     | Type        | Null | Key | Default | Extra          |
+-----------+-------------+------+-----+---------+----------------+
| id        | bigint(20)  | NO   | PRI | NULL    | auto_increment |
| action_id | varchar(64) | NO   |     | NULL    |                |
| file_md5  | varchar(64) | YES  |     | NULL    |                |
| time      | varchar(64) | YES  |     | NULL    |                |
| order     | int(11)     | YES  |     | NULL    |                |
| thread    | varchar(64) | YES  |     | NULL    |                |
| funciton  | varchar(64) | YES  |     | NULL    |                |
| fun_args  | text        | YES  |     | NULL    |                |
| fun_ret   | text        | YES  |     | NULL    |                |
| is_native | tinyint(1)  | YES  |     | 1       |                |
+-----------+-------------+------+-----+---------+----------------+
monitorInfor字典的定义：
monitorData["md5"] = fileMd5
monitorData["action_id"] = str(uuid.uuid1())
monitorData["time"] = time
monitorData["order"] = self.order
monitorData["thread"] = threadInfor
monitorData["function"] = functionInfor
monitorData["args"] = argsInfor
monitorData["isNative"] = isNativeInfor


'''

class OperateMonitorInfor:
    '''
    类功能：通过操作app_dynamic_monitor_action数据，实现apk静态信息的保存
    '''

    @staticmethod
    def SearchMonitorInfor(fileMd5):  
        pass




    @staticmethod
    def InsertMonitorInfor(monitorInfor):
        '''
        函数功能：将静态数据插入表中
        参数：manifestInfor manifest文件中的静态数据
        注：改为多个检测引擎，多条扫描任务
        '''

 
        sql = ("INSERT INTO app_dynamic_monitor_action (file_md5 , action_id, time , micro_second,serial,"
               "thread, function, fun_args, fun_ret, is_native)"
            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")

      
        time = monitorInfor["time"]
        timeData = time.split(",")
                 
        values = []
        values.append(monitorInfor["md5"])
        values.append(monitorInfor["action_id"])
        values.append(timeData[0])
        values.append(int(timeData[1]))
        values.append(monitorInfor["order"])
        
        values.append(monitorInfor["thread"])
        values.append(monitorInfor["function"])
        values.append(monitorInfor["args"])
        values.append(monitorInfor["ret"])
        values.append(monitorInfor["isNative"])
      
        data.iexecute(config.g_curDatabaseName, sql, values)


    
def main():
    print 'start'    

    monitorData={}
    monitorData["md5"] = "1"
    monitorData["action_id"] = "2"
    #monitorData["time"] = datetime.datetime.now()
    monitorData["time"] ="2013-12-18 10:49:33,234"
    #monitorData["time"] = "2009-06-09 00:24:08"
    #monitorData["time"] = "3"
    monitorData["order"] = 4
    monitorData["thread"] = "5"
    monitorData["function"] = "6"
    monitorData["args"] = "7"
    monitorData["isNative"] = "8"
    monitorData["ret"] = "9"
    
    
    OperateMonitorInfor.InsertMonitorInfor(monitorData)
    
    
    
    
    print 'end' 

    

if __name__ == '__main__':
    main()     
    
    
    
    
    
    
    
    
    
    
    
    
