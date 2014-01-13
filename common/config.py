#! /usr/bin/env python
#coding=utf-8

import os



#当前的工作目录
g_workFolderPath = os.getcwd()  #工作路径
g_sampleFolder = "sample"  #保存样本的文件夹名称，在工作路径下
g_actionMonitor = "action_monitor.log"  #设置保存监控信息的文件名

g_waitTimeForRunApk = 30  #设置待检测文件在虚拟机中的时间
#g_isUninstallApk = True #监控完成后，是否卸载被监控apk
g_isUninstallApk = False #监控完成后，是否卸载被监控apk

g_curDatabaseName = "loc_db_test" #选择要使用的数据 [部署时需要修改的配置]
g_databaseInfor = {"loc_db_online":  #数据库服务器的名称
                        {"addr":"127.0.0.1",  #数据库服务器的Ip
                         "port": 3306, #数据库服务器的端口
                         "db_name": "audit", #数据库的名称
                         #"user": "root", #数据库访问的用户名
                         #"password":"0cf0b12e4e5ec08c",
                         "user":"audit",
                         "password":"3df202e44e22e36be7ed8895154e933c",
                         "watch_dog":False
                         }, 
                   "loc_db_test":  #数据库服务器的名称
                        {"addr":"127.0.0.1",  #数据库服务器的Ip
                         "port": 3306, #数据库服务器的端口
                         "db_name": "audit", #数据库的名称
                         "user": "root", #数据库访问的用户名
                         "password":"0cf0b12e4e5ec08c",
                         #"user":"audit",
                         #"password":"3df202e44e22e36be7ed8895154e933c",
                         "watch_dog":False
                         }
                   
                   }