#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import os, os.path, sys
import time

from common import util
from process_manifest import ProcessManifest

from common.DataOperate import OperateAppStaticInfor

class ApkStaticAnalysis:
    
    def __init__(self, fileName, filePath):
        self.apkFileName = fileName
        self.filePath = filePath
        self.apkFilePath = self.filePath + os.sep +self.apkFileName
        self.apkDecoderFolderName = self.apkFileName + "_decoder"
        self.decoderFolderPath = self.filePath + os.sep +self.apkDecoderFolderName
        
    @staticmethod    
    def ApktoolDecodeStatic(self, apkFilePath, apkDecodeFolderPath):
        '''
        函数功能：使用apktool对apk文件进行解码
        参数：apkFilePath 待解码的apk文件的路径
             apkDecodeFolderPath 保存解码后内容的文件的路径
        apktool d <file.apk> <dir>
        '''
        pass
        command ="apktool d %s  %s"%(apkFilePath, apkDecodeFolderPath)
        print command
        util.sh(command, False, False, False)
        
    def ApktoolDecode(self):
        '''
        函数功能：使用apktool对apk文件进行解码
        参数：apkFilePath 待解码的apk文件的路径
             apkDecodeFolderPath 保存解码后内容的文件的路径
        apktool d <file.apk> <dir>
        '''
        pass
        command ="apktool d %s  %s"%(self.apkFilePath, self.decoderFolderPath)
        print command
        util.sh(command, True, True, False)
 
    def StaticAnalysis(self):
        '''
        函数功能：对静态文件进行分析
        '''
        self.processManifest = ProcessManifest()
        manifestFilePath = self.decoderFolderPath + os.sep + "AndroidManifest.xml"
        print manifestFilePath

        self.processManifest.ParseManifestFile(manifestFilePath)

 
    def SaveStaticInfor(self, apkInfor):
        
        flag, data = OperateAppStaticInfor.SearchFileInforFromTaskTable(apkInfor["md5"])
        if flag == False:
            OperateAppStaticInfor.InsertAppStaticInfor(self.processManifest, apkInfor)

def main():
        

    #ApkStaticAnalysis.ApktoolDecode("/home/anbc/test/360MobileSafe_4.3.2.1032.apk", "/home/anbc/test/360MobileSafe")
    apkStaticAyalysis = ApkStaticAnalysis("360MobileSafe_4.3.2.1032.apk", "/home/anbc/test")
    apkStaticAyalysis.ApktoolDecode()
    apkStaticAyalysis.StaticAnalysis()
    print apkStaticAyalysis.processManifest.packageName
    print apkStaticAyalysis.processManifest.launcherActivity


if __name__ == '__main__':
    main() 
 
 
 
 
 
 
  