#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import os, os.path, sys, time
from common import util
from common import config


class ApkOperate:
    
    @staticmethod
    def InstallApk(apk_file_path, emulator_name=None):
        '''
        函数功能：安装一个apk文件到模拟器
        参数：apk_file_path 要安装的apk文件的路径
        例子：adb install SoundRecorder.apk
        '''
        if emulator_name==None:
            command = "adb install %s"%(apk_file_path)
        else:
            command = "adb -s %s install %s"%(emulator_name,apk_file_path)
        util.sh(command, False, False, False)


    @staticmethod
    def UninstallApk(apk_packet_name):
        '''
        函数功能：卸载一个apk文件
        参数：apk_packet_name 包名称
        例子：adb uninstall com.doodoobird.anttest 
        '''
    
        command = "adb uninstall %s"%(apk_packet_name)
        util.sh(command, False, False, False) 
        
    @staticmethod
    def SetDebugModel(apk_packet_name):
        '''
        函数功能：将指定的apk程序设置为调试模式
        参数：apk_packet_name  监控目标apk的包名
        例子：adb shell am set-debug-app -w com.android.browser
        '''
    
        command = "adb shell am set-debug-app -w %s"%(apk_packet_name)
        print command
        util.sh(command, False, False, False)
        
    @staticmethod  
    def ClearDebugModel(apk_packet_name):
        '''
        函数功能：清楚指定应用的调试标签
        参数：apk_packet_name 应用的包名
        例子： adb shell am clear-debug-app 
        '''
        
        command = "adb shell am clear-debug-app"
        util.sh(command, False, False, False)

    @staticmethod
    def RunApkProgram(apk_packet_name, activity_name):
        '''
        函数功能：将一个apk文件运行起来
        参数：apk_packet_name  包名
             activity_name  activity 活动的名称
        例子：adb shell am start -n com.android.browser/com.android.browser.BrowserActivity    
        '''    
        index=activity_name.find(activity_name)
        if index==0:
            #处理：adb shell am start -n com.android.browser/com.android.browser.BrowserActivity
            command = "adb shell am start -n  %s/%s"%(apk_packet_name, activity_name)
        
        index = activity_name.find(".")
        if index==0:
            #处理：adb shell am start -n com.android.browser/.BrowserActivity
            command = "adb shell am start -n  %s/%s"%(apk_packet_name, activity_name)
        else:
            #处理：adb shell am start -n com.android.browser/BrowserActivity 在前边加一个.
            command = "adb shell am start -n  %s/.%s"%(apk_packet_name, activity_name)
            
            
        print command
        util.sh(command, False, False, False)
        
    @staticmethod
    def StopApkProgram(apk_packet_name):
        '''
        函数功能：终止一个apk文件的运行
        参数：apk_packet_name 被终止apk文件的包名
        例子： adb shell am force-stop com.lt.test
        '''
        command = "adb shell am force-stop %s"%(apk_packet_name)
        print command
        util.sh(command, False, False, False)
        
        
        
    @staticmethod
    def StartupMonitorApk(apkInfor, wait_time=20):
        '''
        函数功能：启动apk监控
        参数：apk_packet_name apk的包名
        例子：andbug monitor -p com.android.browser
        '''
        apk_packet_name = apkInfor["package_name"]
        apk_md5 = apkInfor["md5"]
        monitor_log_file_path = apkInfor["apk_work_folder"] + os.sep + config.g_actionMonitor
        command = "andbug monitor -p %s  %s"%(apk_packet_name, monitor_log_file_path)
        #command = "andbug"
        #command = "/home/anbc/Work/run/apktool"
        print command
        #util.sh(command, False, True, False)  
        process = util.ShellIO(command, wait_time)
        
        '''
        print "begin sleep"
        time.sleep(wait_time) 
        print "end sleep"
        print "out:" + process.stdout.read()
        process.stdin.write("exit \n")
        process.stdin.flush()
        '''
    
def main():
        
        

    #ApkOperate.InstallApk("/home/anbc/test/apk11123.apk", emulator_name=None)  #安装apk
    #ApkOperate.UninstallApk("com.jimu.wether.activity")  #卸载制定apk
    
    
    
    #ApkOperate.SetDebugModel("com.jimu.wether.activity")
    #adb shell am start -n com.android.browser/com.android.browser.BrowserActivity  
    #ApkOperate.RunApkProgram("com.jimu.wether.activity", "com.jimu.wether.activity.BeijingAirActivity")
    

    #ApkOperate.StartupMonitorApk("com.jimu.wether.activity")
    ApkOperate.StopApkProgram("com.jimu.wether.activity")
    
    
    print "game over"



if __name__ == '__main__':
    main()