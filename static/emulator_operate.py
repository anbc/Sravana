#!/usr/bin/env python
# -*- coding: utf-8 -*- 


import os, os.path, sys

from common import util




class EmulatorOperate:
    
    
    @staticmethod
    def CreatEmulator(emulator_name, target_id):
        '''
        函数功能：创建一个模拟器
        参数：emulator_name 模拟器的名称
             target_id  android SDK的版本id
        例子：　　android create avd -n Android_2 -t 2
        ''' 
        command = "android create avd -n %s -t %d"%(emulator_name, target_id)
        print command
        process = util.ShellIO(command)
        process.stdin.write("no \n")
        process.stdin.flush()
        
        
    @staticmethod
    def RunEmulator(emulator_name):
        '''
        函数功能：运行模拟器
        参数：emulator_name 模拟器的名称
        例子:emulator -avd android4.2.2
        '''
        command = "emulator -avd %s"%(emulator_name)
        print command
        #process = util.ShellIO(command)
        util.sh(command, False, False, True)


    @staticmethod
    def DeleteEmulator(emulator_name):
        '''
        函数功能：删除指定的模拟器
        参数：emulator_name 模拟器的名称
        例子：android delete avd –n android4.2.2
        '''    
        command = "android delete avd -n %s"%(emulator_name)
        print command
        #process = ShellIO(command)
        util.sh(command, False, False, False)
    
    @staticmethod
    def DevicesListStatus():
        '''
        函数功能：列举出当前运行模拟器的状态
        参数：无
        例子：adb devices
        '''
        command = "adb devices"
        print command
        #process = ShellIO(command)
        util.sh(command, False, False, False)
     
        
        
def main():
        
    #CreatEmulator("Android37", 3)  #创建模拟器
    EmulatorOperate.RunEmulator("Android_7")    #运行模拟器
    #DeleteEmulator("Android_6") #删除模拟器
    #DevicesListStatus()  #显示模拟器列表

    print "game over"


if __name__ == '__main__':
    main()