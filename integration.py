#!/usr/bin/env python
# -*- coding: utf-8 -*- 


import os, os.path, sys, time
import hashlib
import shutil


from static.apk_operate import ApkOperate
from static.apk_static_analysis import ApkStaticAnalysis
from static.emulator_operate import EmulatorOperate
from dynamic.parse_action_log import ParseActionLog
from common import config
from common import util


'''
字典apkInfor包含的内容：
apkInfor["apk_file_name"]  待检测apk文件的名称
apkInfor["source_path"]  apk文件所在的源文件夹路径
apkInfor["package_name"] apk文件的报名
apkInfor["launcher_activity_name"] apk首个启动的activity的名称
apkInfor["md5"] apk的md5值  
apkInfor["apk_work_folder"]  apk文件的工作目录  
apkInfor["monitor_log_file_path"]  动态监控文件路径
apkInfor["apktool_folder_path"]  apktool工具获得的静态数据的保存路径


'''
def ApktoolDecode():
    '''
    函数功能：使用apktool对apk文件进行解码
    '''
    
    
def BatchRunApks(emulator_name, apk_files=[]):
    '''
    函数功能：批量运行程序
    ''' 
    #InstallApk(apk_file_path, emulator_name=None):
    EmulatorOperate.RunEmulator(emulator_name)
    RunApkFileMonitor(apk_files)
        

def RunApkFileMonitor(apkInforList=[]):
    '''
    函数功能：运行多个文件进行监控
    '''
    for apkInfor in apkInforList:
        apkFilePath = apkInfor["apk_work_folder"] + os.sep + apkInfor["apk_file_name"]
        ApkOperate.InstallApk(apkFilePath) 
        ApkOperate.SetDebugModel(apkInfor["package_name"])
        ApkOperate.RunApkProgram(apkInfor["package_name"], apkInfor["launcher_activity_name"])     
        
        ApkOperate.StartupMonitorApk(apkInfor, config.g_waitTimeForRunApk)

        
        ApkOperate.StopApkProgram(apkInfor["package_name"])
        
        if config.g_isUninstallApk==True:
            ApkOperate.UninstallApk(apkInfor["package_name"])
        

        
def StaticAnalysisApk(apkInforList):
    '''
    函数功能：对apk文件进行静态分析
    '''
    for apkInfor in apkInforList:
        apkStaticAyalysis = ApkStaticAnalysis(apkInfor["apk_file_name"], apkInfor["apk_work_folder"])
        apkStaticAyalysis.ApktoolDecode() 
        apkStaticAyalysis.StaticAnalysis()
        apkStaticAyalysis.SaveStaticInfor(apkInfor)
        
        apkInfor["package_name"] = apkStaticAyalysis.processManifest.packageName
        apkInfor["launcher_activity_name"] = apkStaticAyalysis.processManifest.launcherActivity
        print "［package name］:%s \t ［launcher activity name］:%s "%(apkStaticAyalysis.processManifest.packageName, apkStaticAyalysis.processManifest.launcherActivity)    



def CreatWorkPlatform(apkInforList):
    '''
    函数功能：为待检测的apk文件生成工作目录
    
    '''
    
    sampleFolder = config.g_workFolderPath + os.sep + config.g_sampleFolder 
    isExit = os.path.exists(sampleFolder)
    if isExit==False:
        os.mkdir(sampleFolder)
        
    for apkInfor in apkInforList:
        apkFolder = sampleFolder + os.sep  + apkInfor["md5"]
        isExit = os.path.exists(apkFolder)
        if isExit==True:
          
            shutil.rmtree(apkFolder)
            
        os.mkdir(apkFolder) #创建特定apk文件的工作目录
        newFilePath = apkFolder + os.sep + apkInfor["apk_file_name"]
        oldFilePath = apkInfor["source_path"] + os.sep + apkInfor["apk_file_name"]
        shutil.copy(oldFilePath, newFilePath)   
        
        apkInfor["apk_work_folder"] = apkFolder
        
    
def GenMd5(apkInforList): 
    '''
    函数功能：增加md5信息
    '''
    
    for apkInfor in apkInforList:
        filePath = apkInfor["source_path"] + os.sep + apkInfor["apk_file_name"]
        flag, md5= util.FileMd5(filePath)
        if flag==True:
            apkInfor["md5"] = md5

def ProcessMonitorInfor(apkInforList):
    '''
    函数功能：将监控获取的调用信息进行解析，并保存到数据库中
    参数：apkInforList
    返回值：无
    '''
    
    sampleFolder = config.g_workFolderPath + os.sep + config.g_sampleFolder 
    for apkInforItem in apkInforList:
        monitorFilePath = sampleFolder + os.sep + apkInforItem["md5"] + os.sep + config.g_actionMonitor
        parseActionLog = ParseActionLog()
        parseActionLog.ParseLogFile(monitorFilePath, apkInforItem["md5"])
  
    
def main():
   
    '''
    apkInforList=[{"apk_file_name":"29510.apk","source_path":"/home/anbc/test/audit_run"},
                  {"apk_file_name":"29511.apk","source_path":"/home/anbc/test/audit_run"},
                  {"apk_file_name":"29512.apk","source_path":"/home/anbc/test/audit_run"},
                  {"apk_file_name":"29513.apk","source_path":"/home/anbc/test/audit_run"},
                  {"apk_file_name":"29514.apk","source_path":"/home/anbc/test/audit_run"},
                  {"apk_file_name":"29515.apk","source_path":"/home/anbc/test/audit_run"},
                  {"apk_file_name":"29516.apk","source_path":"/home/anbc/test/audit_run"},
                  {"apk_file_name":"29517.apk","source_path":"/home/anbc/test/audit_run"},
                  {"apk_file_name":"29518.apk","source_path":"/home/anbc/test/audit_run"},
                  {"apk_file_name":"29519.apk","source_path":"/home/anbc/test/audit_run"}]
    '''
    
    apkInforList=[{"apk_file_name":"13750.apk","source_path":"/home/anbc/test/audit_run"}]
    GenMd5(apkInforList)
    CreatWorkPlatform(apkInforList)
    StaticAnalysisApk(apkInforList)
    
    print apkInforList
    RunApkFileMonitor(apkInforList)
    
   
   
    #apkInforList=[{"md5":"174daed8a4643f45f9c33491601797a7"}]
    ProcessMonitorInfor(apkInforList)
    
    print str(apkInforList[0]["md5"])
    print "game over"

'''
subprocess.Popen stdin参数
应该可以满足多参数输入的需求。还待进一步确认
'''
if __name__ == '__main__':
    main()